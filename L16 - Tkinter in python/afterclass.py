import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter the length of the password: "))
password = ''.join(random.choices(characters, k=length))
if length < 8:
    print("Your password length is too short, else it is not safe and secured")
else:
    print("Your password is:", password)