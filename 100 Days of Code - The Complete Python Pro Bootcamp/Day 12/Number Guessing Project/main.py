import random

EASY_ATTEMPT=10
HARD_ATTEMPT=5
max_attempts=0

def set_game_level():
    global max_attempts
    option = input(f"Choose option 'Easy' or 'Hard' :").lower()
    if option=="easy":
        max_attempts=EASY_ATTEMPT
    else:
        max_attempts=HARD_ATTEMPT

def process_result(number_to_find,attempt):
    print(f"You have {attempt} attempts to Guess the Number.")
    guess_number = int(input("Make a guess:"))

    if guess_number == number_to_find:
        return True
    elif guess_number < number_to_find:
        print("Too Low")
    else:
        print("Too High")
    return False

def number_guess_game():
    print("Welcome to Nuber guessing Game")
    print("I am thinking of a number between 1 to 100")
    number_to_find= random.choice(range(1,100))
    set_game_level()

    attempt=max_attempts
    number_found=False

    while attempt> 0 and not number_found:
        number_found=process_result(number_to_find,attempt)
        attempt-=1

    if number_found:
        print(f"You got it. The number was {number_to_find}")
    else:
        print(f"You loose. Try again. The number was {number_to_find}")


number_guess_game()

