#1st code
def good_day(name, ending, space = "default value"):
    print("Good Day", name)
    print(ending)
    print(space)
    return "done" #return the specified value to any variable that calls the function, in this example it give "done" to a

a = good_day("Harry", "Thanks",) #throws an error if all the required positional arguments are not present(only if the given parameter doesnt have a default value)

#2nd code
def factorial(n):
    if(n==1 or n==0):
      return 1
    return n * factorial(n-1)

n = int(input("Enter a Number: "))
print("The factorial of",n,"is:",factorial(n))

#3rd code
def sum(n):
    if(n==1 or n==0):
      return 1
    return n + sum(n-1)

n = int(input("Enter a Number: "))
print("The sum of",n,"is:",sum(n))

#4th code
def rem(l, word):
    n = []
    for items in l:
        if not(items == word):
            n.append(items.strip(word))
    return n
l = ["Rohan", "Harry", "sohan", "an"]
print(rem(l, "an"))
