# shopping list app for CS1
# 1. Add an item to the list
# 2. Remove an item from the list
# 3. View all items in the list
# 4. Clear the entire list
# 5. Show the total cost 
# 6. Exit the application
# simple list managment didnt use the dictionary this time because it seemed overkill for this application
# each item is a tuple of (item_name, quantity, cost, total_cost) seemed more appropriate then multiple lists and tracking location of each
# kept with exit check command throughout because I liked that flow and felt fitting
# added user_continue function to give user a break between operations felt like a better user experience then immediately popping back to menu


# display menu function
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add an item to the list")
    print("2. Remove an item from the list")
    print("3. View all items in the list")
    print("4. Clear the entire list")
    print("5. Show the total cost")
    print("6. Exit the application")
    choice = custom_user_entry("Please select an option (1-6): ")
    return choice

# checks for exit command
def exit_check ( input_value ):
    if input_value.lower() == "quit":
        print("Goodbye!!")
        exit()

# used to always check for exit command
def custom_user_entry( input_message ):
    input_value = input(input_message)
    exit_check( input_value )
    return input_value

# adds item to list with cost and quantity with calculation of total cost
def add_item(shopping_list):
    item = custom_user_entry("Enter the item name: ")
    try:
        cost = float(custom_user_entry("Enter the item cost: "))
        quantity = int(custom_user_entry("Enter the quantity: "))
        total_cost = round(cost * quantity, 2)
        shopping_list.append((item, quantity, cost, total_cost))
        print(f"{item} added to the list.")
    except ValueError:
        print("Invalid cost or quantity. Please enter numeric values.")

# removes item from list
def remove_item(shopping_list):
    item = custom_user_entry("Enter the item name to remove: ")
    for i, (name, quantity, cost, total_cost) in enumerate(shopping_list):
        if name == item:
            shopping_list.remove((name, quantity, cost, total_cost))
            print(f"{item} removed from the list.")
            return
    print(f"{item} not found in the list.")

# views all items in list with details
def view_items(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\nShopping List Items:")
        for item, quantity, cost, total_cost in shopping_list:
            print(f"- {item} (Quantity: {quantity}, Unit Cost: ${cost}), Total Cost: ${total_cost}")

# clears the entire list
def clear_list(shopping_list):
    shopping_list.clear()
    print("The shopping list has been cleared.")

# shows the total cost of all items in the list
def show_total_cost(shopping_list):
    total = 0
    for item, quantity, cost, total_cost in shopping_list:
        total += total_cost
    print(f"The total cost of items in the list is: ${total}")

# prompts user to continue or exit the application, gives break between operations
def user_continue():
    choice = custom_user_entry("Press any key to continue or type 'no' to exit: ")
    if choice.lower() == 'no':
        print("Exiting the application. Goodbye!")
        exit()

# main program loop starts here
print("Welcome to the Shopping List Application!")
print("   To exit at any time type: Quit")
shopping_list = []
# main loop to handle user selections 
while True:
    choice = display_menu()
    if choice == '1':
        add_item(shopping_list)
        user_continue()
    elif choice == '2':
        remove_item(shopping_list)
        user_continue()
    elif choice == '3':
        view_items(shopping_list)
        user_continue()
    elif choice == '4':
        clear_list(shopping_list)
        user_continue()
    elif choice == '5':
        show_total_cost(shopping_list)
        user_continue()
    elif choice == '6':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
