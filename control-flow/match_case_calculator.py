num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1, num2 = map(float, (num1, num2))
operation = input("Choose an operation (+, -, * , /): ")
match operation:
    case "+":
        result = num1 + num2
        print(f" The result is {result}")
    case "-":
        result = num1 - num2
        print(f" The result is {result}")
    case "*":
        result = num1 * num2
        print(f" The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f" The result is {result}")
        else:
            print(" Division by zero is not allowed.")