with open("sample_file.txt", "r") as file:
    print(file.read())
    file.close()
with open("sample_file.txt", "w") as file:
    file.write("My name is Moses, and I love coding")
    file.close()
with open("sample_file.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
# with open("My_File", "r") as file:
#     print(file.read())
#     file.close()
file = open("My_File", "x")
with open("My_File", "w") as file:
    file.write("My name is Moses, and I love coding")
    file.close()
import os
os.remove("sample_file.txt")