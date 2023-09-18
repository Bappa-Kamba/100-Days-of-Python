from turtle import Screen, Turtle
import pandas
import os

FONT = ("Courier", 8, "normal")
ALIGN = "center"

image_filename = os.path.abspath('DAY-25/U.S. States Game/blank_states_img.gif')
data_filename = os.path.abspath('DAY-25/U.S. States Game/50_states.csv')
export_filename = os.path.abspath('DAY-25/U.S. States Game/states_to_learn.csv')

screen = Screen()
screen.setup(width=750, height=550)
screen.addshape(image_filename)
screen.title("U.S. States Games")
turtle = Turtle(shape=(image_filename))
writer = Turtle()
writer.penup()
writer.hideturtle()


data = pandas.read_csv(data_filename)
guessed_states = []
states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 correct states",
                                    "What is another state?")
    if answer_state.title() == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv(export_filename)
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        x_cor = int(state.x.iloc[0])
        y_cor = int(state.y.iloc[0])
        writer.goto(x_cor, y_cor)
        writer.write(answer_state, align=ALIGN, font=FONT)

