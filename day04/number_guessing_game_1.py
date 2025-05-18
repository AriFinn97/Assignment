import random

def main():
    think = random.randint(1, 21)
    while True:
        guess = int(input("Guess a number between 1 and 20: "))
        if guess < think:
            print("Your guess is too low.")
        elif guess > think:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed it.")
            break

main()
