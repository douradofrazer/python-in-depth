numbers = [1, 45, 31, 16, 60]

for x in numbers:
    if x % 8 == 0:
        print("These numbers are unacceptable")
        break
else:
    print("These numbers are fine!")
