from math import sqrt
number = int(input("Enter the number to check: "))

for i in range(2, int(sqrt(number))+1):
    if (number % i) == 0:
        print("This is not a prime number")
        break
else:
        print("This is a prime number")