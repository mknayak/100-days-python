from tkinter import *
import pandas as pd
import random

import os.path
BACKGROUND_COLOR = "#B1DDC0"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
ORIGINAL_FILE="./data/french_words.csv"
WORDS_TO_LEARN_FILE="./data/words_to_learn.csv"

word_dict= []
cur_word= {}

#----------- Functions ----------#
def initialize():
    global word_dict
    if os.path.isfile(WORDS_TO_LEARN_FILE):
        word_dict = pd.read_csv(WORDS_TO_LEARN_FILE).to_dict(orient="records")
    else:
        word_dict = pd.read_csv(ORIGINAL_FILE).to_dict(orient="records")

def btn_yes_click():
    index = word_dict.remove(cur_word)
    show_new_word()
    save_files()


def save_files():
    data_to_save=pd.DataFrame(word_dict)
    data_to_save.to_csv(WORDS_TO_LEARN_FILE, index=False)

def show_new_word():
   global cur_word,flip_timer
   window.after_cancel(flip_timer)
   if len(word_dict)>0:
       cur_word = random.choice(word_dict)
       f_word=cur_word["French"]
       canvas.itemconfig(title_text,text="French")
       canvas.itemconfig(word_text, text=f_word)
       canvas.itemconfig(canvas_img, image=bg_img_front)
       flip_timer = window.after(3000, func=show_eng_word)
   else:
       end_game()

def show_eng_word():
   global cur_word
   e_word = cur_word["English"]
   canvas.itemconfig(title_text, text="English")
   canvas.itemconfig(word_text, text=e_word)
   canvas.itemconfig(canvas_img, image=bg_img_back)

def end_game():
    canvas.itemconfig(title_text, text="No more words")
    canvas.itemconfig(word_text, text="")

#------------ Set up UI -------#
window = Tk()
window.title("Flashy")
window.configure( padx=50,pady=50, bg=BACKGROUND_COLOR)

canvas=Canvas(window,width=800,height=526,background=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
bg_img_front=PhotoImage(file="./images/card_front.png")
bg_img_back= PhotoImage(file="./images/card_back.png")
canvas_img=canvas.create_image(400,263, image=bg_img_front)
title_text = canvas.create_text(400,150,text="French",font=TITLE_FONT)
word_text=canvas.create_text(400,263,text="French",font=WORD_FONT)

yes_img=PhotoImage(file="./images/right.png")
no_img=PhotoImage(file="./images/wrong.png")
btn_yes=Button(window,image=yes_img,highlightthickness=0, command=btn_yes_click)
btn_no=Button(window,image=no_img,highlightthickness=0, command=show_new_word)


canvas.grid(row=0,column=0,columnspan=2)
btn_yes.grid(row=1,column=1)
btn_no.grid(row=1,column=0)

initialize()
flip_timer = window.after(3000, show_eng_word)
show_new_word()

window.mainloop()

