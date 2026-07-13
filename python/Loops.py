#1st code
i = 6

while(i>7):
    print(i)
    i += 1

for i in range(100):
    if (i == 34):
        break #Exits the loop when i is equal to 34
    print(i)

for i in range(100):
    if (i == 34):
        continue #Skips the conditioned iteration and continues with the next iteration
    print(i)

for i in range(100):
    pass #The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, 
    #but you avoid getting an error when empty code is not allowed.
#2nd code
b = 2
for i in range(1,11):
    print(f"{b} * {i} = {b*i}") #prints the multiplication table of 2

l = ["Harry", "Sohan", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("Hello " + name) #prints the names that start with S

#3rd code
b = 2
i = 1
while i <= 10:
    print(f"{b} * {i} = {b*i}") #prints the multiplication table of 2
    i += 1        

#4th code
n = int(input("Enter the number: "))
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print(f"The sum of numbers from 1 to {n} is {sum}")

#5th code
n = int(input("Enter the number: "))
product = 1
for i in range (1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

#6th code
n = int(input("Enter the number: "))
for i in range(1, n+1):

    print(" " * (n-i), end ="")
    print("*" * (2*i-1), end = "")
    print() #prints a new line after each row

#7th code
n = int(input("Enter the number: "))
for i in range(1, n+1):

    # print(" " * (n-i), end ="")
    print("*" * (i), end = "")
    print() #prints a new line after each row

#8th code
n = int(input("Enter the number: "))
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * (n), end = "")
    else:
        print("*", end = "")
        print(" " * (n-2), end = "")
        print("*", end = "")
    print() #prints a new line after each row

#9th code
n = int(input("Enter the number: "))
for i in range(10, 0, -1):
    print(f"{n} * {i} = {n*i}") #prints the multiplication table of n in reverse order

    #OR

n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{n} * {11- i} = {n*(11-i)}") #prints the multiplication table of n in reverse order
