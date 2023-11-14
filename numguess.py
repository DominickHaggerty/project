import random



number = random.randint(1, 100)


player = int(input("guess a number:    "))


if(player == number):
    print("That is the number")

elif(player > number):
    print("lower")
    
else:
    print("higher")

player = int(input("guess another number:   "))

if(player == number):
    print("That is the number")

elif(player > number):
    print("lower")
    
else:
    print("higher")


player = int(input("guess another number:   "))

if(player == number):
    print("That is the number")

elif(player > number):
    print("You lose")
    
else:
    print("You lose")

print(number)






