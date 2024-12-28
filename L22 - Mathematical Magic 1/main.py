#Armstrong number
number = int(input("Enter the number to check: "))
length = len(str(number))

result = 0
temp = number

while temp != 0:
    digit = temp % 10
    result += digit ** length
    temp = temp // 10

if number == result:
    print("This is an armstrong number")
else:
    print("This is not an armstrong number")


def factors(n):
    for i in range(1, n+1):
        if(n % i == 0):
            print(i)

factors(144)