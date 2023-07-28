from tkinter import *
import pandas as pd
from random import randint
BACKGROUND_COLOR = "#B1DDC6"
current_card = ""
try:
    datadf = pd.read_csv("Flash Card App\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Flash Card App\data\german_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = datadf.to_dict(orient="records")



def generate_random_word():
    global current_card, flip_timer, key
    window.after_cancel(flip_timer)
    key = randint(0,300)
    current_card = data[key]['English']
    TITLE = "German"
    WORD = data[key]['German']
    canvas.itemconfig(can_back,image=card_front_img)
    canvas.itemconfig(can_word,text=WORD,fill="black")
    canvas.itemconfig(can_title,text=TITLE,fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(can_title, text="English",fill="white")
    canvas.itemconfig(can_word,text=current_card,fill="white")
    canvas.itemconfig(can_back,image=card_back_img)

def is_known():
    data.pop(key)
    words_to_learn = pd.DataFrame(data)
    words_to_learn.to_csv("Flash Card App\data\words_to_learn.csv",index=False)
    generate_random_word()
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="Flash Card App\images\card_front.png")
card_back_img = PhotoImage(file="Flash Card App\images\card_back.png")
can_back = canvas.create_image(400,263,image=card_front_img)
can_title = canvas.create_text(390,150,text="",font=('Ariel',40,"italic"))
can_word = canvas.create_text(390,263,text="",font=("ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
# ------Buttons -------
x_image = PhotoImage(file="Flash Card App\images\wrong.png")
x_button = Button(image=x_image,highlightthickness=0,command=generate_random_word)
x_button.grid(row=1,column=0,padx=50,pady=50)
y_image = PhotoImage(file="Flash Card App\images\\right.png")
y_button = Button(image=y_image,highlightthickness=0,command=is_known)
y_button.grid(row=1,column=1,padx=50,pady=50)
generate_random_word()
window.mainloop()