import art
import random
import game_data
from replit import clear

def compare_ab(selection, value, value2):
  if selection == "a":
    if value > value2:
      return True
    else:
      return False
  if selection == "b":
    if value2 > value:
      return True
    else:
      return False

def select_ab(score, item_two):
  if score == 0:
    return random.choice(game_data.data)
  else:
    return item_two

def format_ab(item):
  name = item["name"]
  description = item["description"]
  country = item["country"]

  return f"{name}, a {description}, from {country}"

def game():
  item_two = {}
  carry = True
  score = 0
  while carry is True:
    print(art.logo)  
    item_one = select_ab(score, item_two)
    value = int(item_one["follower_count"])
    print(f"Compare A: {format_ab(item_one)}")
    print(art.vs)
    item_two = random.choice(game_data.data)
    value2 = int(item_two["follower_count"])
    print(f"Against B: {format_ab(item_two)}")
    selection = input("Who has more followers? Type 'a' or 'b': ").lower()
    carry = compare_ab(selection, value, value2)
    if carry == True:
      score += 1
      input(f"You're right! Current score: {score}")
    else:
      input(f"Sorry that's wrong, final score: {score}")
    clear()
game()