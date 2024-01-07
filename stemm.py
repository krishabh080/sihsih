#!/usr/bin/python3
from nltk.stem import PorterStemmer
import sys

def perform_stemming(sentence):
    stemmer = PorterStemmer()
    words = sentence.split()  # Tokenize words using split on spaces
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

if __name__ == "__main__":
    
    user_input = sys.stdin.read().strip()
    #user_input = input("Enter a sentence: ")
    stemmed_result = perform_stemming(user_input)
    
    text=" ".join(stemmed_result)
    print(text)

