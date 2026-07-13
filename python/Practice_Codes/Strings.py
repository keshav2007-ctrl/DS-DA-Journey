#1st code
a = input("Enter your name: ")
name = input("Enter your name: ")
date = input("Enter the date: ")

print(f"Good Afternoon, {a}!") #prints Good Afternoon, <name>!

print(f'''Dear {name},

        You are selected!
        {date}''') #prints Dear <name>, You are selected! <date>

#2nd code
name = input("Enter your name: ")
date = input("Enter the date: ")

letter = '''Dear <name>,
You are selected!
<date>'''

#replaces <name> and <date> with the values of name and date variables respectively
print(letter.replace("<name>", name).replace("<date>", date)) 

#3rd code
name = "python is an  easy  language   "

print(name.find("   ")) #prints the index of the first occurrence of the substring "    " in the string name

name = "python is an  easy  language   "

print(name.replace("  ", " ")) #prints the string with all occurrences of "  " replaced by " "
print(name) #strings are immutable, so the original string remains unchanged
