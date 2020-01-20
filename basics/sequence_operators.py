# Python 3 has 5 sequence types built in:
# - String type
# - List
# - Tuple
# - Range
# - Bytes and Byte array
# A sequence is defined as an ordered set of items.
# A sequence is ordered.
# Not all sequences can be concatenated or multiplied. Range cannot be concatenated.

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")

print("Hello " * 5)  # multiplication operator print sequence 5 times

today = "friday"
print("day" in today)  # True
print("fri" in today)  # True
print("thur" in today)  # False
print("parrot" in "fjord")  # False
