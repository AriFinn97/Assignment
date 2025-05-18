import random
import sys

def main():
    think = random.randint(1, 20)
    debug_mode = False
    print(type(debug_mode))

    while True:
        if debug_mode == True:
            print(f"[DEBUG] Current number to guess: {think}")
        
        guess = input("Guess a number between 1 and 20")

        if guess == "x":
            sys.exit()

        if guess == "s":
            print(f"The number is {think}, don't tell! Shh...")
            continue

        if guess == "d":
            debug_mode = not debug_mode
            print(f"Debug mode {'ON' if debug_mode == False else 'OFF'}")
            continue
        
        guess = int(guess)
        if guess < think:
            print("Your guess is too low.")
        elif guess > think:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed it.")
            break

main()
