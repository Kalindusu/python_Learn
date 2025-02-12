import random
import sys


print('')
playerchoice = input('Enter...\n 1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n ')
player = int(playerchoice)
if player <1 | player > 3:
    sys.exit("You must enter 1,2, or 3")

computerchoise = random.choice("123")

computer = int(computerchoise)
print("")

print ("you chose " + playerchoice + "." )
print ("python chose " + computerchoise + "." )
print("")


if player ==1 and computer == 3:
    print ("You win")
elif player ==2 and computer == 1:
    print ("You win")
elif player ==3 and computer == 2:
    print ("You win")
elif player==computer:
    print ("Tie game")
else:
    print("Python win ")

 