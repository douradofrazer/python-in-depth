normal_list = ["non pinin", "no more", "space", "jets"]
# append to the list above
normal_list.append("A Norwegian Blue")

for item in normal_list:
    print("This item is: " + item)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
# sort work on the existing variable and does not create a new instance
#numbers.sort()
print(numbers)
# if want to sort and create a new instance we use an inbuilt method
numbers_in_order = sorted(numbers)
print(numbers_in_order)