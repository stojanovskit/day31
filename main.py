from tkinter import *
import pandas
import random

word = ""
pos = None
BACKGROUND_COLOR = "#B1DDC6"
try:
    french = pandas.read_csv('data/data.csv').to_dict()

except:
    french = pandas.read_csv('data/french_words.csv').to_dict()


def flipcard():
    global word

    canvas.itemconfig(frn_word, text=word, fill='white')
    canvas.itemconfig(lng_word, text='English', fill='white')
    canvas.itemconfig(card_background, image=back_card)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def wait3():
    window.after(3000, func=flipcard)


wait3()
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_background = canvas.create_image(400, 263, image=card_front_image)
lng_word = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
frn_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'), fill="black")
canvas.grid(row=0, column=0, columnspan=2)
right_image = PhotoImage(file="images/right.png")


def rnd_word():
    global word
    global pos
    pos = random.randint(0, len(french['French']) - 1)
    word = french['French'][pos]
    en_word = french['English'][pos]
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(frn_word, text=word, fill="black")
    canvas.itemconfig(lng_word, text='French', fill="black")
    word = en_word
    wait3()


def rnd_word_remove():
    global word
    global pos
    del french['French'][pos]
    del french['English'][pos]

    df = pandas.DataFrame.from_dict(french)

    df.to_csv("data/data.csv", index=False)
    rnd_word()


btn_right = Button(image=right_image, highlightthickness=0, command=rnd_word)
btn_right.grid(row=1, column=0)
wrong_image = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong_image, highlightthickness=0, command=rnd_word_remove)
btn_wrong.grid(row=1, column=1)
rnd_word()
window.mainloop()
