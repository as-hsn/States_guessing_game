import turtle
import pandas

screen = turtle.Screen()
FONT = ('Georgia', 14, 'normal')
screen.title("First data retrieve game")
screen.bgpic("blank_states_img.gif")
turtle.hideturtle()
turtle.penup()
read = pandas.read_csv("50_states.csv")
state = read.state.to_list ()


Score = 0
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess next state").title()



    if guess == "Exit" :

        missing = [e_state for e_state in state if e_state not in guessed_states]

        new_data = pandas.DataFrame(missing)
        new_data.to_csv("read_missing_states.csv")

        break

    if guess in state:
            guessed_states.append(guess)
            state_data = (read[read.state == guess])
            turtle.goto(int(state_data.x),
                        int(state_data.y))
            turtle.write(guess, font=FONT)



