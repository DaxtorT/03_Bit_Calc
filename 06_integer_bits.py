# Checks input is a number more than a given value
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


# Convert integer (decimal) to binary and calculates how 
# many bits are needed to represent the original integer
def int_bits():

    # Get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    # Convert decimal to binary
    var_binary = "{0:b}".format(var_integer)

    # Calculate # of bits (length of binary string)
    num_bits = len(var_binary)

    # Output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print("We need {} bits to represent {}".format(num_bits, var_integer))
    print()

    return ""

# Main Routine goes here
int_bits()