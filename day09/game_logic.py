import random

def generate_number(low=1, high=20):
    """Return a random number between low and high (inclusive)."""
    return random.randint(low, high)

def toggle_mode(current):
    """Flip a boolean value (True becomes False, False becomes True)."""
    return not current

def move_number(current, low=1, high=20):
    """Randomly adjust the number by -1, 0, or +1, staying within bounds."""
    change = random.choice([-1, 0, 1])
    new = current + change
    return max(low, min(high, new))

def check_guess(guess, secret):
    """
    Compare guess to secret:
    - returns -1 if guess is too low
    - returns 1 if guess is too high
    - returns 0 if correct
    """
    if guess < secret:
        return -1
    elif guess > secret:
        return 1
    else:
        return 0

