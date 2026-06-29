"""
f = open("text.txt", "w" )
str = "This is how to open and write in a file"
f.write(str)
f.close()
"""

"""
f = open("text.txt")
data = f.read()
print(data)
f.close()
"""

"""
#how to make a while loop to readlines:
f = open("text.txt")
line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()

f.close()
"""

"""
f = open("text.txt", "a" )
str = "This is how to open and write in a file"
f.write(str)
f.close()
"""

"""
#with statement
with open("text.txt", "r") as f:
    text = f.read()

print(text)
"""

"""
diffrent line functions:
f.open()
f.read()
f.write()
f.readlines()
f.close()
"""

"""
f = open("text.txt)
contect = f.read()

if("this" in content):
    print("this word is present in the file)
    
else:    
    print("this word is not present in the file)
"""

"""
import random

def game():
    print("You're playing the game...")
    score = random.randint(1, 62)

    with open("score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        
    print(f"Your score is: {score}")
    if(score > hiscore):
        with(open("score.txt", "w") as f):
            f.write(str(score))

    return score

game()
"""

"""
def generateTable(n):
    table = ""
    for i in range (1, 11):
        table = f"{n} * {i}: {n*i}"

    #used if we want to have the folder created aswell
    import os
     folder = rf"C:\vs coding\python\Practice_Codes\text files\Tables"
    os.makedirs(folder, exist_ok=True)

    with open(rf"C:\vs coding\python\Practice_Codes\text files\Tables\table_{n}.txt", "w") as f:
        f.write(table) 
for i in range (2, 21):
    generateTable(i)
"""
"""
with open(rf"C:\vs coding\python\Practice_Codes\text files\text.txt", "r") as f:
    content = f.read()
    contentNew = content.replace("donkey", "######")

with open(rf"C:\vs coding\python\Practice_Codes\text files\text.txt", "w") as f:
    f.write(contentNew)
"""
