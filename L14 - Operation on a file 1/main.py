moses = open("abc.txt", "r")
print(moses.read())
moses.close()
moses = open("abc.txt", "r")
print(moses.readline())
print(moses.readline())
print(moses.readline())
moses.close()
file = open("abc.txt", "r")
for m in file:
    print(m)