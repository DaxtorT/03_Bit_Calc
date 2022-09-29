# Calculates the # of bits for text (# of characters x 8)
def text_bits():

    print ()
    # Ask user for a string
    var_text = input("Enter some text: ")

    # Calculate # of bits (Length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # Output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8 ...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

# Main Routine goes here
text_bits()