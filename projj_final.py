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
import subprocess
from keras.utils import pad_sequences

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
test = form.getvalue("d")
print("Received input:", test)
load_model = keras.models.load_model("hate&abusive_model.h5")
with open('tokenizer.pickle', 'rb') as handle:
    load_tokenizer = pickle.load(handle)
with open('stopwords.txt', 'r') as file:
    stopwords_list = set(file.read().splitlines())

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
    #print("check1")
    
    print("<br>")
    print("<br>")
    print(text)
    print("<br>")
    # Call the stemming script and capture the output
    input_bytes = bytes(text, 'utf-8')  # Convert input to bytes
    process = subprocess.Popen(["python3", "stemm.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=input_bytes)

        # Decode the output
    stemming_result = stdout.decode('utf-8')
    #print(stemming_result)
    text= re.sub('\n', '', stemming_result)
    #print("check2")
    #print(type(text))
    print(text)
    return text
test=[clean_text(test)]
#print("check3")

print("<br>")

print("<br>")
print(test)


#print("check4")

print("<br>")

print(type(test))
print("<br>")

seq = load_tokenizer.texts_to_sequences(test)
padded = pad_sequences(seq, maxlen=300)
#print(seq)
pred = load_model.predict(padded)

print("<br>")
print("<br>")

print("pred", pred)
print("<br>")
if pred<0.6:
    print("no hate")
else:
    print("hate and abusive")

