farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

"""
Cannot create an empty set with just brackets {},
{} creates a dictionary hence we need to use, set()
"""
empty_set = set()
empty_set_2 = {}  # creates a dictionary
empty_set.add(1)
# empty_set_2.add(1) fails as its not a set

even = set(range(0, 20, 2))
print(even)
print(len(even))
square_tuple = (4, 9, 16, 25)
squares = set(square_tuple)
print(squares)
print(len(squares))

union_numbers = even.union(squares)
print(union_numbers)
print(len(union_numbers))

intersection_numbers = even.intersection(squares)
print(intersection_numbers)
print(even & squares)

print(sorted(squares))  # since set is unordered to make it readable we can sort it
print("even minus squares")
print(even.difference(squares))  # this is preferred as it makes it clear we are working with sets
print(even - squares)

# can use difference update on parent to change it
# even.difference_update(squares)
print(sorted(even))

squares.discard(25)
squares.discard(9)
# This will throw an error if value not in set we need to check if the value exists in set
# squares.remove(16)

# if squares.issubset(even):
#     print("Squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is super set of squares")

even = frozenset(range(0, 20, 2))  # immutable set
print(even)
