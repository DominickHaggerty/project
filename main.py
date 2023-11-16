import random


def main():
    play_game()


def play_game():
    print("Would you like to guess a number?")
    playGame = input("Enter Response: ")
    playGame = playGame.capitalize()
    print("Starting Game!")
    while playGame == ("Yes"):
        number = generate_random_number()
        attempts = 0
        while attempts != 3:
            player = player_guess()
            feedback = give_feedback(player, number)
            if feedback == 1:
                attempts += 1
            elif feedback == 0:
                break
            else:
                print("This message should not be coming up")
        print("Game Over, the number was ", number,
              " and you used ", attempts, " attempts.")
        playAgain = new_game()
        if playAgain == 1:
            new_game()


def generate_random_number():
    return random.randint(1, 100)


def player_guess():
    return int(input("Guess a number: "))


def give_feedback(player, number):
    if (player == number):
        print("Correct!")
        return 0
    elif (player > number):
        print("Lower")
        return 1
    else:
        print("Higher")
        return 1


def new_game():
    print("Would you like to play again?")
    playAgain = input("Enter Response: ")
    playAgain = playAgain.capitalize()
    if playAgain == ("Yes"):
        return 1
        print("RESTARTING GAME")  # change to restart function
    elif playAgain == ("Yeah"):
        return 1
        print("eeeee")
    else:
        return 0
        print("Ok :(")


if __name__ == "__main__":
    main()
