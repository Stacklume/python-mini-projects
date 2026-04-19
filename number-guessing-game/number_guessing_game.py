import random
logo="""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|     """
print(logo)
print("Welcome to the Number Guessing Game!I'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts=0
num=random.randint(1,100)
print(num)
guess=int(input("Make a guess: "))


if difficulty=="easy":
    attempts=10
elif difficulty=="hard":
    attempts=5

if guess==num:
    print(f"You got it! The answer was {num}.")

while guess!=num:
    if guess>num:
        print("Too high.")
    else:
        print("Too low.")
    attempts-=1
    if attempts==0:
        print("You've run out of guesses, you lose.")
        break
    else:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))