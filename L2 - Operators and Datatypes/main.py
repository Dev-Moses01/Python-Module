# Function to swap three numbers
def swap_three_numbers(a, b, c):
    return c, a, b  # Swapping in the order of c, a, b

# Main function to execute the program
def main():
    # Taking input from the user
    print("Enter three numbers:")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    
    # Swapping the numbers
    a, b, c = swap_three_numbers(a, b, c)
    
    # Displaying the swapped numbers
    print("After swapping:")
    print("First number:", a)
    print("Second number:", b)
    print("Third number:", c)

# Run the program
if __name__ == "__main__":
    main()













# name = "Moses" #string
# age = 18 #integers
# height = 5.2 #float
# is_student = True #boolean
# print(age)
# print("20" + "20")
# x = 20
# y = 20
# print(int(x) + int(y))
# name = bool(name)
# print(name)
# print(type(name))

# num1 = 10
# num2 = 20

# print(num1 + num2)
# print (num1 - num2)
# print (num1 / num2)
# print (num1 * num2)
# print (num1 ** 2)
# print (num2 ** 0.5)
# print (num1 > num2)
# print (num1 < num2)
# print (num1 == num2)
# print (num1 != num2)