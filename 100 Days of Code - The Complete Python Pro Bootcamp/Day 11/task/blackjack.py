import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer1_pc = []
dealer2_user = []
win_score = 21
def initialize_game():
    user_deal(2)
    pc_deal(2)

def user_deal(no_of_cards):
    for _ in range(1, no_of_cards+1):
        user_card = random.choice(cards)
        if user_card==11 and sum(dealer2_user)>21:
            user_card=1
        dealer2_user.append(user_card)

def pc_deal(no_of_cards):
    if no_of_cards==-1:
        user_total=sum(dealer2_user)
        pc_total=sum(dealer1_pc)
        while pc_total<user_total and pc_total<=17:
            pc_deal(1)
            pc_total=sum(dealer1_pc)
    else:
        for _ in range(1, no_of_cards + 1):
            dealer1_pc.append(random.choice(cards))

def print_result(dealer1,dealer2):
    your_total = sum(dealer2)
    pc_deal(-1)
    pc_total=sum(dealer1)
    print(f'Your final hand:{list(dealer2)}, final score:{your_total}')
    print(f'Computer\'s final hand:{list(dealer1)}, final score:{pc_total}')
    if your_total > win_score:
        if pc_total> win_score:
            print("Draw :)")
        else:
            print("Computer Win")
    elif pc_total > win_score:
        print("You Win")
    else:
        if your_total == pc_total:
            print("Draw :)")
        elif your_total> pc_total and your_total<=win_score:
            print("You Win")
        else:
            print("Computer Win")

def print_game(dealer1,dealer2):
    your_total = sum(dealer2)
    print(f'Your final hand:{list(dealer2)}, Current score:{your_total}')
    print(f'Computer\'s first card:{dealer1[0]}')
    if your_total< win_score:
        return True
    return False

def blackjack():
    decision= input("Do you want to play a game of Blackjack? Type 'Y' or 'N':").lower()
    if decision=="n":
        print_result(dealer1_pc,dealer2_user)
    else:
        print(art.logo)
        initialize_game()
        continue_game=True
        while continue_game:
            if print_game(dealer1_pc, dealer2_user):
                continue_play=input("Type 'y' to play another card, type 'n' to pass:").lower()
                if continue_play=="y":
                    user_deal(1)
                else:
                    continue_game=False
            else:
                continue_game = False

        print_result(dealer1_pc, dealer2_user)

blackjack()