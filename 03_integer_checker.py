# Checks if the integer is more than or equal to 0
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than (or equal to) {}".format(low)

        try:

            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if response >= low:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()
            
        except ValueError:
            print(error)


# Main Routine goes here

keep_going = ""
while keep_going == "":
    print()
    # Asks user for an integer (Must be more than or equal to 0)
    var_integer = num_check("Enter an integer: ", 0)
    print()

    # Ask for width & height of an image
    # (Must be more than or equal to 1)
    image_width = num_check("Image Width? ", 1)
    print()
    image_height = num_check("Image Height? ", 1)
