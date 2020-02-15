# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#
# print("-" * 30)

available_exits = ["north", "south", "east", "west"]
chosen_exist = ""
while chosen_exist not in available_exits:
    chosen_exist = input("Please choose a direction:")
    if chosen_exist.casefold() == "quit":
        print("Game Over")
        break
else:  # this will only print if the loops exits naturally and not if forced by break
    print("aren't you glad you got out of there!")
