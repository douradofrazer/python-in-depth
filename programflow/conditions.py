"""
When comparing conditions using 'and', python will stop checking as soon as it find
a condition that is False.
When comparing conditions using 'or', it will stop as soon as it finds one that is
True.
"""

age = int(input("How old are you?"))

# if age >= 16 and age <= 65:
if age in range(16, 66):  # simplified comparison
    print("Have a good day at work!")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")