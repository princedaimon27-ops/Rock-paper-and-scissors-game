Rock, Paper, Scissors Game
Description

This is a simple Rock, Paper, Scissors game built using Python.
The game allows a user to play against the computer.

The computer randomly chooses between:

Rock
Paper
Scissors

The player enters their choice, and the program determines the winner.

Features
User vs Computer gameplay
Random computer choices
Win, lose, and tie detection
Simple and beginner-friendly Python project
Technologies Used
Python
Random Module
Code Overview
# a rock,paper,scissors game between a computer and a user

import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

golden = input("Enter rock, paper, or scissors: ")

print("Computer chose:", computer)

if golden == computer:
    print("It's a tie")

elif golden == "rock" and computer == "scissors":
    print("You win")

elif golden == "paper" and computer == "rock":
    print("You win")

elif golden == "scissors" and computer == "paper":
    print("You win")

else:
    print("You lose")
How the Program Works
The program imports the random module.
The computer randomly selects:
rock
paper
scissors
The user enters their choice.
The game compares both choices.
The result is displayed:
Win
Lose
Tie
Game Rules
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
Example Output
Enter rock, paper, or scissors: rock
Computer chose: scissors
You win
Future Improvements
Add score tracking
Add multiple rounds
Add input validation
Create a graphical interface
