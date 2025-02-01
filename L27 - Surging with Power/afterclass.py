import math

def ispowerof8(n):
    return n > 0 and (n & (n-1)) == 0 and (n-1) % 7 == 0

num = int(input("Enter a number to check: "))

print(f"Is {num} a power of 8? {ispowerof8(num)}")