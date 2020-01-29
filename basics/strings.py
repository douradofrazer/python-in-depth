print("Python's string are easy to use")
print('we can even include "quotes" in strings')
print('hello' + ' world')

greeting = 'Hello'
name = 'Jack'  # input('Please enter your name: ')
age = 25

print(greeting + ' ' + name)

# Rules for variable names
# - Variable names must begin with a letter (either upper or lower case) or
# and underscore _ character
# - Can contain letter, numbers or underscore characters (but cannot begin with
# a number)
# - Variables are case sensitive, so 'greetings' and 'Greetings' would refer
# to 2 different variables
# - Variables are created when they first attach to a value, using =.

print(type(greeting))
print(type(age))

# Built-in data types in python:
# - Numeric
#   int, float, complex (int replaces long in python 3,
#   long existed in python 2 as int couldn't store very large values)
#   int has no size limit, we will run out of memory before we ever find a size limit for int
#   float has 52 digits of precision, if more precision is required we can use Decimal
# - Iterator
# - Sequence (which are also iterators)
# - Mapping
# - File
# - Class
# - Exception

parrot = "Norwegian Blue"

s = "we win"
print(s[0])
print(s[-1])
print()

# Slice
# Inclusive of first up till but not including the end
print(parrot[0:6])  # Norweg
print(parrot[-14:-8])
print(parrot[0:4])
print(parrot[:4])
print(parrot[4:])
print(parrot[:])
# [] used for indexing and slicing
print(parrot[-4:-2])
print(parrot[-4:12])
# step in slice
print(parrot[0:6:3])  # Nw
print()

# Example of where slice would be useful
number = "9,233;373:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print()

# f-string, works on python 3.6 or higher
print(name + f" is {age} years old")
print(f"Pi is approximately {22 / 7 : 12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
