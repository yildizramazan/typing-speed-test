import nltk
import random
from nltk.corpus import words
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
BLACK = "#191717"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# nltk.download('words')

#returning 10 random word in english
common_words = random.choices(words.words(), k=150)

words_text = ""
number_of_words_in_one_line = 0

#changing all the words to lowercase
for word in common_words:
    if word[0].isupper():
        index = common_words.index(word)
        common_words[index] = word.lower()
        words_text = words_text + f" {common_words[index]}"
    else:
        words_text = words_text + f" {word}"
    number_of_words_in_one_line += 1
    if number_of_words_in_one_line == 8:
        words_text += "\n"
        number_of_words_in_one_line = 0

print(words_text)
print(common_words)


window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=0, bg=YELLOW)

words = Label(text=words_text, fg=BLACK, bg=YELLOW, font=(FONT_NAME, 15), width=100, height=50)
words.grid(column=0, row=0)





window.mainloop()
