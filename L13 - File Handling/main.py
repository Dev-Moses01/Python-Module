#r = read, w = write (and it removes everything, it can also open a new txt file), a = append
moses = open("moses.txt", "r")
print(moses.read())
moses.close()
moses = open("moses.txt", "w")
moses.write("I am into python")
moses.close()
moses = open("moses.txt", "a")
moses.write("I love solving problems also")
moses.close()