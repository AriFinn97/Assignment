import random
import sys

def main():
    think = random.randint(1, 20)
    while True:
        guess = input("Guess a number between 1 and 20: ")
        if guess == "s":
            print (f"the nmuber is {think}, dont tell shh")
            continue
        if guess == "x":
          print ("goodbye")
          sys.exit()
        guess = int(guess)
        if guess < think:
            print("Your guess is too low.")
        elif guess > think:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed it.")
            break

main()
