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
# Programme to calculate the total items in a shopping cart using for loop
# Example: prices = [10, 20, 30]

def cart():
    prices = [10, 20, 30]
    total = 0
    for items in prices:
        total += items
    print(f"Total: {total}")


# For loop
# Programme that will draw 'F' shape using for loop
#
def draw_f():
    numbers = [5, 2, 5, 2, 2]
    for i in numbers:
        print("*" * i)


# For loop
# Programme that will draw 'F' shape using for loop
#
def draw_f_2():
    numbers = [5, 2, 5, 2, 2]
    print_x = "x"
    for i in numbers:
        print_x_2 = ""
        for ii in range(i):
            print_x_2 += print_x
        print(print_x_2)
