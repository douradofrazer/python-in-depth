"""
Create a list of items then create an iterator using the
iter() function.
Use a for loop to loop "n" times, where n is the number of items in your list.
Each time round the loop, use next() on your list to print the next item.
"""
example = "1234567890"
it = iter(example)

for i in range(len(example)):
    print(next(it))
