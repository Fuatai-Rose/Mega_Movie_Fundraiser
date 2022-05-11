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

# check for an integer more than 0
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


# * * * * * * * * Main Routine * * * * * * * *

# Set up dictionaries / lists needed to hold data

# ask user if they have used the program before and show instructions if necessary

# Loop to get ticket details
MAX_TICKETS = 5

name = " "
ticket_count = 0
ticket_sales = 5


while name != "xxx" and ticket_count < MAX_TICKETS:

    # Warn user that the seats are almost sold out
    if ticket_count >= MAX_TICKETS - 1:
        print("There is ONE seat left!")

    # Tells user how many seats are left
    else:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    # Get details

    # Get name (Can't be blank)
    name = not_blank("Name: ")

    # End the loop if the exit code is entered
    if name == "xxx":
        break

    # Get age between 12 and 130
    age = int_check("Age: ")

    # Check if age is valid
    if age < 12:
        print("Sorry, you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

# End of tickets loop
# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. There are {} places still available".format(ticket_count,
                                                                                 MAX_TICKETS - ticket_count))

# End of tickets loop

# Calculate ticket price

# Loop to ask for snacks

# Calculate snack price

# Ask for payment method (and apply surcharge if necessary)

# Calculate Total sales and profit

# Output data to text file
