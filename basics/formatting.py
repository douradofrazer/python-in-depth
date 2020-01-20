for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()
# left aligned: < , right aligned: > (default), center aligned: ^
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))  # General format, print 15 decimals
print("Pi is approximately {0:12f}".format(22 / 7))  # f signifies default of 6 digits
print("Pi is approximately {0:12.50f}".format(
    22 / 7))  # .50 is precision, but python does not truncate numbers hence considers precision over field width
# Below 3 lines print the same value in different widths
# Max precision of python float number is between 51 & 53 digits
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))