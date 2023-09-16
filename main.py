import tkinter as tk
import nltk
import random
from nltk.corpus import words, brown
import nltk
from nltk.corpus import words

# nltk.download('words')

#returning 10 random word in english
common_words = random.choices(words.words(), k=10)


#changing all the words to lowercase
for word in common_words:
    if word[0].isupper():
        index = common_words.index(word)
        common_words[index] = word.lower()

print(common_words)
