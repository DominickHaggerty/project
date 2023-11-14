def gameover():
    playagain()

def playagain():
    print("Would you like to play again?")
    playAgain = input("Enter Response: ")
    playAgain = playAgain.capitalize()
    if playAgain == ("Yes"):
        print("RESTARTING GAME") #change to restart function
    elif playAgain == ("Yeah"):
        print("eeeee")
    else:
        print("Ok :(")
    
if __name__ == "__main__":
    gameover()