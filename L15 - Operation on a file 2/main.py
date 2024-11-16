with open("moses.txt", "r") as file:
    print(file.read())
    file.close()\
    
with open("moses.txt", "w") as file:
    file.write("I am still Moses, don't be scared!!")
    file.close()

with open("moses.txt", "a") as file:
    file.write(" Are you happy now?")
    file.close()

with open("moses.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# file = open("mo.txt", "x")

import os
os.remove("mo.txt")