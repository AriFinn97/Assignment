from game_logic import generate_number, toggle_mode, move_number, check_guess

def guessing_game():
    secret = generate_number()
    debug = False
    move = False

    print("Welcome to the Guessing Game!")
    print("Guess a number between 1 and 20.")
    print("Type 'd' to toggle debug mode.")
    print("Type 'm' to toggle move mode.")
    print("Type 'x' to exit.")

    while True:
        if debug:
            print(f"[DEBUG] Secret number is: {secret}")

        guess = input("Your guess: ")

        if guess.lower() == 'x':
            print("Goodbye!")
            break

        if guess.lower() == 'd':
            debug = toggle_mode(debug)
            print("Debug mode enabled." if debug else "Debug mode disabled.")
            continue

        if guess.lower() == 'm':
            move = toggle_mode(move)
            print("Move mode enabled." if move else "Move mode disabled.")
            continue

        try:
            guess_num = int(guess)
            if guess_num < 1 or guess_num > 20:
                print("Guess must be between 1 and 20.")
                continue

            result = check_guess(guess_num, secret)
            if result == -1:
                print("Too low!")
            elif result == 1:
                print("Too high!")
            else:
                print("You got it! ")
                break

            if move:
                secret = move_number(secret)

        except ValueError:
            print("Please enter a number or a valid command.")

if __name__ == "__main__":
    guessing_game()
