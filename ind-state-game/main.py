#make it better 1. adjust the name coordinates.
import turtle as tu
import pandas as pd

screen = tu.Screen()
screen.title("IND States Game")
screen.bgcolor('black')
image = "states.gif"
screen.addshape(image)
tu.shape(image)

data = pd.read_csv("india.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 36:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/36 States/UT Correct', prompt='Name a state/UT').title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        #new_data.to_csv("states-to-learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = tu.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)