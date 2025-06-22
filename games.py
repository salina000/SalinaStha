import random

a = random.randint(10, 50)
print(a)

while True:

    user_input = int(input("enter a number: "))
    if a == user_input:
        print("You win")
        user_play = input("Do you want to play again: ")

        if user_play == "Y":
            a = random.randint(10, 50)
            print(a)
        else:
            break

    else:
        print("Number does not exist.")


# mport random

# a =random.randint(10,50)
# print(a)
# total_attempt = 5
# user_attempt = 0
# while(True):

# user_input = int(input("enter a number: "))
# user_attempt = user_attempt + 1
# if a==user_input:
#   print("You win")
# user_play = input("Do you want to play again: ").upper()

# if user_play == ("Y" or "YES"):
#  a = random.randint(10,50)
# user_attempt = 0
#  print(a)
# else:
# break
# else:
# print("Number doesnot match, please try again.. Remaining attempt", user_attempt)


# if user_attempt == total_attempt:
# print("Total attempt exceeded", "Random number is", a)
#  break


# user correct => 5 points
# computer => 3 points
# user wrong  -1
# user correct computer value should be -1


# 10 point


a = random.randint(10, 50)
user_score = 0
cam_score = 0
ultimate_score = 10
print(a)

while True:

    user_input = int(input("enter a number: "))
    if a == user_input:
        print("You win")
        user_score = +5
        cam_score = -1
        user_play = input("Do you want to play again: ")

        if user_play == ("y"):
            a = random.randint(10, 50)
            print(a)

        else:
            break

    else:
        print("Number doesnot match, try again")
        user_score = -1
        cam_score = +3



import random

user_score = 0
computer_score = 0
attempts = 0
max_attempts = 5

# Random number between 10 and 50
target = random.randint(10, 50)
print(target)
print("Guess the number between 10 and 50")

while user_score < 10 and computer_score < 10:
    if attempts >= max_attempts:
        print(" You have made 5 incorrect guesses. Game Over.")
        break

    try:
        user_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    computer_guess = random.randint(10, 50)
    print(f"Computer guessed: {computer_guess}")

    if user_guess == target:
        user_score += 5
        computer_score -= 1
        print(" You guessed correctly! +5 points")
        target = random.randint(10, 50)
        print(target)

    else:
        user_score -= 1
        attempts += 1
        print("Wrong guess. -1 point")

    if computer_guess == target:
        computer_score += 3
        print("Computer guessed correctly! +3 points")

    print(f"Your score: {user_score} | Computer score: {computer_score}\n")

# Final result
if user_score >= 10:
    print(" You win the game!")
elif computer_score >= 10:
    print(" Computer wins the game!")






    
