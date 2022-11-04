def game():
    """The function guesses what number between 1 and 1000 the user has chosen"""
    print("Think a number from 0 to 1000 and I'll guess it in max. 10 tries")
    min = 0
    max = 1000
    answer = ""
    while answer != "you guessed it":
        guess = int((max - min) / 2) + min
        print(f"I guess {guess}")
        answers = ["too small", "too big", "you guessed it"]
        while True:
            answer = input(
                "If the number you selected is greater enter too small, \nif it is smaller, enter too big \nif I guessed it, enter you guessed it ")
            if answer in answers:
                break
            else:
                print("You entered the wrong answer, possible answers: too small, too big, you guessed it ")
        if answer == "too big":
            max = guess
        elif answer == "too small":
            min = guess
        elif answer == "you guessed it":
            print("I win")
        else:
            print("Don't cheat")


if __name__ == '__main__':
    game()
