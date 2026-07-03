#1st code
a = int(input("Enter your age: "))

if 0< a < 18:
    print("You are a minor.")

elif a == 0:
    print("Really?")

else:
    print("You are an adult.")

#2nd code
a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))

if a1 > a2 and a1 > a3 and a1 > a4:
    print("The largest number is:", a1)

elif a2 > a1 and a2 > a3 and a2 > a4: 
    print("The largest number is:", a2)

elif a3 > a1 and a3 > a2 and a3 > a4:
    print("The largest number is:", a3)

else:
    print("The largest number is:", a4)

#3rd code
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

if (m1*100/100) >= 33:
    print("You have passed the 1st subject")
if (m2*100/100) >= 33:
    print("You have passed the 2nd subject")
if (m3*100/100) >= 33:
    print("You have passed the 3rd subject")

total_percentage = (m1+m2+m3 / 300) * 100
if total_percentage >= 40:
    print("You have passed the exam.", total_percentage)
else:
    print("You have failed the exam.", total_percentage)

#4th code
user = input("Enter your username: ")

if len(user) < 10:
    print("Username must be at least 10 characters long.")
else:
    print("Username is valid.")

#5th code
post = input("Enter your post: ")
word = input("Enter the word to search: ")

if (word.lower() in post.lower()):
    print("The word is present in the post.")
else:
    print("The word is not present in the post.")

    
