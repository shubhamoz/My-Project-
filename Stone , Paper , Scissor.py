import random

play = ["stone", "paper", "scissor"]

user = input("Enter stone, paper or scissor: ").lower()

computer = random.choice(play)

print("Computer chose:", computer)

if user == computer:
    print("Draw!")

elif (
    (user == "stone" and computer == "scissor") or
    (user == "paper" and computer == "stone") or
    (user == "scissor" and computer == "paper")
):
    print("You Win!")

else:
    print("Computer Wins!")
    