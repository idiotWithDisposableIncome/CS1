#exit command check
def exit_check ( input_value ):
    if input_value.lower() == "q":
        print("Goodbye!!")
        exit()
#used to always check for exit command
def custom_user_entry( input_message ):
    input_value = input(input_message)
    exit_check( input_value )
    return input_value
#validate for float on decimal based conversions
def float_check ( input_value ):
    try:
        float( input_value )
        return float( input_value )
    except ValueError:
        correct_value = False
        input_value = ""
        while not correct_value:
            input_value = custom_user_entry("Please only enter a decimal: ")
            if input_value.isdecimal():
                input_value = float(input_value)
                correct_value = True
            else:
                print("Really how hard is this enter a number!!")
        return input_value
#validate for integer based conversions
def integer_check ( input_value ):
    try:
        int( input_value )
        return int( input_value )
    except ValueError:
        correct_value = False
        input_value = ""
        while not correct_value:
            input_value = custom_user_entry("Please only enter a decimal: ")
            if input_value.isdigit():
                input_value = int(input_value)
                correct_value = True
            else:
                print("Really how hard is this enter a number!!")
        return input_value

def fahrenheit_to_celsius ( input_value ):
    input_value = float_check( input_value )
    final_value = round((input_value - 32) * (5/9),2)
    return f"{input_value}\u00b0F is {final_value}\u00b0C"

def celsius_to_fahrenheit ( input_value ):
    input_value = float_check( input_value )
    final_value = round((input_value * ( 9/5 ) ) + 32,2)
    return f"{input_value}\u00b0C is {final_value}\u00b0F"

def miles_to_kilometers ( input_value ):
    input_value = float_check( input_value )
    final_value = round(input_value * 1.60934,2)
    return f"{input_value} miles is {final_value} kilometers"

def kilometers_to_miles ( input_value ):
    input_value = float_check( input_value )
    final_value = round(input_value / 1.60934,2)
    return f"{input_value} kilometers is {final_value} miles"

def pounds_to_kg ( input_value ):
    input_value = float_check( input_value )
    final_value = round(input_value / 2.205,2)
    return f"{input_value} pounds is {final_value} kilograms"

def kg_to_pounds ( input_value ):
    input_value = float_check( input_value )
    final_value = round(input_value * 2.205,2)
    return f"{input_value} kilograms is {final_value} pounds"

def binary_to_decimal ( input_value ):
    #implement check that input is binary
    if not set(input_value).issubset({'0', '1'}):
        correct_value = False
        input_value = ""
        #these while loops could probably be abstracted into 1 method
        while not correct_value:
            input_value = custom_user_entry("Please only enter a binary value: ")
            if set(input_value).issubset({'0', '1'}):
                correct_value = True
            else:
                print("Really how hard is this enter a binary value!!")

    decimal_value = 0
    for digit in input_value:
        # Convert the character digit to an integer
        int_digit = int(digit)
        # Apply Horner's method: multiply by base and add current digit
        decimal_value = (decimal_value * 2) + int_digit
    return f"{input_value} binary is {decimal_value} in decimal"

def decimal_to_binary ( input_value ):
    input_value = integer_check( input_value )
    final_value = f"{input_value:b}"
    return f"{input_value} decimal is {final_value} in binary"

conversions = {
    "1: fahrenheit to celsius": fahrenheit_to_celsius,
    "2: celsius to fahrenheit": celsius_to_fahrenheit,
    "3: miles to kilometers": miles_to_kilometers,
    "4: kilometers to miles": kilometers_to_miles,
    "5: pounds to kgs": pounds_to_kg,
    "6: kg to pounds": kg_to_pounds,
    "7: binary to decimal": binary_to_decimal,
    "8: decimal to binary": decimal_to_binary,
}

print("Welcome to the Unit Converter\n", end='\n')

print("Please Choose a number from the following options or Press q to Exit:")

print(*conversions.keys(), sep='\n')

#implement selection validation
#implement error loop
#implement post choice continuance loop
#let users drop out when done
user_done = False
while not user_done:
    conversion_choice = ""
    correct_conversion = False
    while not correct_conversion:
        conversion_choice = custom_user_entry("Choose Conversion 1-8: ")
        if conversion_choice.isdigit():
            conversion_choice = int(conversion_choice)
            if conversion_choice < 9 and conversion_choice > 0:
                correct_conversion = True
            else:
                print("Please enter a number between 1-8")
        else:
            print("Please enter a number between 1-8")

    conversions_list = list(conversions.keys())
    conversion_text = conversions_list[conversion_choice -1]

    user_input_value = custom_user_entry("Please Enter a value for "+conversion_text+ ": ")

    final_value = conversions[conversion_text](user_input_value)
    print( "Converted Value: ", final_value )
    
    and_another = custom_user_entry("Would you like to continue yes/no: ")
    if and_another.lower() == "yes":
        user_done = False
        print("Please Choose a number from the following options or Press q to Exit:")
        print(*conversions.keys(), sep='\n')
    elif and_another.lower() == "no":
        user_done = True
    else:
        while and_another.lower() not in ["yes", "no"]:
            and_another = custom_user_entry("Please enter 'yes' or 'no': ")
