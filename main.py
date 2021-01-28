from replit import clear

from art import logo
print(logo)

more_bidders = "yes"

bidders = {}

while more_bidders == "yes":
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidders[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
  clear()


highest_bid = 0
for bidder in bidders:
  if bidders[bidder] > highest_bid:
    highest_bid = bidders[bidder]
    winner = bidder

print(f"{winner} won the auction for ${highest_bid}.")