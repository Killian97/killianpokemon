while True:
    try:
        number = int(input("What is the number? "))
        if number == 100:
            print(number, "Is correct you win!")
            break
        elif number > 100:
            print(number, "Is a bit to high mate")
        elif number < 100:
            print (number, "Is a bit low innit")
    except ValueError:
        print("Thats not an int number mate")
