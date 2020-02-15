# using for loop to extract separators
# number = "9,233;373:036 854,775;807"
number = input("Please enter a series of numbers, using any separator you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

# continue
shopping_list = ["Milk", "Bread", "Eggs", "Spam", "rice"]

for item in shopping_list:
    if item == "Spam":
        continue
    print(item)