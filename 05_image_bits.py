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


# Calculates the # of bits for 24 bit colour
def image_bits():

    # Ask user for image width and height
    image_width = num_check("Image Width: ", 1)
    image_height = num_check("Image Height: ", 1)

    # Calculate # of pixels (Width x Height)
    num_pixels = image_width * image_height
    
    # Calculate # of bits in 24 bit colour (Pixels x 24)
    num_bits = num_pixels * 24

    # Output answer with working
    print()
    print("# of pixels is {} x {} = {}".format(image_width, image_height, num_pixels))
    print("# of bits = {} x 24 = {}".format(num_pixels, num_bits))
    print("We need {} bits to represent your image".format(num_bits))
    print()

    return ""

# Main Routine goes here
image_bits()