# Function goes here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays Instructions / Information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that asci encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""


# Checks if user choice is 'integer', 'text' or 'image'
def user_choice():

    # Lists of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "p", "picture", "pic"]
    
    valid = False
    while not valid:

        # Ask user for choice and change response to lowercase
        response = input("File Type (integer / text / image): ").lower()

        # Checks for valid response and returns text, integer or image
               
        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image.")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # If response is not valid, output an error
            print("Please choose a valid file type!")
            print()


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


# Calculates the # of bits for text (# of characters x 8)
def text_bits():

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

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)
    print()

    # For integers, ask for integer
     # (Must be an integer more than or equal to 0)
    if data_type =="integer":
        int_bits()
   
    # For images, ask for width and height
    # (Must be integers more than or equal to 1)
    elif data_type =="image":
        image_bits()
    
    # For text, ask for a string
    else:
        text_bits()
    
    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()