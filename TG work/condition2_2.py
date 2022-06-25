n = 0

while n != 100:
    try:
        n = int(input("Gimme a number bro: "))

        if n < 100:
            print("too low")
        elif n > 100:
            print("too high")
        else:
            print("100 is correct!")
            break
    except ValueError:
        print("thats not a number dude")
