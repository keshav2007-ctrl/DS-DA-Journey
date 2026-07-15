"""
1 is snake
-1 is water
0 is gun
"""
import random
random_number = random.choice([-1, 0, 1])
computer = random_number

youstr = input("Enter you choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1 : "snake", -1 : "water", 0 : "gun"}
you = youdict[youstr]
print(f"you choose {reversedict[you]}\nCoumputer choose {reversedict[computer]}")

if(computer == you):
    print("Its a draw!")

else:
"""    if(computer == 1 and you == 0):
        print("you win!")

    elif(computer == 1 and you == -1):
        print("you lose!")

    elif(computer == -1 and you == 1):
        print("you win!")
        
    elif(computer == -1 and you == 0):
        print("you Lose!")

    elif(computer == 0 and you == -1):
        print("you win!")

    elif(computer == 0 and you == 1):
        print("you Lose!")
    
    else:
        print("Something went wrong!")
"""
    if((computer - you) == 1 or (computer - you) == -2):
        print("you win!")

    else:
        print("you Lose!")