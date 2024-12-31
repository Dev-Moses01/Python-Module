def binary_to_decimal():
    binary_code = input("Enter a binary number (only 0s and 1s): ")
    try:
        decimal = int(binary_code, 2)
        print(f"The decimal equivalent of binary {binary_code} is {decimal}.")
    except ValueError:
        print("Invalid binary number. Please enter a valid binary code (only 0s and 1s).")

binary_to_decimal()
