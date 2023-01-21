# While loop
# Assignment 1
# Guessing Game
#

def guess():
    guess_limit = 3
    secret_number = 9
    guess_count = 0
    while guess_count < guess_limit:
        input_txt = int(input("Guess: "))
        guess_count = guess_count + 1
        if input_txt == secret_number:
            print("You win!")
            break
        else:
            print("Wrong Guess, try again...")
    else:
        print("Sorry you failed!")

