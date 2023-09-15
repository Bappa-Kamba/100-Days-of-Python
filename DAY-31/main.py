from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

current_card = {}
known_words = []
# ---------------------------- BUTTON FUNCTIONS ------------------------------- #
def next_card():
    global flip_timer, current_card

    window.after_cancel(flip_timer)  
    current_card = choice(to_learn)  
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_image_front)
    flip_timer = window.after(3000, flip_card)

def is_known():
    known_words.append(current_card)
    to_learn.remove(current_card)
    updated_words = pandas.DataFrame(to_learn)
    updated_words.to_csv(words_to_learn, index=False)
    known_list = pandas.DataFrame(known_words)
    known_list.to_csv(words_learnt, index=False)
    next_card()

def flip_card():
    canvas.itemconfig(canvas_image, image=card_image_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# ---------------------------- FILES ------------------------------- #
card_image_front = PhotoImage(file="DAY-31\\images\\card_front.png")
card_image_back = PhotoImage(file="DAY-31\\images\\card_back.png")
known_image = PhotoImage(file="DAY-31\\images\\right.png")
unknown_image = PhotoImage(file="DAY-31\\images\\wrong.png")
data_file = "DAY-31\\data\\french_words.csv"
words_to_learn = "DAY-31\\data\\words_to_learn.csv"
words_learnt = "DAY-31\\data\\words_learnt.csv"

# ---------------------------- DATA ------------------------------- #
try:
    with open(words_to_learn) as file:
        data = pandas.read_csv(file)
except FileNotFoundError:
    data = pandas.read_csv(data_file)
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

    # ---------------------------- CANVAS ------------------------------- #
canvas = Canvas(width=820, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(410, 265, image=card_image_front)
language_text = canvas.create_text(410, 150, text="Language", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(410, 265, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#     # ---------------------------- BUTTONS ------------------------------- #
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()