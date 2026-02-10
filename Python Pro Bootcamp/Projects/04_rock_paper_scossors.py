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

lost = "You lost"
win = "You win"
draw = "Draw"
rock_paper_scissors_numbers =   [0, 1, 2] # [rock, paper, scissors]
rock_paper_scissors =           [rock, paper, scissors]

user_choice = int(input("What doy choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS ").strip())

if user_choice > 2 or user_choice < 0:
    print("Your choice must be 0, 1 or 2 ")
    # print(user_choice)
else:
    computer_choice = random.choice(rock_paper_scissors_numbers)
    print(rock_paper_scissors[user_choice])
    print("COMPUTER CHOICE ")
    print(rock_paper_scissors[computer_choice])
    
    if user_choice == 0:
        if computer_choice == 1:
            print(lost)
        elif computer_choice == 2:
            print(win)
        else:
            print(draw)
    elif user_choice == 1:
        if computer_choice == 0:
            print(win)
        elif computer_choice == 1:
            print(draw)
        elif computer_choice == 2:
            print(lost)
    elif user_choice == 2:
        if computer_choice == 0:
            print(lost)
        elif computer_choice == 1:
            print(win)
        elif computer_choice == 2:
            print(draw)
