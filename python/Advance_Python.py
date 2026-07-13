# #walrus operator
# if (n := len([1, 2, 3, 4, 5])) >3:
#     print(f"List is too long ({n} elements, expected <=3)") #shortens our code

# #types in python
# from typing import list, tuple, dict, union

# #match case
# def htpps_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Error! Not Found"
#         case 500:
#             return "Server Down"
#         case _:
#             return "unkown Status"

#Dict Merger
# dict1 = {'a':1, 'b':2, 'c':3 }
# dict2 = {'d':4, 'e':5, 'g':6 }
# merged = dict1 | dict2
# print(merged)

# #exception ,this is used for part which are error prone, this helps in protecting the code from crashes
# try:
#     a = int(input("Enter a number: "))
#     print(a)

# except Exception as e:
#     e = "Please enter a valid number"
#     print(e)

# else:
#     print("run") #this block runs if try runs successfully

# finally:
#     print("ran") #this block runs in any case, this is useful in functions and it runs even if the function returns. 
# print("Thank You")
# print(__name__) #this tells us where this code has been run from main(as in its original file) or from a file where it was imported

"""
raise can be used to raise custom exceptions, it crashes programs
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if( b == 0):
    raise ZeroDivisionError ("∞")

else:
    print(f"The division of {a} and {b} is {a/b}")
"""
# #lambda func
# square = lambda x: x*x
# square(6)

table = [str(7*i ) for i in range(1, 11)]

s = "\n" .join(table)
print(s)

 #map, enumerate, filter, reduce(this is imported from fuctools), virtual enviornment, format 