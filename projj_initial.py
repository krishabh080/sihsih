#!/usr/bin/python3
import cgi
import joblib
import pickle
import re
import string
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import sys
import json
import keras
from keras.utils import pad_sequences
#from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
#import tensorflow as tf

#print("initial check")

print("Content-type: text/html")
print()

# Add this line to import the required NLTK resources
#import nltk
#nltk.download('stopwords')

# ... (rest of the imports)

form = cgi.FieldStorage()
test = form.getvalue("d")
print("Received input:", test)
load_model = keras.models.load_model("hate&abusive_model.h5")
with open('tokenizer.pickle', 'rb') as handle:
    load_tokenizer = pickle.load(handle)
with open('stopwords.txt', 'r') as file:
    stopwords_list = set(file.read().splitlines())
#stopword = set(stopwords.words('english'))
#stemmer = PorterStemmer()
#print("check 2")
def clean_text(text):
    #print(text)
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    #print(text)
    text = [word for word in text.split(' ') if word not in stopwords_list]
    text=" ".join(text)
    #text = [stemmer.stem(word) for word in text.split(' ')]
    #text=" ".join(text)
    return text
test=[clean_text(test)]
#print("check3")
print(test)
print("<br>")
seq = load_tokenizer.texts_to_sequences(test)
padded = pad_sequences(seq, maxlen=300)
#print(seq)
#tf.get_logger().setLevel('ERROR')

#sys.stdout = open(os.devnull, 'w')
#sys.stderr = open(os.devnull, 'w')
pred = load_model.predict(padded)
#pred=0.11
#sys.stdout = sys.__stdout__
#sys.stderr = sys.__stderr__
print("pred", pred)
print("<br>")
if pred<0.6:
    print("no hate")
else:
    print("hate and abusive")

