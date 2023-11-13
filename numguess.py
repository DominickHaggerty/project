import random

while True:

    number = random.randint(1, 100)
    print(number)

    player = int(input("guess a number:    "))


    if(player == number):
        print("That is the number")

    elif(player > number):
        print("lower")
    
    else:
        print("higher")









