# Boolean expressions
day = "Monday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Learn Python")

# Truthy Values
# 0 is considered false
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
# empty sequence is considered false
if name:  # if name != ""
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
