num1 = input("Enter the first number")
num2 = input("Enter the second number")
num1, num2 = map(float, (num1, num2))
operation = input("Choose an operation (add, subtract, multiply, divide): ")
match operation:
    case "add":         
        result = num1 + num2
        print(f" The result is {result}")
    case "subtract":
        result = num1 - num2
        print(f" The result is {result}")           
    case "multiply":
        result = num1 * num2
        print(f" The result is {result}")
    case "divide":
        if num2 != 0:
            result = num1 / num2
            print(f" The result is {result}")
        else:
            print(" Division by zero is not allowed.")