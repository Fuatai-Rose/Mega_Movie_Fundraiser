# Function goes here

def int_check(question, low_num, high_num):

    error = "please enter a whole number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # Ask user for number and check if valid
        try:
            response = int(input(question))

            if low_num < response < high_num:
                return response
            else:
                print(error)

        # If an integer is not entered, display error
        except ValueError:
            print(error)


# main function
age = int_check("Age: ", 12, 130)
