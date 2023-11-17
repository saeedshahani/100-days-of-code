import random
from replit import clear
from art import logo

def check_answer(user_guess, ran_num, lives):
  if user_guess > ran_num:
    print("Too High.")
    return lives - 1
  elif user_guess < ran_num:
    print("Too Low.")
    return lives - 1
  elif user_guess == ran_num:
    print(f"Correct! The answer is {ran_num}.")
  else:
    print("Error.")
    return lives - lives

def calculate_lives():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10
  else:
    return 5

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  random_number = random.randint(1, 100)
  lives = calculate_lives()
  guess = 0
  while guess != random_number:
    print(f"You have {lives} lives remaining.")
    guess = int(input("Guess a number between 1 and 100: "))
    lives = check_answer(guess, random_number, lives)
    if lives == 0:
      print("No more turns left. You lose.")
      return
    elif guess != random_number:
      print("Guess again")
  play = input("Do you want to play again? Type 'y' or 'n': ")
  if play == "y":
    clear()
    game()

game()