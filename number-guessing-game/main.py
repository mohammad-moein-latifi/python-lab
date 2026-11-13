import random


MIN_NUMBER = 0
MAX_NUMBER = 100
MAX_ATTEMPTS = 10


def get_valid_guess(attempts_left):
    """Prompt until the user enters a whole number within the allowed range.

    Invalid input does not consume an attempt. Return None if the user
    interrupts input or the input stream is closed.
    """
    while True:
        attempt_label = "try" if attempts_left == 1 else "tries"
        prompt = (
            f"Your guess ({MIN_NUMBER}-{MAX_NUMBER}) "
            f"[{attempts_left} {attempt_label} left]: "
        )

        try:
            user_input = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nNo worries! Game stopped. See you next time!")
            return None

        try:
            guess = int(user_input)
        except ValueError:
            print("Oops! Whole numbers only. No try used.")
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(
                f"Keep it between {MIN_NUMBER} and {MAX_NUMBER}. "
                "No try used."
            )
            continue

        return guess


def play_game():
    """Run one round of the number guessing game."""
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts_used = 0

    print(
        "\n🎯 I've picked a number between 0 and 100. "
        "Can you guess it in 10 tries?\n"
    )

    while attempts_used < MAX_ATTEMPTS:
        attempts_left = MAX_ATTEMPTS - attempts_used
        guess = get_valid_guess(attempts_left)

        if guess is None:
            return

        attempts_used += 1

        if guess == secret_number:
            attempt_label = "guess" if attempts_used == 1 else "guesses"
            print(
                f"🎉 You got it! {secret_number} was the number. "
                f"You nailed it in {attempts_used} {attempt_label}!"
            )
            return

        if guess < secret_number:
            hint = "Too low! Go higher."
        else:
            hint = "Too high! Go lower."

        attempts_left = MAX_ATTEMPTS - attempts_used

        if attempts_left > 0:
            attempt_label = "try" if attempts_left == 1 else "tries"
            print(f"{hint} {attempts_left} {attempt_label} left.")
        else:
            print(f"{hint} 💀 Game over! The number was {secret_number}.")


if __name__ == "__main__":
    play_game()
