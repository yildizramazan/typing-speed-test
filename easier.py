from tkinter import *
import random
import math

PINK = "#e2979c"
RED = "#e7305b"
BLACK = "#191717"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

common_words_list = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with",
    "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her",
    "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up",
    "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time",
    "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could",
    "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think",
    "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even",
    "new", "want", "because", "any", "these", "give", "day", "most", "us", "is", "are", "was", "were",
    "been", "being", "have", "has", "had", "do", "does", "did", "shall", "will", "should", "would",
    "may", "might", "must", "can", "could", "ought", "me", "my", "mine", "we", "our", "ours",
    "us", "your", "yours", "him", "his", "her", "hers", "it", "its", "their", "theirs", "who", "whom",
    "whose", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "being", "been",
    "have", "has", "had", "do", "does", "did", "will", "shall", "would", "should", "can", "could", "may",
    "might", "must", "ought", "need", "dare", "used", "know", "not", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "abundant", "acquire", "admire", "adventure", "affection", "ambitious", "analyze", "appeal", "appetite",
    "astonish", "authentic", "avenue", "awesome", "benevolent", "brilliant", "captivate", "celebration",
    "charming", "coincidence", "compassion", "comprehend", "confident", "conscious", "courageous",
    "curiosity", "delightful", "desire", "determined", "devotion", "discover", "diverse", "effortless",
    "elegant", "embrace", "endeavor", "enthusiasm", "envision", "fascinate", "fortunate", "freedom",
    "grateful", "harmony", "heritage", "humble", "illuminate", "imagination", "impressive", "infinite",
    "inspiration", "integrity", "intuitive", "invigorate", "journey", "joyful", "kindness", "knowledge",
    "laughter", "liberate", "magnificent", "meditate", "miracle", "nurture", "optimistic", "passionate",
    "peaceful", "perceptive", "persevere", "persistence", "prosperous", "radiant", "reflection", "rejoice",
    "resilient", "serenity", "spontaneous", "stimulate", "succeed", "tenacious", "tranquil", "vibrant",
    "wholesome", "wonderful", "adaptable", "advocate", "alluring", "amazing", "balance", "benevolence",
    "breathtaking", "brilliance", "celebrate", "charismatic", "clarity", "comfortable", "companion",
    "confidant", "contentment", "cozy", "cuddle", "dazzling", "dedication", "delicate", "dependable",
    "effervescent", "eloquent", "empathy", "energetic", "entertain", "exhilarating", "exploration",
    "fascination", "flourish", "freethinker", "graceful", "gratitude", "happiness", "harmonious",
    "heartfelt", "heroic", "imagination", "incandescent", "independence", "insightful", "intimate",
    "jubilation", "lighthearted", "magnanimous", "marvelous", "mesmerize", "nourish", "passion",
    "perfection", "perspective", "prosperity", "radiance", "refreshing", "rejuvenate", "resolute",
    "reverence", "sensational", "serendipity", "spirited", "splendid", "stunning", "synchronize",
    "tantalize", "tenderness", "tranquility", "uplifting", "vivacious", "wanderlust", "whimsical",
    "zestful", "adventure", "allure", "awe-inspiring", "balance", "beauty", "blessing", "captivation",
    "charisma", "cheerful", "clarity", "comfort", "compassion", "confidence", "cozy", "daring", "darling",
    "dazzle", "delight", "devotion", "dream", "ecstasy", "effulgent", "eloquence", "embrace", "enchant",
    "endurance", "enjoyment", "enthusiastic", "eternity", "excitement", "exhilaration", "exploration",
    "faith", "fascination", "friendship", "gentle", "glow", "grace", "happiness", "healing", "honesty",
    "hope", "imagination", "integrity", "joy", "kindness", "laughter", "love", "luminous",
    "miracle", "nurturing", "passion", "patience", "peace", "playful", "radiance", "rejoice", "renewal",
    "serenity", "smile", "sparkle", "spirit", "sunshine", "tenderness", "togetherness", "tranquil",
    "treasure", "unity", "vibrancy", "warmth", "whimsy", "wonder", "youthfulness"
    "too", "very"
]

common_words = random.choices(common_words_list, k=150)

unique_words = []

for word in common_words:
    if word not in unique_words:
        unique_words.append(word)

words_text = ""
number_of_words_in_one_line = 0
for word in unique_words:
    words_text = words_text + f" {word}"
    number_of_words_in_one_line += 1
    if number_of_words_in_one_line == 8:
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


words = Label(text=words_text, fg=BLACK, bg="#FFCC70", font=(FONT_NAME, 20), width=75, height=25)
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
