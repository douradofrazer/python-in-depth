low = 1
high = 1000

print("Please think of a number between {0} and {1}".format(low, high))
input("Press Enter to start")
guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     "Enter h or l, or c if my guess was correct : ".format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The lower end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses += 1

else:
    print("You though of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
