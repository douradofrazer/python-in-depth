my_list = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
# join method can be used on any sequence and is more efficient than
# concatenation of strings as string are immutable.
new_string = ", ".join(my_list)
print(new_string)
new_string = ", ".join(letters)
print(new_string)
new_string = " mississippi ".join(numbers)
print(new_string)

