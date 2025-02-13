# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
bidder_data={}

more_bidders_exists=True
print(logo)
while more_bidders_exists:
    user=input("What is your name?:")
    bid= int(input("What is your bid?:"))
    if user in bidder_data.keys():
        print("User already exists")
    else:
        bidder_data[user]=bid

    decision=input("Are there more bidders?('yes','no'):")
    if decision=="yes":
        more_bidders_exists=True
        print("\n"*20)
    else:
        more_bidders_exists=False

highest_bidder=""
highest_bidding_amount=0

for bidder in bidder_data:
    if bidder_data[bidder] > highest_bidding_amount:
        highest_bidder=bidder
        highest_bidding_amount=bidder_data[bidder]

print(f"Highest bidder :{highest_bidder} with Bidding amount:{highest_bidding_amount}")

