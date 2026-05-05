# a rock,paper,scissors game between a computer and a user
import random
choices =["rock","paper","scissors"]
computer = random.choice(choices)
golden = input("enter rock,paper,scissors :")
print("computer chose :", computer)
if golden == computer :
    print("its a tie")
elif golden == "rock" and  computer == "scissors":
        print("you win")
 
elif golden == "paper" and computer == "rock":
    print("you win")
   
elif golden == "scissors" and computer == "paper":
   print("you won")
else:
    print("you lose")