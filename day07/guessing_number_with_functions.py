import random

def generate_secret_number():
    return random.randint(1, 10)

def get_user_guess():
    user_input = input("Guess a number between 1 and 10: ")
    return int(user_input)

def check_guess(secret_number, guess):
    return guess == secret_number

def show_result(is_correct, secret_number):
    if is_correct:
        print("That's the number!")
    else:
        print("Try again!")

def run_game():
    secret_number = generate_secret_number()
    while True:
        guess = get_user_guess()
        is_correct = check_guess(secret_number, guess)
        show_result(is_correct, secret_number)
        if is_correct:
            break

if __name__ == "__main__":
    run_game()
