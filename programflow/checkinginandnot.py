# docs : https://docs.python.org/3/library/stdtypes.html
# in
parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

print("-" * 50)

# not in
activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():
    # casefold() converts string to lowercase but handles certain character sets
    # better than just converting to lower case.
    print("But I want to go to the cinema")
else:
    print("Great I wanna join too.")
