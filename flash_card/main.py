from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#-------- Press right button ------#

def on_press_right():
    canvas.itemconfig(flash_card, image=card_front_img)


def on_press_wrong():
    canvas.itemconfig(flash_card, image=card_back_img)



#-------- Creating UI ---------#

# Creating window
window = Tk()
window.title = "Pomodoro Technique Manager"
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating canvas for flash card back and front
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
flash_card = canvas.create_image(400, 270, image=card_front_img)
canvas.itemconfig(flash_card, image=card_back_img)
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=on_press_wrong)
right_button = Button(image=right_img, highlightthickness=0, command=on_press_right)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)



window.mainloop()