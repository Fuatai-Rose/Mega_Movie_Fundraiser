# Valid snacks holds list of all snacks
# Each item in valid snacks is a list with
# Valid options for each snack <full name, letter code (a - e)
# and possible abbreviations etc. >
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"], # First item is M&M
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]
# initialise variables

snack_ok = ""
snack = ""

# Loop three times to make testing quicker
for item in range(0, 3):

    # Ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        # If the snack is in one of the lists, return the full name of that snack
        if desired_snack in var_list:

            # Get full name of snack and put it
            # In title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        # if the chosen snack is not valis, set snack_ok to no
        else:
            snack_ok = "no"

    # If the snack is not OK - ask question again.
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("invalid choice")
