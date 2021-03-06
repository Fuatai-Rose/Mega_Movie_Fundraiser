# Import statements
import re
import pandas

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

# Checks for an integer more than 0
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

# checks number of tickets left and warns user
# if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    # tells user how mny seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

        # warns user that only one seat is left
    else:
        print("***There is only one seat left!!***")

    return ""

# Gets ticket price based on age
def get_ticket_price():

    # Get age (between 12 and 130
    age = int_check("Age: ")

    # Check that age is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age <65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price

# * * * * * * * * Main Routine * * * * * * * *

# Set up dictionaries / lists needed to hold data

# Initialise loops so that it runs at least once
MAX_TICKETS = 5

name = " "
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets

}

# ask user if they have used the program before and show instructions

# loop to get tickets details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # Check numbers of ticker limit has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # Get details for each ticket

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # end of loop if the exit code is entered
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()
    # if age is invalid, restart loop and get name again
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks

    # Get payment method (ie: work out if surcharge is needed)

# End of tickets / snacks / payment loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# tell user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets!")
else:
    print("You have sold {} tickets.".format(ticket_count))
    print("There are {} places still available".format( MAX_TICKETS - ticket_count))

