def age():
    their_age = int(input("how old r u? "))
    their_salary = int(input("how much do u make?"))
    # rich: 250000
    # poor: 30000
    if (their_age > 32 and their_salary >= 250000):
        print("ur old but let's be friends")
    elif (their_age > 32 and their_salary <= 250000):
        print("too poor sry")
    elif (their_age <= 12):
        print("go back to middle school loser")
    else:
        print("wow let's be friends!")

age()
