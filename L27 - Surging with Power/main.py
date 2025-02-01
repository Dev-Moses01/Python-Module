import math

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

def is_power_of_4(n):
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

def is_logarithmic(n):
    return n > 0 and math.log(n, 2).is_integer()

num = int(input("Enter a number: "))

print(f"Is {num} a power of 2? {is_power_of_2(num)}")
print(f"Is {num} a power of 4? {is_power_of_4(num)}")
print(f"Is {num} following O(log n) pattern? {is_logarithmic(num)}")