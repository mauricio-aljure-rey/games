# Game taken from online course

import pandas
import turtle


# Setting up the screen
screen = turtle.Screen()
background_img = "blank_states_img.gif"
screen.addshape(background_img)
turtle.shape(background_img)

# Reading the States name and location with pandas
states = pandas.read_csv("50_states.csv")

# Initializing the turtles to write on the map
names_on_map = turtle.Turtle()
names_on_map.penup()
names_on_map.hideturtle()


# Running the game
counter = 0
while counter < 50:
    # Asking user for State name
    state_written = screen.textinput(f"{counter}/50 States found", "Please write the name of a State")
    state_written = state_written.capitalize()

    if state_written == "Exit":
        break

    # Checking if written name is within the list of states
    state_info = states[states["state"] == state_written]
    if not state_info.empty:  # User entered correctly
        x = int(state_info.x)
        y = int(state_info.y)
        names_on_map.goto(x, y)
        names_on_map.write(state_written)
        counter += 1
