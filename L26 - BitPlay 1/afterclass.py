def find_rightmost_set_bit(num):
    if num == 0:
        return "No set bits, as the number is zero."
    
    position = 1
    while (num & 1) == 0:
        num = num >> 1
        position += 1
    
    return position

# Input from the user
try:
    number = int(input("Enter a number: "))
    result = find_rightmost_set_bit(number)
    print(f"The rightmost set bit is at position: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")
