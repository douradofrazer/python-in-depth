letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

# slice for qpo
qpo = letters[16:13:-1]
print(qpo)
# slice for edcba
edcba = letters[4::-1]
print(edcba)
# slice for string to produce last 8 characters in reverse
# rev8 = letters[:17:-1]
rev8 = letters[:-9:-1]
print(rev8)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])  # no exception if string is empty
# print(letters[0]) same as above but throws exception
# if string is empty
