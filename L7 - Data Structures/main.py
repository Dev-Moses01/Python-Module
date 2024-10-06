# name = ["Moses", "Kate", "Isreal", "David"]
# print(name)
# name.sort()
# print(name)
# name.reverse()
# print(name)
# name.append("Sonia")
# print(name)
# name.pop(3)
# print(name)
# numbers = [36, 12, 40, 7, 100, 2, 74]
# print(numbers)
# numbers.sort()
# print(numbers)

# student1 = {
#     "name": 'Moses',
#     "school": 'Codingal',
#     "about": 'Chill'
# }
# student1["name"] = 'Boss'
# student1["hobbies"] = 'Problem-solving'
# student1.pop("school")
# print(student1)
# print(student1["name"])

#After-Class Project
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
            
            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
