# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is an even number sir")
# else:
#     print("The number is an odd number sir")

# import datetime

# print(datetime.datetime.now())

# import calendar

# print(calendar.calendar(2024))

# age = 100
# if age < 20:
#  print("You are an Underage")
# elif age > 60:
#  print("You are Very Old")
# else:
#  print("You are an Adult")

#Assignment
attendance = int(input("Enter the total number of working days: "))
absent = int(input("Enter the total number of absent days: "))
percent = attendance + absent/100
if percent < 75:
    print("You are not eligible to sit for the exam")
else:
    print("You are eligible to sit for the exam") 