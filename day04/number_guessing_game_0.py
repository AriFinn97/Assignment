import random
think = random.randint(1,21)
guess = int(input("pick a number between 1-20"))
if guess > think:
    print (f"your number is too high{think}")
elif guess < think:
    print (f"your number is too low{think}") 
else:
    print (f"yay you guessed the right number {think}")
         
