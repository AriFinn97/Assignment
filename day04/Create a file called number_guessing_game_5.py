import random
import sys

def main():
    think = random.randint(1, 20)
    debug_mode = False
    moving_mode = False

    print(type(debug_mode))

    while True:
        if debug_mode == True:
            print(f"[DEBUG] Current number to guess: {think}")
        
        guess = input("Guess a number between 1 and 20")

        if moving_mode == True:
                think += random.choice([-2,-1,0,1,2])
                think = max(1,min(20,think))

        if guess == "x":
            sys.exit()

        if guess == "m":
            moving_mode = not moving_mode
            print (f"moving mode is{ ' on' if moving_mode else ' off'}")
            continue  

        if guess == "s":
            print(f"The number is {think}, don't tell! Shh...")
            print (moving_mode)
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
