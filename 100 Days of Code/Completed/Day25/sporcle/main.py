import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.speed("fastest")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_list = []
while len(correct_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_list)}/50 States Correct", prompt="What's another state's "
                                                                                           "name?").title()
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        writer.home()
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(f"{answer_state}", align="center", font=("Courier", 6, "normal"))
        # writer.write(state_data.state.item())  # Would also work
        correct_list.append(answer_state)
    elif answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if correct_list not in all_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")  # Generate csv file with non-guessed states
        break


# def get_mouse_click_coor(x, y):  # Determine x, y coordinates on map
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()  # Keeps screen open, alternative to exitonclick
