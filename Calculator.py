import math
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function calculates the square root of a number
def square_root(x):
    return math.sqrt(x)

# This function calculates x raised to the power y
def power(x, y):
    return math.pow(x, y)

# This function calculates the sine of a number
def sin(x):
    return math.sin(math.radians(x))

# This function calculates the cosine of a number
def cos(x):
    return math.cos(math.radians(x))

# This function calculates the tangent of a number
def tan(x):
    return math.tan(math.radians(x))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square Root")
print("6.Power")
print("7.Sin")
print("8.Cos")
print("9.Tan")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

    # check if choice is one of the available options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        try:
            # For sin, cos, tan, and square root, we only need one input
            if choice in ('5', '7', '8', '9'):
                num1 = float(input("Enter the number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print("Square root of", num1, "=", square_root(num1))
        
        elif choice == '6':
            print(num1, "raised to the power of", num2, "=", power(num1, num2))

        elif choice == '7':
            print("Sin of", num1, "degrees =", sin(num1))

        elif choice == '8':
            print("Cos of", num1, "degrees =", cos(num1))

        elif choice == '9':
            print("Tan of", num1, "degrees =", tan(num1))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")