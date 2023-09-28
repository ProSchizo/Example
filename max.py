def max():
    temp_list = input("enter at least two numbers, separated by commas",
                      "(no spaces!)")
    user_list = temp_list.split(",")
    user_list = list(map(float, user_list))
    # your code here!
