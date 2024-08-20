from art import logo
import os

# Print the logo
print(logo)

# Initialize an empty dictionary to store bids
bids = {}

# Flag to indicate when the bidding has finished
bidding_finished = False

# Function to find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # Iterate over the bidding record to find the highest bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # Print the winner's name and their bid amount
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Loop until the bidding is finished
while not bidding_finished:
    # Ask for the bidder's name and bid amount
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # Store the bid in the dictionary
    bids[name] = price

    # Validate input for continuing bidders
    while True:
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if should_continue == "no":
            bidding_finished = True
            find_highest_bidder(bids)
            break
        elif should_continue == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


