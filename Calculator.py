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

# This function calculates the logarithm (base 10) of a number
def log(x):
    return math.log10(x)

# This function calculates the natural logarithm (base e) of a number
def ln(x):
    return math.log(x)

# This function calculates the factorial of a number
def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers"
    elif x == 0 or x == 1:
        return 1
    else:
        return math.factorial(int(x))

# This function calculates the degree to radian conversion
def degrees_to_radians(x):
    return math.radians(x)

# This function calculates the radian to degree conversion
def radians_to_degrees(x):
    return math.degrees(x)

# This function calculates the permutation (nPr)
def permutation(n, r):
    if n >= r >= 0:
        return math.perm(n, r)
    else:
        return "Invalid input for permutation. Ensure n >= r >= 0."
    
# This function calculates the combination (nCr)
def combination(n, r):
    if n >= r >= 0:
        return math.comb(n, r)
    else:
        return "Invalid input for combination. Ensure n >= r >= 0."

# This function calculates the absolute value of a number
def absolute(x):
    return abs(x)

# This function calculates the greatest common divisor (GCD)
def gcd(x, y):
    return math.gcd(x, y)

# This function calculates the least common multiple (LCM)
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)
  
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
print("10.Logarithm (base 10)")
print("11.Natural Logarithm (base e)")
print("12.Factorial")
print("13.Degrees to Radians")
print("14.Radians to Degrees")
print("15.Permutation (nPr)")
print("16.Combination (nCr)")
print("17.Absolute Value")
print("18.Greatest Common Divisor (GCD)")
print("19.Least Common Multiple (LCM)")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19): ")

    # check if choice is one of the available options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'):
        try:
            # For sin, cos, tan, square root, log, ln, factorial, and degree/radian conversions, we only need one input
            if choice in ('5', '7', '8', '9', '10', '11', '12', '13', '14', '17', '18', '19'):
                num1 = float(input("Enter the number: "))
            elif choice in ('15', '16'):
                num1 = int(input("Enter n: "))
                num2 = int(input("Enter r: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
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

        elif choice == '10':
            print("Logarithm (base 10) of", num1, "=", log(num1))
        
        elif choice == '11':
            print("Natural Logarithm (base e) of", num1, "=", ln(num1))

        elif choice == '12':
            print("Factorial of", num1, "=", factorial(num1))

        elif choice == '13':
            print(num1, "degrees =", degrees_to_radians(num1), "radians")

        elif choice == '14':
            print(num1, "radians =", radians_to_degrees(num1), "degrees")

        elif choice == '15':
            print("Permutation (", num1, "P", num2, ") =", permutation(num1, num2))

        elif choice == '16':
            print("Combination (", num1, "C", num2, ") =", combination(num1, num2))

        elif choice == '17':
            print("Absolute value of", num1, "=", absolute(num1))

        elif choice == '18':
            print("GCD of", num1, "and", num2, "=", gcd(num1, num2))

        elif choice == '19':
            print("LCM of", num1, "and", num2, "=", lcm(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

