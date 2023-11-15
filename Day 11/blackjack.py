import random
from replit import clear
from art import logo


def deal_card():
  card = random.choice(cards)
  return card

def ace_replace(cards, old, new):
  return (new if ace == old else ace for ace in cards)

def calculate_score(card_list):
  score = sum(card_list)
  if score == 21 and len(cards) == 2:
    score = 0
  if 11 in card_list and score > 21:
    card_list = ace_replace(card_list,11,1)
    score = sum(card_list)
  return score


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True
input(logo + "\nPress enter to continue")
clear()
while play == True:
  user_win = False
  dealer_win = False
  user_cards = []
  dealer_cards = []
  another_card = "y"
  print(logo)
  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
  while another_card == "y":
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    if user_score == 0:
      user_win = True
      break
    if user_score > 21:
      dealer_win = True
      break
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
      user_cards.append(deal_card())
  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)      
    if dealer_score == 0:
      dealer_win = True
      break
    if dealer_score > 21:
      user_win = True
      break
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
  if user_score > 21:
    print("You lose")
  elif user_win == True and dealer_win == True:
    print("Draw.")
  elif user_win == True and dealer_win == False:
    print("You win")
  elif user_win == False and dealer_win == True:
    print("You lose")
  elif user_win == False and dealer_win == False:
    if user_score > dealer_score:
      print("You win")
    elif user_score == dealer_score:
      print("Draw.")
    else:
      print("You lose")
  else:
    print("Unexpected error")
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    play = True
  else:
    play = False
  clear()
      



#another_card = input("Type 'y' to get another card, type 'n' to pass: ")