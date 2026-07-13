mark = {} #this is an empty dictionary
marks = {
        "devika": 85,
        "rahul": 92,
        "priya": 78
}

print("Marks of Devika:", marks["devika"])
print(marks.items())  # Print all key-value pairs in the dictionary
print(marks.keys())   # Print all keys in the dictionary
print(marks.values()) # Print all values in the dictionary

#methods to update the dictionary
marks["rahul"] = 95 
marks.update({"priya": 80}) 

#methods to add new key-value pairs to the dictionary
marks["ananya"] = 88
marks.update({"siddharth": 90})
marks.setdefault("neha", 75)  # Add a new key-value pair only if the key doesn't exist
print(marks)

#methods to remove key-value pairs from the dictionary
del marks["devika"]  # Remove the key-value pair with the key "devika
marks.pop("priya")  # Remove the key-value pair with the key "priya"
marks.popitem()  # Remove the last inserted key-value pair from the dictionary
marks.clear()  # Remove all key-value pairs from the dictionary

print(marks.get("rahul"))  # Get the value associated with the key "rahul"
print(marks["rahul"])  # Access the value using square brackets
print(marks.get("rahul2")) #returns None if the key doesn't exist
print(marks["rahul2"]) #throws KeyError if the key doesn't exist

d = {}
name = input("Enter name: ")
lang = input("Enter programming language: ")
d.update({name: lang})  # Add the name and programming language to the dictionary
print("Dictionary:", d)  # Print the dictionary

#sets code
 #1st code
s = {1, 2, 3, 4, 5, 5, 5} #this is a set
e = set() #this is an empty set
s.add(6) #add an element to the set
s.remove(3) #remove an element from the set

#sets dont allow repitition of elements, so if you try to add a duplicate element, it will be ignored  
#sets are unordered collections of unique elements
#sets are mutable, but you cannot change the elements present in the set
#you cannot access elements in a set using indexing or slicing

#operations on sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.union(s2)) #union of two sets
print(s1.intersection(s2)) #intersection of two sets
print(s1.difference(s2)) #difference of two sets
print(s1.subset(s2)) #check if s1 is a subset of s2
print(s1.issuperset(s2)) #check if s1 is a superset of s2
s.add(9) #add an element to the set
s.pop() #removes and returns an random element from the set
s.remove(2) #removes the element 2 from the set
s.remove(10) #throws KeyError if the element is not present in the set
s.clear() #removes all elements from the set

 #2nd code
s4 = set()
e = input("Enter elements for the set (comma-separated): ")
e = e.split(",")  # Split the input string into a list of elements
for item in e:
    s4.add(int(item))  # Add each element to the set
print("Set elements:", s2)
