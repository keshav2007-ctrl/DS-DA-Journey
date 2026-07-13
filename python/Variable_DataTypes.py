#a is integer
a = 1
#b is float
b = 2.22
#c is string
c = "string"
#d is boolean
d = True
#e is NoneType
e = None 
"""
A variable name can contain letters, numbers, and underscores.
A variable name can only start with a letter or an underscore.
No whitespace are allowed in variable names.

Types of operators in Python:
1. Arithmetic Operators: +, -, *, /, %, **, //
2. Comparison Operators: ==, !=, >, <, >=, <= (they only return boolean values True or False)
3. Logical Operators: and, or, not
4. Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
5. Bitwise Operators: &, |, ^, ~, <<, >>
6. Membership Operators: in, not in
7. Identity Operators: is, is not
8. Ternary Operator: value_if_true if condition else value_if_false
9. Walrus Operator: := (used to assign values to variables as part of an expression)
10. Operator Precedence: The order in which operators are evaluated in an expression.
11. Operator Associativity: The order in which operators of the same precedence are evaluated in an expression.
12 . Operator Overloading: The ability to define the behavior of operators for user-defined classes.
13. Operator Chaining: The ability to chain multiple operators together in a single expression.
14. Operator Short-Circuiting: The ability of certain operators to skip the evaluation of the second operand if the first operand is sufficient to determine the result.
15. Operator Precedence Table: A table that lists the precedence and associativity of all operators in Python
16. Operator Precedence and Associativity Rules: The rules that govern the order in which operators are evaluated in an expression, based on their precedence and associativity.
"""
#prints the type of variable.
a = 3
b = float(a) #converts a to float(given that it is possible to convert it to float)
t = type(b)

print(t) 

str(31) #converts 31 to string
int("31") #converts "31" to integer
float(31) #converts "31" to float
