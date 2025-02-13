from platform import android_ver

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0
#TODO: 1. Get User Option
#TODO: 2. Turn off by entering "off" to the prompt
#TODO: 3. Print report

def show_report():
    print(f"Water:{resources['water']}")
    print(f"Milk:{resources['milk']}")
    print(f"Coffee:{resources['coffee']}")
    print(f"Money: ${money}")
def prepare_drink(option):
    res=MENU[option]['ingredients']
    global resources
    global money
    if 'water' in res.keys():
        resources['water'] -= res['water']
    if 'milk' in res.keys():
        resources['milk'] -= res['milk']
    if 'coffee' in res.keys():
        resources['coffee'] -= res['coffee']
    money += MENU[option]['cost']
    print(f"Here is your {option}. Enjoy!")

def exchange_money(option):
    res_option = MENU[option]
    print(f"Cost of a {option}:{res_option['cost']}")

    quarters=int(input("Quarters (0.25) :"))
    dimes=int(input("Dimes (0.10) :"))
    nickles=int(input("Nickles (0.05) :"))
    pennies=int(input("Pennies (0.01) :"))
    total=(quarters * 0.25) + (dimes * 0.10)+(nickles*0.05)+(pennies*0.01)
    if total < res_option['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if total > res_option['cost']:
        balance = round( total - res_option['cost'],2)
        print(f"Here is {balance} dollars in change.")
    return True
def check_resource(req_resource,option):
    if option not in req_resource.keys():
        return True
    else:
        return resources[option]>= req_resource[option]

def confirm_option(option):
    req_res= MENU[option]['ingredients']
    if check_resource(req_res,'water'):
        if check_resource(req_res,'milk'):
            if check_resource(req_res,'coffee') :
                return True
            print("Sorry there is not enough Coffee")
        print("Sorry there is not enough Milk")
    print("Sorry there is not enough Water")
    return False

def show_options():
    user_option = input("What would you like? (espresso/latte/cappuccino):")
    if user_option=='off':
        return
    elif user_option=='report':
        show_report()
    else:
        if confirm_option(user_option):
            if exchange_money(user_option):
                prepare_drink(user_option)

    show_options()

show_options()