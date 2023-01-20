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


weight_converter()