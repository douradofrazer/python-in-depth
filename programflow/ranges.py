# Range produces a range of numbers from the starting value,
# up to but not including the end value.

# Start defaulting to zero
# range(0, 10)
for i in range(10):
    print("i is now {}".format(i))

print("-" * 30)

# In steps
for i in range(0, 10, 2):
    print("i is now {}".format(i))

print("-" * 30)

# Negative steps
for i in range(10, 0, -2):
    print("i is now {}".format(i))
