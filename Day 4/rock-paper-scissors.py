import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors]

compchoice = options[random.randint(0,2)]

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(choice)

print(f"Computer chose:\n {compchoice}")

if choice == 0:
  choice = rock
elif choice == 1:
  choice = paper
elif choice == 2:
  choice = scissors
else:
  print("error")

print(f"You chose:\n {choice}")

if choice == rock:
  if compchoice == scissors:
    print("You win.")
  elif choice == compchoice:
    print("Draw.")
  else:
    print("You lose.")
elif choice == paper:
  if compchoice == rock:
    print("You win.")
  elif choice == compchoice:
    print("Draw.")
  else:
    print("You lose.")
elif choice == scissors:
  if compchoice == paper:
    print("You win.")
  elif choice == compchoice:
    print("Draw.")
  else:
    print("You lose.")