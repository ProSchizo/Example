def while_loop():
    n = int(input("gimme a big number!"))
    counter = 0
    while(n > 10):
        n = n / 2
        counter = counter + 1
    print("it took", counter, "divisions to be less than 10")
    password = "obvious_password"
    their_guess = input("password: ")
    while(their_guess != password):
        print("you dummy! that's wrong!")
        their_guess = input("guess again: ")
    print("you got it!")



while_loop()
