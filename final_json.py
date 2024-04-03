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

print("Content-type: application/json")
print()

form = cgi.FieldStorage()
test = form.getvalue("d")
#print("Received input:", test)

load_model = keras.models.load_model("hateabusive.h5")

with open('tokenizer.pickle', 'rb') as handle:
    load_tokenizer = pickle.load(handle)

with open('stopwords.txt', 'r') as file:
    stopwords_list = set(file.read().splitlines())

def clean_text(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopwords_list]
    text = " ".join(text)
    input_bytes = bytes(text, 'utf-8')
    process = subprocess.Popen(["python3", "stemm.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    stdout, _ = process.communicate(input=input_bytes)
    stemming_result = stdout.decode('utf-8')
    text = re.sub('\n', '', stemming_result)
    return text

test = [clean_text(test)]

seq = load_tokenizer.texts_to_sequences(test)
padded = pad_sequences(seq, maxlen=300)
pred = load_model.predict(padded, verbose=0)

prediction_label = int(pred < 0.6)

response = {"input": test[0], "prediction_value": float(pred[0][0]), "prediction_label": prediction_label}
print(json.dumps(response))
