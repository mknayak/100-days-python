import game_data
import art
import random
#list of dictionaries, read into variable
GAME_DICT= game_data.data

def show_options(optA,optB):
    print(f"Compare A: {optA['name']}, a {optA['description']}, from {optA['country']}.")
    print(art.vs)
    print(f"Against B: {optB['name']}, a {optB['description']}, from {optB['country']}.")

#find random item from list. A
# find another random item from list: B
# compare function (a,b)
    # ask user to choose A or B
    # check followers count and if user choice has more followers, they win
    # compare followers count
def choose_options(user_select, user_score):
    com_select= random.choice(GAME_DICT)
    show_options(user_select,com_select)
    user_option= input("Who has more followers? Type 'A' or 'B' :")
    continue_game=False
    if user_option=='A' and user_select['follower_count'] > com_select['follower_count']:
        continue_game=True
    elif user_option == 'B' and user_select['follower_count'] < com_select['follower_count']:
        continue_game=True
        user_select=com_select

    if continue_game:
        user_score+=1
        print(f"You're right! Current score: {user_score}")
        choose_options(user_select,user_score)
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")


#print logo
def play_game():
    print(art.logo)
    user_select= random.choice(GAME_DICT)
    choose_options(user_select,0)





# store user score in a variable


play_game()