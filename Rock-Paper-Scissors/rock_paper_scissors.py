# Rock Paper Scissors Game

# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If the same, it's a tie

# Write a program so that you can play rock, paper, scissors with the computer.
# The program should randomly select rock, paper, or scissors for the computer.
# Get the user to input either rock, paper, or scissors.
# The program should then compare the user's choice to the computer's choice
# Let the programm print out the result stating who won.

# Advanced
# Let the user type in again and again until they type in something to quit
# Keep track how of many times each player won

import random

print("Welcome to Rock, Paper, Scissors!\n")

while True:
  user_pick = input("Enter a choice (rock, paper, scissors): ").lower()
  possible_picks = ["rock", "paper", "scissors"]
  computer_pick = random.choice(possible_picks)

  if user_pick == computer_pick:
      print(f"Both players selected {user_pick} - It's a tie!")
  elif user_pick == "rock":
      if computer_pick == "scissors":
          print("Rock smashes scissors - You win! 🏆")
      else:
          print("Paper beats rock - You lose. 😭")
  elif user_pick == "paper":
      if computer_pick == "rock":
          print("Paper covers rock - You win! 🏆")
      else:
          print("Scissors cuts paper! You lose. 😭")
  elif user_pick == "scissors":
      if computer_pick == "paper":
          print("Scissors cuts paper - You win! 🏆")
      else:
          print("Rock smashes scissors! You lose. 😭")
  else:
    print("Invalid input!")
  
  repeat = input("\nPlay again? (y/n)").lower()

  if repeat == 'n':
    break

print("\nThanks for playing 🎉")

# Other possible Solution for the if-else condition:
# if user_pick == computer_pick:
#     print("It's a tie!")
# elif user_pick == "rock" and computer_pick == "scissors":
#     print("You win!")
# elif user_pick == "rock" and computer_pick == "paper":
#     print("You lose!")
# elif user_pick == "paper" and computer_pick == "rock":
#     print("You win!")
# elif user_pick == "paper" and computer_pick == "scissors":
#     print("You lose!")
# elif user_pick == "scissors" and computer_pick == "paper":
#     print("You win!")
# elif user_pick == "scissors" and computer_pick == "rock":
#     print("You lose!")
# else:
#     print("Invalid input!")
#     print("Please try again!")