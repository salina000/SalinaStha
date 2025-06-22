print(101%2)
num=44
if num % 2==0:
    print("even")
else:
    print("odd")
range(20,31)
for i in range(10,16):
    if i % 2!=0:
        print(i,end=' ')


print(0%2)
import random

a =random.randint(10,50)
user_score = 0
computer_score = 0
ultimate_score = 10
attempts= 0
max_attempts = 5

print(a)



while (True):
        user_input = int(input("Enter a number: "))
        if a == user_input:
        
            print(" You win")
            user_score += 5
            computer_score = -1

            user_play = input("Do you want to play again: ").upper()
            if user_play == ("Y" or "YES"):
                a = random.randint(10,50)
                print(a)

                print(f"Your score: {user_score}, Computer: {computer_score}")

            else:
                break

        else:
            print(" Number does not match.")
            user_score -= 1
            computer_score += 3
        
            print(f"Your score: {user_score}, Computer: {computer_score}")

#to end game
            if user_score >= 10:
                print(" You won the game!")
            elif computer_score>=10:
                print(" You lost.")
            