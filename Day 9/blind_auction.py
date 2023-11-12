from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bidders = {}
others = "yes"

while others == "yes":
  #ask for name input
  name = input("Enter your name.\n")
  #ask for bid price
  bid = input("Enter your bid.\n$")
  # add name and bid into a dictionary as the key and value
  bidders[name] = int(bid)
  #ask if there are other users whant to bid
  others = input("Type 'yes' if there are other users, 'no' if not.\n")
  clear()

#yes, clear the screen, ask for name etc
#no, find the highest bid in the dictionary and declare the winner
winner = max(bidders, key=bidders.get)
winning_bid = bidders[winner]
print(f"{winner} has won at a bid of {winning_bid}!")
