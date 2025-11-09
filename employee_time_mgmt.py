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
    if input_value.lower() == "quit":
        print("Goodbye!!")
        exit()

# used to always check for exit command
def custom_user_entry( input_message ):
    input_value = input(input_message)
    exit_check( input_value )
    return input_value

def add_employee(input_list):
    print('Enter the following information')
    emp_id = int(custom_user_entry('Enter Employee Id: '))
    emp_name = custom_user_entry('Employee Name: ')
    hours_worked = float(custom_user_entry('Hours Worked: '))
    hourly_rate = float(custom_user_entry('Hourly Rate: '))
    input_list.append([emp_id, emp_name, hours_worked, hourly_rate])
    print('Empoyee: ', emp_name, ' added to system')

def find_employee(input_list):
    if check_list_not_empty(input_list): return
    found_emp_id = False
    while not found_emp_id:
        emp_id = int(custom_user_entry('Enter Employee Id: '))
        for emp_list in input_list:
            if emp_list[0] == emp_id:
                return emp_list
        print('Employee Id not found please try again')

def check_list_not_empty(input_list):
    if len(input_list) == 0:
        print('System currently has no employees')
        return True
    return False

def remove_employee(input_list):
    if check_list_not_empty(input_list): return
    emp_list = find_employee(input_list)
    input_list.remove(emp_list)
    print('Employee: ', emp_list[1], ' Removed')

def view_all_employees(input_list):
    if check_list_not_empty(input_list): return
    print('Current employees in system: ')
    for emp_list in input_list:
        print('Employee Id: ', emp_list[0], end=', ')
        print('Employee Name: ', emp_list[1], end=', ')
        print('Hours Worked: ', emp_list[2], end=', ')
        print('Hourly Rate: ', emp_list[3])

def calc_total_payroll(input_list):
    if check_list_not_empty(input_list): return
    total_payroll = 0.0
    for emp_list in input_list:
        total_payroll += emp_list[2] * emp_list[3]
    print('Total Payroll = ', round(total_payroll, 2))

def calc_hours_to_binary(input_list):
    pass

def bitwise_shift(input_list):
    pass

def bitwise_and(input_list):
    pass

def bitwise_or(input_list):
    pass



main_list = []

