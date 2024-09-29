# age = 15
# def intro():
#     name = 'Moses'
#     print("I am Him " + name)

# def outro():
#     print("Goodbye Bwoi")
#     print(age)

# intro()
# outro()

# def add(x,y):
#     return x + y
# def multiply(x,y):
#     return x * y
# def divide(x,y):
#     return x / y
# def sub(x,y):
#     return x - y

# print(add(5,5))
# print(multiply(5,5))
# print(int(divide(5,5)))
# print(sub(5,5))
#Assignment

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for m in range(n):
        series.append(a)
        a, b = b, a + b
    return series

num_terms = int(input("Enter the number of terms:- "))
print(fibonacci_series(num_terms))