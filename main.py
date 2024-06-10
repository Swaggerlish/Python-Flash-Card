from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

current_word = {}
word_list = []
def next_word():
    global word_list
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    try:
        df = pandas.read_csv("./data/unlearned_word.csv")
        word_list = df.to_dict(orient="records")
    except FileNotFoundError:
        df = pandas.read_csv("./data/french_words.csv")
        word_list = df.to_dict(orient="records")

    current_word = random.choice(word_list)
    canvas.itemconfig(card_word, text=current_word["French"])
    canvas.itemconfig(card_title, text="French")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")

def word_to_learn():
    word_list.remove(current_word)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/unlearned_word.csv", index=False)
    next_word()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title= canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="",font=("ariel", 40, "bold"))
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=word_to_learn)
right_button.grid(row=1, column=0)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=1)

# generate_random_word()








window.mainloop()


