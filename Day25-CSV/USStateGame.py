from turtle import Turtle,Screen
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

game=Turtle()
scr= Screen()
scr.title("US States Game")
mapimg="blank_states_img.gif"
scr.addshape(mapimg)
game.shape(mapimg)
write_turtle=Turtle()
write_turtle.penup()
write_turtle.hideturtle()
game_data=pd.read_csv("50_states.csv")
print(game_data)
game_on=True
score=0
total_states= len(game_data)
user_selected_states=[]
while score < total_states:
    user_input= scr.textinput(f"{score}/{total_states} - state quiz","Name a state").title()
    if user_input=="Exit":
        states=game_data.state.to_list()
        print(states)
        remaining_data = [x for x in states if x not in user_selected_states]
        new_df=pd.DataFrame(remaining_data)
        new_df.to_csv("remaining_states.csv")
        break
    elif user_input is not None:
        user_answer_data = game_data[game_data.state  ==user_input]
        if len(user_answer_data)>0:
            x_cor= user_answer_data.x
            y_cor=user_answer_data.y
            #write_turtle.setposition(x_cor.iloc[0],y_cor.iloc[0])
            write_turtle.setposition(x_cor.item(), y_cor.item())
            write_turtle.write(user_answer_data.state.item())
            score+=1
            user_selected_states.append(user_answer_data.state.item())




scr.exitonclick()