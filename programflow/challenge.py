option = "-"
while option != "0":
    if option in "12345":
        print("You chose {}".format(option))
    else:
        print("Please enter your option from the list below:\n"
              "1. Learn Python\n"
              "2. Learn Java\n"
              "3. Go Swimming\n"
              "4. Have Dinner\n"
              "5. Go to bed\n"
              "0. Exit")
    option = input()
