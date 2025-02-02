a = 10
b = 7

temp = a
a = b
b = temp
print(a, b)

x = 3
y = 5

x = x + y #3+5=8=x
y = x - y #8-5=3=y
x = x - y #8-3=5=x
print(x, y)

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("after swapping a =", a,"b = ", b)

swap(10, 100)