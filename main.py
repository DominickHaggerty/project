import random


number = random.randint(1, 100)


# working on while loop for the logic part based off Dom's original game code.
def player_guess():

    for x in range(30):
        player = int(input("guess a number:"))

    if (player == number):
        print("Correct!")

    elif (player > number):
        print("Lower")

    else:
        print("Higher")

    player = int(input("guess another number:"))

    if (player == number):
        print("That is the number")

    elif (player > number):
        print("lower")

    else:
        print("higher")

    player = int(input("guess another number:   "))

    if (player == number):
        print("That is the number")

    elif (player > number):
        print("You lose")

    else:
        print("You lose")

    print(number)
