# Function goes here

#Checks for an integer more than 0
def int_check(question):

    error = "please enter a number that is more 0"

    valid = False
    while not valid:

        # Ask user for number and check if valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # If an integer is not entered, display error
        except ValueError:
            print(error)



