from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import pandas as pd
import underthesea
import re
import joblib
from sklearn.metrics import accuracy_score
import numpy as np


with open("vietnamese-stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set(f.read().splitlines())

with open('vocab.txt', 'r', encoding='utf-8') as f:
    vocabulary = [s.strip() for s in f]

def pre(sentence):
    # viết thường
    sl = sentence.lower()

    # bỏ dấu câu, kí tự đặc biệt
    sl1 = re.sub(r'[^a-zA-Zà-ỹÀ-Ỹ\s]', '', sl)
    # print(sl1)

    # tách từ
    arr = underthesea.word_tokenize(sl1)
    # print(arr)

    # loại bỏ từ dừng
    for i in arr:
        if i in stopwords:
            arr.remove(i)
    # print(arr)
    return arr

def bow(s):
    vector = []
    for j in vocabulary:
        if j in s:
            cnt = s.count(j)
            vector.append(cnt)
        else:
            vector.append(0)
    return np.array(vector).reshape(1,-1)
    # return vector


x_test = 'Lỗi tùm lum mà bán cho khách, làm ăn lừa đảo'

x1 = pre(x_test)
x2 = bow(x1)

model = joblib.load('naive_bayes_model.pkl')

if model.predict(x2)[0] == 0:
    print('nontoxic')
else:
    print('toxic')