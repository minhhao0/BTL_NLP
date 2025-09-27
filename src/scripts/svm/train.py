from idlelib.iomenu import encoding

import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn import model_selection,naive_bayes,svm
from sklearn.metrics import accuracy_score,consensus_score,completeness_score
#download linh tinh
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')
#get vietnamese stop words
vn_stopwords=pd.read_csv('D:\\BTL_NLP\\src\\scripts\\svm\\train_data\\vietnamese.txt',encoding='utf-8-sig')
# print(vn_stopwords)
#set random seed
np.random.seed(500)
corpus=pd.read_csv('D:\\BTL_NLP\\src\\scripts\\svm\\train_data\\comment.csv',encoding='utf-8-sig')

#preprocessing-data
def pre_process(corpus):
 #1. remove blank row
 corpus['Content'].dropna(inplace=True)
 #2. change all text to lower case
 corpus['Content']=[text.lower() for text in corpus['Content']]
 #3. tokenization
 corpus['Content']=[word_tokenize(text) for text in corpus['Content']]
 #4 remove stop words, non-numeric character
 tag_map=defaultdict(lambda :wn.NOUN)
 tag_map['J']=wn.ADJ
 tag_map['V']=wn.VERB
 tag_map['R']=wn.ADV
 for index,entry in enumerate(corpus['Content']):
  final_words=[]
  word_Lemmatized=WordNetLemmatizer()
  for word,tag in pos_tag(entry):
    if word not in vn_stopwords and word.isalpha():
        word_Final=word_Lemmatized.lemmatize(word,tag_map[tag[0]])
        final_words.append(word_Final)
  corpus.loc[index,'text_final']=str(final_words)
pre_process(corpus)
train_X,test_X,train_Y,test_Y=model_selection.train_test_split(corpus['text_final'],corpus['Label'],test_size=0.3,shuffle=True)
Encoder=LabelEncoder()
train_Y=Encoder.fit_transform(train_Y)
test_Y=Encoder.fit_transform(test_Y)
# print(test_Y)

#tf-idf
def tf_idf(train_X):
 tfidf_vect=TfidfVectorizer(max_features=5000)
 tfidf_vect.fit(corpus['text_final'])
 train_X_tfidf=tfidf_vect.transform(train_X)
 return train_X_tfidf
train_X_tfidf=tf_idf(train_X)
test_X_tfidf=tf_idf(test_X)
# print(test_X_tfidf)
# print(test_X_tfidf)
# print(tfidf_vect.vocabulary_)

#svm
SVM=svm.SVC(C=1.0,kernel='linear',degree=3,gamma='auto')
SVM.fit(train_X_tfidf,train_Y)
predictions_SVM=SVM.predict(test_X_tfidf)

#test
test_texts={'Content':['Cho mình hỏi bên mình còn iphone 17 không ạ','làm ăn chán vl.','ve lo khon qua','cam on shop nhieu a']}
test_texts=pd.DataFrame(test_texts)
pre_process(test_texts)
text=tf_idf(test_texts['text_final'])
predict=SVM.predict(text)
# print(predict)
for i in range(len(predict)):
 if predict[i]==0:
  lbl='nontoxic'
 else:
  lbl='toxic'
 print(f'{test_texts['Content'][i]} label: {lbl}')
#print(test_texts)

print('SVM Accuracy Score -> ',accuracy_score(predictions_SVM,test_Y)*100)
