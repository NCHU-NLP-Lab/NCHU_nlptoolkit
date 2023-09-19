
自己蒐集的training data、字典和stopwords並且包成package，讓大家不用重複造輪子。

## Usage

安裝：`pip install NCHU_nlptoolkit`

1. 濾掉stopwords, remove stopwords 並且斷詞
p.s. rm stop words時就會跟著載入實驗室字典了
  ```
  from NCHU_nlptoolkit.cut import *
  
  # minword 是最小詞的字數(斷詞最少幾個字)
  
  # default
  cut_sentence(input string, flag=False, minword=1)

  # return segmentation with part of speech.
  cut_sentence(input string, flag=True, minword=1)
  ```
2. 載入法律辭典
   ```
   from NCHU_nlptoolkit.cut import *

   load_law_dict()
   ```
3. demo:
  * zh:

    ```
    >>> doc = '首先，對區塊鏈需要的第一個理解是，它是一種「將資料寫錄的技術」。'
    >>> cut_sentence(doc, flag=True)
    [('區塊鏈', 'n'), ('需要', 'n'), ('第一個', 'm'), ('理解', 'n'), ('一種', 'm'), ('資料', 'n'), ('寫錄', 'v'), ('技術', 'n')]
    ```

  * en:

    ```
    >>> doc = 'The City of New York, often called New York City (NYC) or simply New York, is the most populous city in the United States.'
    >>> list(cut_sentence_en(doc))
    ['City', 'New York', 'called', 'New York City', 'NYC', 'simply', 'New York', 'populous', 'city', 'United States']
    
    >>> list(cut_sentence_en(doc, flag=True))
    >>> [('City', 'NNP'), ('New York', 'NNP/NNP'), ('called', 'VBN'), ('New York City', 'NNP/NNP/NNP'), ('NYC', 'NN'), ('simply', 'RB'), ('New York', 'NNP/NNP'), ('populous', 'JJ'), ('city', 'NN'), ('United States', 'NNP/NNS')]
    ```
   