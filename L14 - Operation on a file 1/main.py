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

#After class project
file = open("file.txt", "w")
file.write("I love smiling, \n I love coding, \n I love solving problems.")
file.close()
file = open("file.txt", "r")
for l in file:
    print(l)