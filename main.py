from tkinter import *
import pandas
import random

BACKGROUND_COLOR="#B1DDC6"
current_card = {}
list_of_words ={}

# ----------------------------------- Generate Random words ----------------------------------- #



try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/ru_en-word-list.csv")
    list_of_words = original_data.to_dict(orient="records")
else:
    list_of_words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list_of_words)
    question_card_canvas.itemconfig(card_title, text="Russian", fill="black")
    question_card_canvas.itemconfig(card_word, text=current_card["Russian"], fill="black")
    question_card_canvas.itemconfig(front_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)

def is_known():
    list_of_words.remove(current_card)
    print(len(list_of_words))
    
    data = pandas.DataFrame(list_of_words)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()
    

def flip_card():
    question_card_canvas.itemconfig(front_image, image=card_back_image)
    question_card_canvas.itemconfig(card_title, text="English", fill="white")
    question_card_canvas.itemconfig(card_word, text=current_card["English"],fill="white" )



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=25, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

question_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

front_image = question_card_canvas.create_image(400, 263, image=card_front_image)

card_title =question_card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = question_card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
question_card_canvas.grid(row=0, column=0, columnspan=2)


wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

next_card()




window.mainloop()