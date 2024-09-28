# for m in range(1,10+1):
#     print(5 * m)
# # for k in "Moses":
# #     print(k)

# fruits = ['apple', 'watermelon', 'strawberry']
# adj = ['sweet', 'juicy', 'tasty']
# for i in fruits:
#     for m in adj:
#         print(m,i)

#assignment
def is_armstrong_number(num):
    digits = str(num)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == num

user_input = int(input("Enter a number to check if it is an Armstrong number: "))

if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
