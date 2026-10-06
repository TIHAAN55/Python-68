print("===== Welcome to car bulider =====")

type = int(input("Choose car(2) or bike(1)."))

if type == 1:

    print("Choose type:")
    print(" 1. Scootee")
    print(" 2. Mountain bike")

    choice = int(input("Enter type 1 or 2"))

    if choice == 1:
        print("You have officially selected your vehicle, a scootee.")
    else: 
        print("You have officially selected your vehicle, a mountain bike.")

if type == 2:
    print("Choose type:")
    print("1. SUV")
    print("2. Sedan")

    choiced = int(input("Enter 1 or 2."))

    if choiced == 1:
        print("You have seleceted an SUV.")
    else:
        print("You have selected a Sedan.")