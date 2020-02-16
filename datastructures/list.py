list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("List are equal!")

even = [2, 4, 6, 8]
# another_even point to the same list even
another_even = even
# To prove the above statement
# is states that it point to same variable in memory, not if contents are equal
print(another_even is even)
# Both another_even and even are reversed as they point to same object
another_even.sort(reverse=True)
# another_even = sorted(even, reverse=True)
print(even)
# if we make a new list, then even and another_even will be different
another_even = list(even)
print(another_even is even)
# To prove contents are equal we use ==
print(another_even == even)

odd = [1, 3, 5, 7, 9]
numbers = [even, odd]
for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
