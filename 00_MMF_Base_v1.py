# Import statements

# functions go here

# Checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error and repeat loop
        else:
            print("Sorry - this can't be blank")


def int_check(question, low_num, high_num):

    error = "please enter a whole number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # Ask user for number and check if valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # If an integer is not entered, display error
        except ValueError:
            print(error)

    # * * * * * * * * Main Routine * * * * * * * *

    # Set up dictionaries / lists needed to hold data

    # ask user if they have used the program before and show instructions if necessary

    # Loop to get ticket details


name = " "
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # Tells user how many seats are left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # Warn user that the seats are almost sold out
    else:
        print("There is ONE seat left!")

    # Get details

    # Get name (Can't be blank)
    name = not_blank("Name: ")

    # End the loop if the exit code is entered
    if name == "xxx":
        break

    count += 1

    # Get age between 12 and 130
    age = int_check("Age: ", 12, 130)

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} places still available".format(count, MAX_TICKETS - count))

# End of tickets loop

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate Total sales and profit

# Output data to text file
