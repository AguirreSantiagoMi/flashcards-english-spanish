from tkinter import *
import pandas
import random
BACKGROUND ='#b1ddc6'

#---------------------------------------------------------------- New word ----------------------------------------------------------------#
try:
    words = pandas.read_csv('Data\\words_to_learn.csv')
except FileNotFoundError:
    words = pandas.read_csv('Data\\common_words.csv')
finally:
    words = words.to_dict(orient= 'records')
    current_card = {}

def learned_word():
    global current_card, words
    new_words = [word for word in words if word != current_card]
    pandas.DataFrame(new_words).to_csv('Data\\words_to_learn.csv', index=False)
    
    words = pandas.read_csv('Data\\words_to_learn.csv')
    words = words.to_dict(orient= 'records')
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(words)
    canvas_card.itemconfig(card_title, text='English', fill='black')
    canvas_card.itemconfig(card_word, text=current_card['english'], fill='black')
    canvas_card.itemconfig(front_card, image = card_front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas_card.itemconfig(card_title, text='Spanish', fill='white')
    canvas_card.itemconfig(card_word, text=current_card['spanish'], fill='white')
    canvas_card.itemconfig(front_card, image=card_back_img)

#---------------------------------------------------------------- UI ----------------------------------------------------------------#
window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND)

flip_timer = window.after(3000, func=flip_card)

#IMAGES
card_back_img = PhotoImage(file='images\\card_back.png')
card_front_img = PhotoImage(file='images\\card_front.png')
right_img = PhotoImage(file='images\\right.png')
wrong_img = PhotoImage(file='images\\wrong.png')

#Card
canvas_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND)
front_card = canvas_card.create_image(400, 265, image=card_front_img)
card_title = canvas_card.create_text(400, 150, text='', fill='black', font=('Arial', 40, 'italic'))
card_word = canvas_card.create_text(400, 263, text='', fill='black', font=('Arial', 60, 'bold'))
canvas_card.grid(column=0, row=0, columnspan=2)

#Buttons
wrong_bt = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_bt.grid(column=0, row=1)
right_bt = Button(image=right_img, highlightthickness=0, command=learned_word)
right_bt.grid(column=1, row=1)

next_card()

window.mainloop()