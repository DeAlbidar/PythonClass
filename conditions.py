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
