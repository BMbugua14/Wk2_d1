#task1
#Answer1
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
#Answer2
def select_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Enter a valid numbers.")
#answer3
def select_operation():
    while True:
        operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
        if operation in ["add", "subtract", "multiply", "divide"]:
            return operation
        else:
            print("Enter a valid operation.")

def calculate():
    num1, num2 = select_numbers()
    operation = select_operation()

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)

    print(f"The result of the {operation} operation is: {result}")

calculate()

#Task2
#Answer1
shopping_list = []
def add_item(shopping_list):
    item = input("What would you like to add to the shopping list? ")
    shopping_list.append(item)
    print(f"You have added {item} to your list.")
#Answer2
def remove_item(shopping_list):
    item = input("What would you like to remove from the shopping list? ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your list.")
    else:
        print(f"{item} is not in your list.")
#Answer3
def print_list(shopping_list):
    if shopping_list:
        print("Your shopping list contains:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is currently empty.")

def main():
    
    while True:
        print("\nShopping List Menu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View shopping list")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            print_list(shopping_list)
        elif choice == "4":
            print("Come Again!")
            break
        else:
            print("Please choose a valid option.")

main()