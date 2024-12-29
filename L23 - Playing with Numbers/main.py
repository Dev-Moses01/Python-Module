number = int(input("Enter the number to check: "))

original_number = number
reversed_string = str(number)[::-1]
reversed_number = int(reversed_string)
print(reversed_number)
if original_number == reversed_number:
    print("This is a palindrome number")
else:
    print("This is not a palidrome number")

# print("martin"[::-1])

number_large = int(input("Enter the large number to check: "))
number_small = int(input("Enter the small number to check: "))

while  number_small !=0:
    number_large, number_small = number_small, number_large % number_small
    print(number_large)