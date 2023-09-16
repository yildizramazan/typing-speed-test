import nltk
import random
from nltk.corpus import words
from tkinter import *
import math


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

unique_words = []
for word in common_words:
    if word not in unique_words:
        unique_words.append(word)

words_text = ""
number_of_words_in_one_line = 0
for word in unique_words:
    words_text = words_text + f" {word}"
    number_of_words_in_one_line += 1
    if number_of_words_in_one_line == 7:
        words_text += "\n"
        number_of_words_in_one_line = 0


correct_words = 0
def calculating_wpm():
    global correct_words
    correct_words = 0
    user_typed_words = text_entry.get().split(" ")
    for user_word in user_typed_words:
        for common_word in unique_words:
            if user_word == common_word:
                correct_words += 1



def start_timer():
    text_entry.config(state="normal")
    start_button.config(state="disabled")
    count_down(60)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"0{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        calculating_wpm()
        score = Label(text=f"Your score is: \n{math.ceil(correct_words / 60)} word/min", font=(FONT_NAME, 25, "bold"), fg=RED, bg=YELLOW)
        score.grid(row=3, column=1)


window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=10, bg=YELLOW)

title = Label(text="Typing Speed Test", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=BLACK)
title.grid(row=0, column=0, columnspan=2, pady=20)


words = Label(text=words_text, fg=BLACK, bg="#FFCC70", font=(FONT_NAME, 18), width=90, height=25)
words.grid(row=1, column=0)

text_entry = Entry(bg="#8ECDDD", fg=BLACK, font=(FONT_NAME, 15), state="disabled")
text_entry.grid(row=2, column=0, pady=20)
text_entry.config(width=36)

start_button = Button(command=start_timer, text="Start", width=15, height=2, font=(FONT_NAME, 20, "bold"), fg="#22668D")
start_button.grid(row=3, column=0, pady=10)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(60, 65, text="00:00", fill=BLACK, font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1, padx=75, pady=0)


window.mainloop()