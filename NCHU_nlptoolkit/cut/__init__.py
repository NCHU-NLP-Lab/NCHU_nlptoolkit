'''
this module supply some segmetation function for multiple language
also remove stopwords as well.
'''
import pickle
from pathlib import Path, PurePath

import nltk
from nltk.stem import WordNetLemmatizer
import json

STOPWORD_PKL = pickle.load(open(str(PurePath(Path(__file__).resolve().parent, '2023_stopword.pkl')), 'rb'))
STOPWORD_EN_PKL = pickle.load(open(str(PurePath(Path(__file__).resolve().parent, 'stopwords-en.pkl')), 'rb'))
WORDNET_LEMMATIZER = WordNetLemmatizer()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
import NCHU_nlptoolkit.dictionary
import jieba.posseg as pseg
import jieba
jieba.initialize()
def cut_sentence(doc, flag=False,minword=1):
    '''
    parameter:
      doc: input string
      flag: boolean, if true will return segment with pos.
    '''
    def is_chinese(keyword):
        for uchar in keyword:
            if '\u4e00' <= uchar <= '\u9fff':
                continue
            else:
                return False
        return True

    def is_english(keyword):
        if not is_chinese(keyword) and keyword.isalpha():
            return True
        return False

    doc = doc.strip()

    # flag means showing part of speech
    if flag:
        return  list(tuple(i) for i in pseg.cut(doc)
                if i.word not in STOPWORD_PKL
                and ((is_chinese(i.word) and len(i.word)>=minword) or (is_english(i.word) and len(i.word) >= 2))
                and i.word not in ['\xa0', '\xc2']
                and not i.word.isdigit()
                )
    else:
        return  list(i for i in jieba.cut(doc)
                if i not in STOPWORD_PKL
                and ((is_chinese(i) and len(i)>=minword) or (is_english(i) and len(i) >= 2))
                and i not in ['\xa0', '\xc2']
                and not i.isdigit()
                )

# Yang, 2018/08/08
def cut_sentence_en(doc, flag=False):
    '''
    parameter:
      doc: input string
      flag: boolean, if true will return segment with pos.
    '''
    def has_numbers(input_string):
        return any(char.isdigit() for char in input_string)

    import re
    from nltk import ne_chunk, pos_tag, word_tokenize

    doc = doc.strip()
    chunks = ne_chunk(pos_tag(word_tokenize(doc)))
    words = [w[0] if isinstance(w, tuple) else ' '.join(t[0] for t in w) for w in chunks]
    for word in words:
        word = re.sub(r'[^a-zA-Z0-9 -]', '', word)
        if word and not has_numbers(word) and word.lower() not in STOPWORD_EN_PKL:
            if flag:
                if len(word.split()) > 1:
                    pos = '/'.join([pos_tag(word_tokenize(i))[0][1] for i in word.split()])
                else:
                    pos = pos_tag(word_tokenize(word))
                    if not pos:
                        continue
                    pos = pos[0][1]
                yield WORDNET_LEMMATIZER.lemmatize(word.lower()), pos
            else:
                yield WORDNET_LEMMATIZER.lemmatize(word.lower())
# dan 2023/3/23
def load_law_dict():
    import os
    dirpath = os.path.join(str(PurePath(Path(__file__).resolve().parent.parent,"dictionary/law.txt")))
    jieba.load_userdict(dirpath)
