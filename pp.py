#!/usr/bin/python3
import cgi
import joblib
import pickle
import re
import string
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import keras
from keras.utils import pad_sequences
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Add this line to import the required NLTK resources
import nltk
#nltk.download('stopwords')

# ... (rest of the imports)

#form = cgi.FieldStorage()
#test = form.getvalue("d")
test = input("Enter a string: ")
load_model = keras.models.load_model("./hate&abusive_model.h5")
with open('tokenizer.pickle', 'rb') as handle:
    load_tokenizer = pickle.load(handle)

stopword = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
  #  print(text)
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
   # print(text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
test=[clean_text(test)]
#print(test)
seq = load_tokenizer.texts_to_sequences(test)
padded = pad_sequences(seq, maxlen=300)
print("check 1 ")
#print(seq)
pred = load_model.predict(padded)

print("check 1 ")
print("pred", pred)
if pred<0.6:
    print("no hate")
else:
    print("hate and abusive")

