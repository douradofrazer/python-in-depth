fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# "apple": "round and crunchy"} Duplicate key over writes the original value

print(fruit)
print(fruit["orange"])
fruit["pear"] = "an odd shaped apple"
print(fruit["pear"])
# assigning a new value to an existing key in dictionary
fruit["pear"] = "great with tequila"
# remove item from dictionary
del fruit["lemon"]
print(fruit)

# delete whole dictionary, del fruit
# To empty the dictionary we use
# fruit.clear()
# print(fruit["tomato"]) This throws an error if key does not exist

# while True:
#     dick_key = input("Please enter a fruit: ")
#     if dick_key == "quit":
#         break
#     description = fruit.get(dick_key, "we don't have a {}".format(dick_key))
#     print(description)
#     if dick_key in fruit:
#         description = fruit.get(dick_key)
#         print(description)
#     else:
#         print("we don't have a {}".format(dick_key))

# Dictionary is not ordered
# for snack in fruit:
#     print(fruit[snack])
# We can order it as follows:
# for f in sorted(list(fruit.keys())):
#     print(f + " - " + fruit[f])

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, desc = snack
    print(item + " is " + desc)

# create a dictionary from a tuple
print(dict(f_tuple))

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmm, lovely",
       "spinach": "can I have some more fruit, please"}

# update a dictionary with another
veg.update(fruit)
print(veg)
# copy of dictionary
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
