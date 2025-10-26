#Please choose an operation:
#1. Display all numbers
#2. Display only even numbers
#3. Calculate the sum and average
#4. Perform a bitwise operation on all numbers
#5. Check if a target value is present
#6. Quit

# I should be using .split(" ") in stead of just eliminating the " " with replace
# it all still works but makes the value checks useless on the array input validation
# since its only working on single characters at a time
# We settled on a new house last Friday the 3rd and work has been brutal
# so this or the midterm isnt my best work and a bit rushed
# but it should all work for what you are looking for
# also would have liked to reduce the values down to 4 bits for bitwise ops but agian out of time
def exit_check ( input_value ):
    if input_value.lower() == "quit":
        print("Goodbye!!")
        exit()

#used to always check for exit command
def custom_user_entry( input_message ):
    input_value = input(input_message)
    exit_check( input_value )
    return input_value
# deals with checking the user entered value for the select is correct based on input and approved values
def single_integer_check_loop ( input_value, approved_values ):
    valid_entry = False
    entry_int = ''
    while not valid_entry:
        try:
            entry_int = int(input_value)
        except:
            print("must be an integer of values",*approved_values,sep=" ")
            input_value = custom_user_entry("Please Enter an integer:\n")
            continue
        if entry_int in approved_values:
            valid_entry = True
        else:
            print("must be an integer of values",*approved_values,sep=" ")
            input_value = custom_user_entry("Please Enter an integer:\n")
    return entry_int
#confirms valusa are integers and in approved values (see top comments)
def integer_check ( input_value, approved_values ):
    input_value = input_value.replace(" ","")
    error_strings = []
    for i in range(len(input_value)):
        valid_int = False
        try:
            int( input_value[i] )
            valid_int = True
        except ValueError:
            error_strings.append(f"Value at position {i}:{input_value[i]} is not an integer")
        if valid_int:
            if i not in approved_values:
                error_strings.append(f"Value at position {i}:{input_value[i]} must be an integer of values {' '.join(map(str,approved_values))}")
    return error_strings
#confirms correct length of input
def length_check (input_value):
    error_string = ""
    input_value = input_value.replace(" ","")
    if len(input_value) > 4:
        error_string = f"Please only enter a list of 4; Entered a list of {len(input_value)}"
    return error_string
#converts input into integers
def convert_integer_array(input_value):
    input_value = input_value.replace(" ","")
    integer_array = []
    for i in range(len(input_value)):
        integer_array.append(int( input_value[i] ))
    return integer_array
#method for handling user list entry
def begin_entry():
    errors = True
    while errors:
        user_entry = custom_user_entry("Please enter 4 integers seperated by spaces or type Quit to exit at any time: \n")
        check_length = length_check(user_entry)
        entry_check = integer_check(user_entry,[0,1,2,3,4,5,6,7,8,9])
        if check_length != "":
            print(check_length)
        elif len(entry_check) != 0:
            print(*entry_check,sep="\n")
        else:
            errors = False
    return convert_integer_array(user_entry)
#finds sum of input
def find_sum(input_array):
    sum_total = 0
    for number in input_array:
        sum_total += number
    return sum_total
#finds average
def find_average(input_array):
    sum_total = find_sum(input_array)
    return sum_total/4
#combines sum and average
def sum_average_value(input_array):
    return f"Sum = {find_sum(input_array)} Average = {find_average(input_array)}"
#displays all number
def display_all_numbers(input_array):
    return " ".join(map(str,input_array))
#diplays all even numbers
def display_even_numbers(input_array):
    even_numbers = []
    for number in input_array:
        if (number % 2) == 0:
            even_numbers.append(number)
    if not even_numbers:
        return f"There are no even number is entered list"
    return f"The following numbers in the list are even: {",".join(map(str,even_numbers))}"
#checks for value in list
def check_for_value(input_array):
    user_entry = custom_user_entry("Enter value to check for:\n")
    user_entry_int = single_integer_check_loop(user_entry,[0,1,2,3,4,5,6,7,8,9])
    if user_entry_int in input_array:
        return f"Value {user_entry_int} is in list"
    else:
        return f"Value {user_entry_int} is not in list"
#exit option
def user_exit(input_array):
    print("Well fine then no more fun with list",*input_array,sep=" ")
    exit()
#bitwise OR ^
def bitwise_or_exclusive(input_array):
    print("This is a bitwise Exclusive OR Operator","   Enter 1 to perform the operator on the List Starting at Index 0","   Enter 2 to start from Index 3",sep="\n")
    valid_entries = [1,2]
    user_entry = custom_user_entry('Please enter 1 or 2:\n')
    user_entry_int = single_integer_check_loop(user_entry,valid_entries)
    bitwise_or_result = ''
    pos_one = input_array[0]
    pos_two = input_array[1]
    pos_three = input_array[2]
    pos_four = input_array[3]
    if user_entry_int == 1:
        bitwise_or_result = pos_one ^ pos_two
        bitwise_or_result = bitwise_or_result ^ pos_three
        bitwise_or_result = bitwise_or_result ^ pos_four
    else:
        bitwise_or_result = pos_four ^ pos_three
        bitwise_or_result = bitwise_or_result ^ pos_two
        bitwise_or_result = bitwise_or_result ^ pos_one
    return f"The final value of the bitwise or exclusive = {bitwise_or_result}"
#bitwise or |
def bitwise_or_non_exlusive(input_array):
    print("This is a bitwise Non-Exclusive OR Operator","   Enter 1 to perform the operator on the List Starting at Index 0","   Enter 2 to start from Index 3",sep="\n")
    valid_entries = [1,2]
    user_entry = custom_user_entry('Please enter 1 or 2:\n')
    user_entry_int = single_integer_check_loop(user_entry,valid_entries)
    bitwise_or_result = ''
    pos_one = input_array[0]
    pos_two = input_array[1]
    pos_three = input_array[2]
    pos_four = input_array[3]
    if user_entry_int == 1:
        bitwise_or_result = pos_one | pos_two
        bitwise_or_result = bitwise_or_result | pos_three
        bitwise_or_result = bitwise_or_result | pos_four
    else:
        bitwise_or_result = pos_four | pos_three
        bitwise_or_result = bitwise_or_result | pos_two
        bitwise_or_result = bitwise_or_result | pos_one
    return f"The final value of the bitwise OR = {bitwise_or_result}"
#bitwise AND
def bitwise_and(input_array):
    print("This is a bitwise AND Operator","   Enter 1 to perform the operator on the List Starting at Index 0","   Enter 2 to start from Index 3",sep="\n")
    valid_entries = [1,2]
    user_entry = custom_user_entry('Please enter 1 or 2:\n')
    user_entry_int = single_integer_check_loop(user_entry,valid_entries)
    bitwise_and_result = ''
    pos_one = input_array[0]
    pos_two = input_array[1]
    pos_three = input_array[2]
    pos_four = input_array[3]
    if user_entry_int == 1:
        bitwise_and_result = pos_one & pos_two
        bitwise_and_result = bitwise_and_result & pos_three
        bitwise_and_result = bitwise_and_result & pos_four
    else:
        bitwise_and_result = pos_four & pos_three
        bitwise_and_result = bitwise_and_result & pos_two
        bitwise_and_result = bitwise_and_result & pos_one
    return f"The final value of the bitwise AND = {bitwise_and_result}"
#menus for bitwise
bitwise_menu = {
    "1: Exclusive OR" : bitwise_or_exclusive,
    "2: Non-Exclusive OR" : bitwise_or_non_exlusive,
    "3: AND" : bitwise_and
}
#main menus desiged to dynamically call functions
main_menu = {
    "1: Display all numbers": display_all_numbers,
    "2: Display only even numbers": display_even_numbers,
    "3: Calculate the sum and average": sum_average_value,
    "4: Perform a bitwise operation on all numbers": bitwise_menu,
    "5: Check if a target value is present": check_for_value,
    "6: Quit": user_exit
}
#method to work through user input and dynamically call out to selected function
def handle_menu_select(input_array):
    print(*main_menu.keys(), sep='\n')
    user_select = custom_user_entry("Choose Menu Option: ")
    user_select = single_integer_check_loop(user_select,[1,2,3,4,5,6])
    menu_list = list(main_menu.keys())    
    menu_text = menu_list[user_select -1]
    #there is a better way to do this but I am tired
    if user_select == 4:
        print(*bitwise_menu.keys(), sep='\n')
        user_select = custom_user_entry("Choose Bitwise Option: ")
        user_select = single_integer_check_loop(user_select,[1,2,3])
        menu_list = list(bitwise_menu.keys())    
        menu_text = menu_list[user_select -1]
        final_value = bitwise_menu[menu_text](input_array)
    else:
        final_value = main_menu[menu_text](input_array)
    print( "Returned Value: ", final_value )
#main body of script to continuely prompt user until exited
print("Welcome to the Basic Number-Processing Tool!")
print("   To exit at any time type: Quit")
user_entered_list = begin_entry()

print("Please Choose a number from the following options or Press q to Exit:")

user_done = False
while not user_done:
    handle_menu_select(user_entered_list)
    and_another = custom_user_entry("Would you like to continue yes/no: ")
    if and_another.lower() == "yes":
        user_done = False
        print("Please Choose a number from the following options or Press q to Exit:")
    elif and_another.lower() == "no":
        user_done = True
    else:
        while and_another.lower() not in ["yes", "no"]:
            and_another = custom_user_entry("Please enter 'yes' or 'no': ")
