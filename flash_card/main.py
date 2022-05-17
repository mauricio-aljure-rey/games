from tkinter import *
import pandas
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"


def select_next_card():
    global next_word_base_lang, checking
    checking = False
    next_word = data.sample()
    next_word_target_lang = next_word.iat[0, 0]
    next_word_base_lang = next_word.iat[0, 1]
    canvas.itemconfigure(word_text, text=next_word_target_lang)
    canvas.itemconfigure(language_text, text=target_lang)
    canvas.itemconfigure(flash_card, image=card_front_img)
    wrong_button["state"] = "disabled"
    right_button["state"] = "disabled"
    canvas.update()


def turn_over():
    canvas.itemconfigure(flash_card, image=card_back_img)
    canvas.itemconfigure(language_text, text=base_lang)
    canvas.itemconfigure(word_text, text=next_word_base_lang)
    wrong_button["state"] = "normal"
    right_button["state"] = "normal"
    canvas.update()
    # window.after(3000)
    # canvas.itemconfigure(flash_card, image=card_front_img)
    # canvas.itemconfigure(language_text, text=target_lang)


def on_press_right():
    select_next_card()


def on_press_wrong():
    select_next_card()


def on_press_flip():
    global checking
    if not checking:
        checking = True
        turn_over()



#-------- Creating UI ---------#

# Creating window
window = Tk()
window.title = "Pomodoro Technique Manager"
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

# Creating canvas for flash card back and front
canvas_width = 250
canvas_height = 100
canvas = Canvas(width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
flash_card = canvas.create_image(canvas_width/2, canvas_height/2, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=3)

# Creating buttons
wrong_img = Image.open("images/wrong.png").resize((50, 50))
wrong_img = ImageTk.PhotoImage(wrong_img)
right_img = Image.open("images/right.png").resize((50, 50))
right_img = ImageTk.PhotoImage(right_img)
flip_img = Image.open("images/flip.png").resize((50, 50))
flip_img = ImageTk.PhotoImage(flip_img)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=on_press_wrong)
right_button = Button(image=right_img, highlightthickness=0, command=on_press_right)
flip_button = Button(image=flip_img, highlightthickness=0, command=on_press_flip)
wrong_button.grid(row=1, column=2)
right_button.grid(row=1, column=1)
flip_button.grid(row=1, column=0)


# Creating text
language_text = canvas.create_text(canvas_width/2, canvas_height/5, text="", font=("Ariel", 10, "italic"))
word_text = canvas.create_text(canvas_width/2, canvas_height/2, text="", font=("Ariel", 30, "bold"))

# Reading the csv file
data = pandas.read_csv("data/Swedish_Words.csv")
target_lang = data.keys().tolist()[0]
base_lang = data.keys().tolist()[1]
#next_word = data.sample().iat[0, 0]
select_next_card()



window.mainloop()