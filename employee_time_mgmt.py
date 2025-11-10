#
# Time managment system with the following options
# Add an employee’s information
# Remove an employee
# View all employees
# Calculate total payroll
# Convert numeric data (e.g., hours) to alternate numeral systems
# Demonstrate a bitwise operation
# Exit the program
#
# data structure is to be in a list of lists format:
# [[employee_id, employee_name, hours_worked, hourly_rate]]
#
# Provide docstrings for each function
#
# building out ususal set of functions to be called in main menu
# sticking to instructions but this would of been 1000x easier with a dictionary or classes

# custom exit check for all user inputs
def exit_check ( input_value ):
    """
    Checks User Entry for Exit Value of Quit.

    Args:
        input_value (String): Input received by user.

    Returns:
        no return value exits program.
    """
    if input_value.lower() == "quit":
        print("Goodbye!!")
        exit()

# used to always check for exit command
def custom_user_entry( input_message ):
    """
    Takes inpute message and calls exit check or return user input.

    Args:
        input_message (String): Message for user input.

    Returns:
        input_value (String): User Input
    """
    input_value = input(input_message)
    exit_check( input_value )
    return input_value

def add_employee(input_list):
    """
    Gathers and adds Employee to given list.

    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return value, prints confirmation message.
    """
    print('Enter the following information')
    emp_id = int(custom_user_entry('Enter Employee Id: '))
    emp_name = custom_user_entry('Employee Name: ')
    hours_worked = round(float(custom_user_entry('Hours Worked Rounded to 2 decimal places: ')),2)
    hourly_rate = round(float(custom_user_entry('Hourly Rate Rounded to 2 decimal places: ')),2)
    input_list.append([emp_id, emp_name, hours_worked, hourly_rate])
    print('Empoyee: ', emp_name, ' Id: ', emp_id, ' added to system')

def find_employee(input_list):
    """
    Finds Employee from a given Id in List of Lists passed in.
    Checks if Id is valid if not re-prompts User for Id.
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        emp_list (List): Specific user detail list of given Id.
    """
    if check_list_not_empty(input_list): return
    found_emp_id = False
    while not found_emp_id:
        emp_id = int(custom_user_entry('Enter Employee Id: '))
        for emp_list in input_list:
            if emp_list[0] == emp_id:
                return emp_list
        print('Employee Id not found please try again')

def check_list_not_empty(input_list):
    """
    Checks if the Given Employee List is empty.
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        Boolean (Boolean): Returns True if list is empty.
    """
    if len(input_list) == 0:
        print('System currently has no employees')
        return True
    return False

def remove_employee(input_list):
    """
    Removes a given Employee based on Id passed in.
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        No return prints confirm message
    """
    if check_list_not_empty(input_list): return
    emp_list = find_employee(input_list)
    input_list.remove(emp_list)
    print('Employee Id: ', emp_list[0], ' Employee Name: ', emp_list[1], ' Removed')

def view_all_employees(input_list):
    """
    Prints all Employees in given list if not empty
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return only prints Employee details
    """
    if check_list_not_empty(input_list): return
    print('Current employees in system: ')
    for emp_list in input_list:
        print('Employee Id: ', emp_list[0], end=', ')
        print('Employee Name: ', emp_list[1], end=', ')
        print('Hours Worked: ', emp_list[2], end=', ')
        print('Hourly Rate: ', emp_list[3])

def calc_total_payroll(input_list):
    """
    Prints total payroll of given list of employees if not empty
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return only prints total payroll
    """
    if check_list_not_empty(input_list): return
    total_payroll = 0.0
    for emp_list in input_list:
        total_payroll += emp_list[2] * emp_list[3]
    print('Total Payroll = ', round(total_payroll, 2))

def calc_hours_to_binary(input_list):
    """
    Converts a given Employee's hours to binary
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return only prints Employee Hours to Binary
    """
    if check_list_not_empty(input_list): return
    emp_list = find_employee(input_list)
    hours = int(emp_list[2])
    print("Binary Conversion for values left of decimal: ")
    print( "Binary Value of Hours: ", bin(hours))
    

def bitwise_shift(input_list):
    """
    Perfoms a bitwise shift left and right of given Employee's hours
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return only prints Employee hours shifted left and right
    """
    if check_list_not_empty(input_list): return
    emp_list = find_employee(input_list)
    shifted_left = int(emp_list[2]) << 2
    shifted_right = int(emp_list[2]) >> 2
    print('Ignoring Values right of Decimal: ')
    print('Hours shifted Left 2: ', shifted_left)
    print('Hours shifted Right 2: ', shifted_right)
    

def bitwise_and(input_list):
    """
    Perfoms a bitwise and on two given employee Ids
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return only prints bitwise AND of Employee hours one and two 
    """
    if check_list_not_empty(input_list): return
    print('Choose Employee 1 hours: ')
    emp_list_1 = find_employee(input_list)
    hours_int_1 = int(emp_list_1[2])
    print('Choose Employee 2 hours: ')
    emp_list_2 = find_employee(input_list)
    hours_int_2 = int(emp_list_2[2])
    hours_and = hours_int_1 & hours_int_2
    print('Ignoring Values right of Decimal: ')
    print('Hours 1 bitwise AND Hours 2: ', hours_and)
    
def bitwise_or(input_list):
    """
    Perfoms a bitwise non-exclusive or on two given employee Ids
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return only prints bitwise OR of Employee hours one and two 
    """
    if check_list_not_empty(input_list): return
    print('Choose Employee 1 hours: ')
    emp_list_1 = find_employee(input_list)
    hours_int_1 = int(emp_list_1[2])
    print('Choose Employee 2 hours: ')
    emp_list_2 = find_employee(input_list)
    hours_int_2 = int(emp_list_2[2])
    hours_or = hours_int_1 | hours_int_2
    print('Ignoring Values right of Decimal: ')
    print('Hours 1 bitwise OR Hours 2: ', hours_or)
    
def user_exit(input_list):
    """
    Exit Function to be called from main menu
    
    Args:
        input_list (List): List of Lists of employee information.

    Returns:
        no return only exits 
    """
    print("Exiting Employee MGMT")
    exit()

def single_integer_check_loop ( input_value, approved_values ):
    """
    Checks the input value is a valid integer in given approved values
    if not valid input user is re-prompted
    
    Args:
        input_value (string): user input string.
        approved_values (list): list of approved values to check against input.

    Returns:
        entry_int (integer): converted Integer  
    """
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

def handle_menu_select(input_array):
    """
    Manages Menu Selection in primary loop 
    
    Args:
        input_array (List): List of Lists of employee information.

    Returns:
        no return executes given function chosen by user
    """
    print(*main_menu.keys(), sep='\n')
    user_select = custom_user_entry("Choose Menu Option: ")
    user_select = single_integer_check_loop(user_select,[1,2,3,4,5,6,7])
    menu_list = list(main_menu.keys())    
    menu_text = menu_list[user_select -1]

    if user_select == 6:
        print(*bitwise_menu.keys(), sep='\n')
        user_select = custom_user_entry("Choose Bitwise Option: ")
        user_select = single_integer_check_loop(user_select,[1,2,3])
        menu_list = list(bitwise_menu.keys())
        menu_text = menu_list[user_select -1]
        bitwise_menu[menu_text](input_array)
    else:
        main_menu[menu_text](input_array)

# menus for bitwise
bitwise_menu = {
    "1: Shift" : bitwise_shift,
    "2: Non-Exclusive OR" : bitwise_or,
    "3: AND" : bitwise_and
}
# main menu for Employee Functions
main_menu = {
    "1: Add Employee": add_employee,
    "2: Remove Employee": remove_employee,
    "3: View All Employees": view_all_employees,
    "4: Calculate Total Payroll": calc_total_payroll,
    "5: Convert Hours to Binary": calc_hours_to_binary,
    "6: Bitwise Menu": bitwise_menu,
    "7: Quit": user_exit
}

# initializes list for Primary function
main_list = []

print("******Welcome to Employee Management Tool******")
print("      To exit at any time type: Quit")
print("      Please Choose a number from the following options:")

user_done = False
while not user_done:
    handle_menu_select(main_list)
    and_another = custom_user_entry("Would you like to continue yes/no: ")
    if and_another.lower() == "yes":
        user_done = False
        print("Please Choose a number from the following options or Quit to Exit:")
    elif and_another.lower() == "no":
        user_done = True
    else:
        while and_another.lower() not in ["yes", "no"]:
            and_another = custom_user_entry("Please enter 'yes' or 'no': ")
