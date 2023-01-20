# Assignment 1 (down_payment)
# Price of a house is $1M
# If buyer has good credit,
#     they need to put down 10%
# otherwise
#     they need to put down 20%
# Print the down payment


def down_payments():
    house_price = 1000000
    credit_status = True
    if credit_status:
        down_payment = 0.1 * house_price
        print(f"You need to make a down payment of ${down_payment}")
    else:
        down_payment = 0.2 * house_price
        print(f"You need to make a down payment of ${down_payment}")


# Assignment 2
# if name is less than 3 characters long
#   name must be at least 3 characters
# otherwise if it's more than 50 characters long
#   name can be a maximum of 50 characters
# otherwise
#   name looks good!

def characters_check():
    text_count = len(input("Enter Your Name: "))
    max_characters = 50
    min_characters = 3
    if text_count < min_characters:
        print("Name must be at least 3 characters")
    elif text_count > max_characters:
        print("Name can be a maximum of 50 characters")
    else:
        print("Name looks Good!")


# Weight Converter

def weight_converter():
    input_weight = int(input("Weight: "))
    unit = input("(L)bs or (K)g: ").lower()
    if input_weight:
        if unit == "l":
            weight = input_weight * 0.45
            print(f"You are {weight} kilos")
        elif unit == "k":
            weight = input_weight / 0.45
            print(f"You are {weight} pounds")
        else:
            print("I don't understand the command...")

