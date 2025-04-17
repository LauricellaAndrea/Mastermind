import random

def generate_secret_sequence(length):
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:length]

def get_user_input(length):
    while True:
        user_input = input(f"Enter a number with {length} different digits: ")
        if len(user_input) == length and len(set(user_input)) == length and user_input.isdigit():
            return [int(i) for i in user_input]
        else:
            print(f"You must enter exactly {length} different digits.")

def check_guess(secret, guess):
    correct = 0
    wrong_position = 0

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            correct += 1
        elif guess[i] in secret:
            wrong_position += 1

    return correct, wrong_position

def mastermind():
    sequence_length = 4
    max_attempts = 10
    secret = generate_secret_sequence(sequence_length)

    print("Welcome to Mastermind!")
    print(f"Guess the sequence of {sequence_length} different digits.")

    for attempt in range(max_attempts):
        user_guess = get_user_input(sequence_length)
        correct, wrong_position = check_guess(secret, user_guess)

        if correct == sequence_length:
            print("Congratulations! You've won!")
            return
        else:
            print(f"{correct} correct and {wrong_position} in the wrong position. Try again.")

        if attempt == max_attempts - 1:
            print(f"You've run out of attempts! The secret sequence was: {secret}")

if __name__ == "__main__":
    mastermind()
