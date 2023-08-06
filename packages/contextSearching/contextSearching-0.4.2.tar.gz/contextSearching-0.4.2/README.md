
# Introduction

Given a word token and a corpus where this word appears, this package helps you find and analyze the context in which the word appears. It can be easily leveraged to improve your bag-of-words based analysis.

# Installation

```
pip install contextSearching
```

# Usage

As an example to illustrate the usage, we choose the term "break" and the Amazon review corpus for Nintendo Switch where people used the term "break". 

From a simple bag-of-words analysis, we know that whenever people mention "break", the product is likely to receive a low star rating. But we do not know what breaks or any other context around "break." 

### Preparation


```python
"""
Preparation
"""
import pandas as pd
import numpy as np
# read in corpus
corpus = pd.read_csv("data/switch_w_break.csv")
# define the target token
target = "break"

corpus.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>stars</th>
      <th>titles</th>
      <th>reviews</th>
      <th>dates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>Already broken parts\n</td>
      <td>Only 3 months later and parts are breaking. Th...</td>
      <td>September 13, 2019</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>Dock is broken\n</td>
      <td>Hey. This was supposed to work. Dock is broken...</td>
      <td>September 11, 2019</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.0</td>
      <td>Dependable seller\n</td>
      <td>Arrived on time,  well packed for the trip.  N...</td>
      <td>August 10, 2019</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>Nintendo Does Not Honor Warranty\n</td>
      <td>My son used this unit for 7 months.  At which ...</td>
      <td>August 8, 2019</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
      <td>Great product, Joycons need work.\n</td>
      <td>Everyone knows the switch is great. I waited a...</td>
      <td>August 5, 2019</td>
    </tr>
  </tbody>
</table>
</div>



### Loading the package and initialize the class



```python
"""
Loading the package and initialize the class
"""
from contextSearching import context_searching

cs = context_searching(target_token=target,doc=corpus['reviews'],left_window=5,right_window=5,padding_token="_empty_")
```

In addition to the target token and the corpus, the class requires three more inputs: left/right window and padding token.

The algorithm takes in the target token and aggressively collect all the words within the specified window. 

For example, when left_window is set to 10, it will find the target token within each document of the corpus, then collect all the ten words to the left of the target, recording the relative position. If there are less than 10 words to the left, the algorithm will append the word list with the padding token.

### Get the Context Probing Matrix



```python
"""
Get the Context Probing Matrix
"""
# Get a list of stopwords
from gensim.parsing.preprocessing import STOPWORDS
stopwords = list(STOPWORDS)
contextPMat = cs.get_context_prob_matrix(stop_words = stopwords,lemmatize=True, stem = False)
```

Assuming we have N documents in the corpus, and left_window and right window are set to 5. The Context Probing Matrix (CPM) is an N by 11 matrix like below:


```python
# We can examine the actual CPM like this:
cpm_df = pd.DataFrame(np.array(contextPMat.context_prob_matrix))
cpm_df.columns = [str(x) for x in contextPMat.position_idx]
cpm_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>-5</th>
      <th>-4</th>
      <th>-3</th>
      <th>-2</th>
      <th>-1</th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>_empty_</td>
      <td>_empty_</td>
      <td>_empty_</td>
      <td>month</td>
      <td>later</td>
      <td>break</td>
      <td>joy</td>
      <td>button</td>
      <td>work</td>
      <td>replace</td>
      <td>_empty_</td>
    </tr>
    <tr>
      <th>1</th>
      <td>_empty_</td>
      <td>hey</td>
      <td>suppose</td>
      <td>work</td>
      <td>dock</td>
      <td>break</td>
      <td>replace</td>
      <td>dock</td>
      <td>pretty</td>
      <td>angry</td>
      <td>_empty_</td>
    </tr>
    <tr>
      <th>2</th>
      <td>_empty_</td>
      <td>arrive</td>
      <td>time</td>
      <td>pack</td>
      <td>trip</td>
      <td>break</td>
      <td>work</td>
      <td>great</td>
      <td>_empty_</td>
      <td>_empty_</td>
      <td>_empty_</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gadget</td>
      <td>year</td>
      <td>expensive</td>
      <td>relative</td>
      <td>function</td>
      <td>break</td>
      <td>quickly</td>
      <td>support</td>
      <td>manufacturer</td>
      <td>beware</td>
      <td>nintendo</td>
    </tr>
    <tr>
      <th>4</th>
      <td>issue</td>
      <td>real</td>
      <td>button</td>
      <td>leave</td>
      <td>joycon</td>
      <td>break</td>
      <td>month</td>
      <td>fortunately</td>
      <td>nintendo</td>
      <td>replace</td>
      <td>warranty</td>
    </tr>
  </tbody>
</table>
</div>



The column index indicates the relative position. For example, in the first document, the word "button" appears two words to the right of the target term "break".

### Get the vocabs dictionary



```python
"""
Get the vocabs dictionary
"""
contextPMat.vocabs['joycon']
```




    [-1, -1, -4, -2, -2, -1, -2, 1]



The .vocabs is a dictionary whose keys are unique tokens collected in constructing the CPM, and the values are lists of recorded relative positions to the target token.

In the output above, we see the term "joycon" appears 8 times in total within the +- 5 window of the target term. It most often appears on the left side of the target term.

### Get the statistics table for each term



```python
"""
Get the statistics table for each term
"""
cpm_stats = contextPMat.get_cpm_stats_tb()
cpm_stats.cpm_stats_tb.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tokens</th>
      <th>mean</th>
      <th>variance</th>
      <th>abs_mean</th>
      <th>count</th>
      <th>median</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>month</td>
      <td>0.142857</td>
      <td>3.979592</td>
      <td>1.857143</td>
      <td>14</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>later</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>1.333333</td>
      <td>3</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>break</td>
      <td>0.186441</td>
      <td>0.643206</td>
      <td>0.186441</td>
      <td>118</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>joy</td>
      <td>-1.444444</td>
      <td>6.024691</td>
      <td>2.555556</td>
      <td>9</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>button</td>
      <td>-0.500000</td>
      <td>2.583333</td>
      <td>1.500000</td>
      <td>6</td>
      <td>-1.0</td>
    </tr>
  </tbody>
</table>
</div>



To understand the context, we can look at the statistics of relative positions for each term collected above. 

For example,

When the occurrence of a term is high, we know that it always appears around the target token;

When the variance of a term's relative position is low, we know that it always appears at the same relative location;

### Infer potential N-grams containing the target term



```python
"""
Infer potential N-grams containing the term
"""
cpm_stats.guess_ngram(n = 5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ngram_candidates</th>
      <th>total_scores</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>look expensive joycon controller break</td>
      <td>0.327352</td>
    </tr>
    <tr>
      <th>1</th>
      <td>expensive joycon controller break month</td>
      <td>0.330129</td>
    </tr>
    <tr>
      <th>2</th>
      <td>joycon controller break month handle</td>
      <td>0.337807</td>
    </tr>
    <tr>
      <th>3</th>
      <td>controller break month handle inside</td>
      <td>0.379144</td>
    </tr>
    <tr>
      <th>4</th>
      <td>break month handle inside item</td>
      <td>0.447479</td>
    </tr>
  </tbody>
</table>
</div>



based on the statistics table, the algorithm can infer most likely n-grams containing the target term

For example, when we want to infer what is most likely the word appears to the left of "break" (i.e. with relative location = -1), we go through the following steps

0. start with a word collected in the CPM constructing process above (e.g. "controller")
1. for the word, take the mean of the observed relative positions, minus the mean by -1 and take the absolute value
2. for the word, take the median of the observed relative positions, minus the median by -1 and take the absolute value
3. Calculate 1/count
4. Calculate the variance of the relative positions of the word
5. Repeat the above on all the collected words and acquire 4 lists of metrics above (abs median difference, abs mean difference, 1/count, variance)
6. normalize the 4 lists
7. for each collected word, multiply its 4 metrics with user-defined weights and take the sum to get a final score

The best candidate words at location -1 will have the smallest final score.

When we want to find the most likely tri-grams, the algorithm considers a trigram with the target token in each possible location. Thus in the example output above, the target term "break" appears as the 5th, 4th, 3rd, 2nd and 1st term on the n-gram respectively.

Now we get more context around "break": 

**Expensive Joycon Controller breaks in months** seem to be the problem.

## Some Notes

1. Currently, when the target term appears more than once in a single document, the CPM only takes the first one into consideration. I will try to improve this in the near future

2. This method works better when we have more documents while each document is short. It will not work well on, for example, a collection of News articles.
