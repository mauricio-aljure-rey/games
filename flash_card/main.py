from tkinter import *
import pandas
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
canvas_width = 700
canvas_height = 500


def select_next_card():
    global checking, next_word
    checking = False
    while True:
        next_word = data.sample()
        if next_word.iloc[0]["num_rights"] < 3:
            break
    canvas.itemconfigure(word_translated_text, state='hidden')
    next_word_target_lang = next_word.iat[0, 0]
    next_word_base_lang = next_word.iat[0, 1]
    canvas.itemconfigure(word_translated_text, text=next_word_base_lang)
    canvas.itemconfigure(word_text, text=next_word_target_lang)
    canvas.itemconfigure(language_text, text=target_lang)
    canvas.itemconfigure(flash_card, image=card_front_img)
    wrong_button["state"] = "disabled"
    right_button["state"] = "disabled"
    flip_button["state"] = "normal"
    canvas.update()


def turn_over():
    canvas.itemconfigure(word_translated_text, state='normal')
    canvas.itemconfigure(flash_card, image=card_back_img)
    canvas.itemconfigure(language_text, text=base_lang)
    wrong_button["state"] = "normal"
    right_button["state"] = "normal"
    flip_button["state"] = "disabled"
    canvas.update()


def on_press_right():
    index = next_word.index.tolist()[0]
    data.at[index, "num_rights"] += 1
    select_next_card()


def on_press_wrong():
    select_next_card()


def on_press_flip():
    global checking
    if not checking:
        checking = True
        turn_over()


def before_closing():
    data.to_csv("data/Swedish_Words.csv", index=False)
    print("Good bye!")
    window.destroy()

#-------- Creating UI ---------#

# Creating window
window = Tk()
window.title = "Flash Cards Learning tool"
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
window.protocol("WM_DELETE_WINDOW", before_closing)

# Creating canvas for flash card back and front

canvas = Canvas(width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
flash_card = canvas.create_image(canvas_width/2, canvas_height/2, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=3)

# Creating buttons
wrong_img = Image.open("images/wrong.png").resize((int(canvas_width/5), int(canvas_width/5)))
wrong_img = ImageTk.PhotoImage(wrong_img)
right_img = Image.open("images/right.png").resize((int(canvas_width/5), int(canvas_width/5)))
right_img = ImageTk.PhotoImage(right_img)
flip_img = Image.open("images/flip.png").resize((int(canvas_width/5), int(canvas_width/5)))
flip_img = ImageTk.PhotoImage(flip_img)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=on_press_wrong)
right_button = Button(image=right_img, highlightthickness=0, command=on_press_right)
flip_button = Button(image=flip_img, highlightthickness=0, command=on_press_flip)
wrong_button.grid(row=1, column=2)
right_button.grid(row=1, column=1)
flip_button.grid(row=1, column=0)


# Creating text
language_text = canvas.create_text(canvas_width/2, canvas_height/5, text="", font=("Ariel", 10, "italic"))
word_text = canvas.create_text(canvas_width/2, canvas_height/2, text="", font=("Ariel", 20, "bold"))
word_translated_text = canvas.create_text(canvas_width/2, canvas_height*3/4, text="whatever", font=("Ariel", 20, "normal"))
# canvas.itemconfigure(word_translated_text, state='hidden')
progress_text = canvas.create_text(canvas_width*8/9, canvas_height*8/9, text="", font=("Ariel", 7))


#-------- Reading the language file ---------#
# Reading the csv file
data = pandas.read_csv("data/Swedish_Words.csv")
target_lang = data.keys().tolist()[0]
base_lang = data.keys().tolist()[1]
try:
    num_rights = data.num_rights()
except Exception as exemption_message:
    print(exemption_message)
    data["num_rights"] = 0

total_cards = len(data)
cards_to_learn = len(data[data["num_rights"] < 3])
canvas.itemconfigure(progress_text, text=f"{cards_to_learn}/{total_cards}")
select_next_card()



window.mainloop()