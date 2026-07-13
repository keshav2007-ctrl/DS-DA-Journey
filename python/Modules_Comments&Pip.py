import pyjokes
print("Hello, World!")

jokes = pyjokes.get_jokes()
joke = pyjokes.get_joke()
print(jokes[0]) # Print the first joke from the list of jokes
print(joke) #prints all jokes in the list randomly
"""
this is a multi-line comment
when you want to write a comment that spans multiple lines, you can use triple quotes either {'*3 or "*3} 
to enclose the comment text. This is useful for providing detailed explanations or documentation within your code.
"""
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, World!")
engine.runAndWait()

import os

#specify the directory path where the files are located
directory_path = "/"

#list all the files in the specified directory
files = os.listdir(directory_path)

#iterate through the list of files and print their names
for file in files:
    print(file)
