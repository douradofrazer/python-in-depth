import random

highest = 10
answer = random.randint(1, highest)

print("Please guess number between 1 and {}:".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    elif guess > answer:
        print("Please guess lower")
    elif guess < answer:
        print("Please guess higher")
