# Calculator

active = True

while active:
    try:

        # Prompts user and places the string into a list "components"

        expression = input("Enter an expression:")

        components = expression.split()

        # Determines if the input is less than or equal to 3, allows for spaces within the expression

        if len(components) !=  3 or len(components) < 3:
            components = " ".join(expression)
            components = components.split()
        
        num1, operator, num2 = components
        num1 = int(num1)
        num2 = int(num2)

        # Operations: Addition, Subtration, Mutiplication, & Division

        if operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            raise ValueError("Invalid operator. Use one of: * + - /")
        
        print(f"Result: {result}")
        break
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except ZeroDivisionError:
        print("Error: Division by zero error. Try again.")