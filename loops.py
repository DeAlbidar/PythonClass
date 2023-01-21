# While loop
# Assignment 1
# Guessing Game

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


# While loop
# Assignment 2
# Car Game
#
# help
#   start - to start the car
#   stop - to stop the car
#   quit - to exit

def car():
    car_status = False
    car_stop = False
    while True:
        command = input("> ").lower()
        if command == "start":
            if not car_status:
                car_status = True
                car_stop = False
                print("Car started... Ready to go!")
            else:
                print("Car already started...")
        elif command == "stop":
            if not car_status:
                print("Car not started...")
            else:
                if not car_stop:
                    car_stop = True
                    car_status = False
                    print("Car stopped.")
                else:
                    print("Car already stopped.")
        elif command == "help":
            print("start - to start the car")
            print("stop - to stop the car")
            print("quit - to exit")
        elif command == "quit":
            break
        else:
            print("Sorry, I don't understand that...")


# For Loops
# 


