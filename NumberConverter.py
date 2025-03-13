# Function to convert decimal to binary
def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

# Function to convert binary to decimal
def binary_to_decimal(binary_number):
    try:
        return int(binary_number, 2)
    except ValueError:
        return "Invalid Binary Input"

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:]

# Function to convert hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal_number):
    try:
        return int(hexadecimal_number, 16)
    except ValueError:
        return "Invalid Hexadecimal Input"

# Main menu and user input loop
def main():
    while True:
        print("Select the conversion option:")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Decimal to Hexadecimal")
        print("4. Hexadecimal to Decimal")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            # Decimal to Binary
            decimal = int(input("Enter a decimal number: "))
            print(f"Decimal {decimal} to Binary is: {decimal_to_binary(decimal)}")
        
        elif choice == '2':
            # Binary to Decimal
            binary = input("Enter a binary number: ")
            print(f"Binary {binary} to Decimal is: {binary_to_decimal(binary)}")
        
        elif choice == '3':
            # Decimal to Hexadecimal
            decimal = int(input("Enter a decimal number: "))
            print(f"Decimal {decimal} to Hexadecimal is: {decimal_to_hexadecimal(decimal)}")
        
        elif choice == '4':
            # Hexadecimal to Decimal
            hexadecimal = input("Enter a hexadecimal number: ")
            print(f"Hexadecimal {hexadecimal} to Decimal is: {hexadecimal_to_decimal(hexadecimal)}")
        
        elif choice == '5':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the main function to start the program
if __name__ == "__main__":
    main()