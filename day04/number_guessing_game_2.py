import random

def main():
    think = random.randint(1, 20)
    while True:
        guess = input("Guess a number between 1 and 20: ")
        if guess == "x":
          break
        guess = int(guess)
        if guess < think:
            print("Your guess is too low.")
        elif guess > think:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed it.")
            break

main()
