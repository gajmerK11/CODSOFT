# Calculator

print("-----------------Calculator--------------")

while True:
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        operation_choice = input("Enter the operation choice (+, -, *, /) or 'q' to quit: ")

        #function to format output based on input types
        def format_result(result):
            if first_number.is_integer() and second_number.is_integer():
                return int(result)
            return result

        if operation_choice == "+":
            sum_result = first_number + second_number
            print(f"The sum of given numbers is {format_result(sum_result)}")
        elif operation_choice == "-":
            difference = first_number - second_number
            print(f"The difference of given numbers is {format_result(difference)}")
        elif operation_choice == "*":
            product = first_number * second_number
            print(f"The product of given numbers is {format_result(product)}")
        elif operation_choice == "/":
            if second_number != 0:
                division = first_number / second_number
                print(f"The division of given numbers is {format_result(division)}")
            else:
                print("Division by zero is not allowed.")
        elif operation_choice.lower() == "q":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Please enter a valid operation choice.")

    except ValueError:
        print("Invalid input! Please enter numeric values for numbers.")

    print("-----------------------------------------")
