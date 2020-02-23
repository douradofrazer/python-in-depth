"""
write a program to append the times table to the sample.txt.
we want tables from 2 to 12
"""

with open("./sample.txt", "a") as tables:
    for i in range(1, 13):
        for j in range(1, 13):
            print("{} times {} is {}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)
