from random import choice


def update_guess(secret, letter, guess):
    for i in range(len(secret)):
        if secret[i] == letter:
            guess = guess[:i] + letter + guess[i+1:]
    return guess

print("Guess The Word!!!")
print("Welcome to GTW!")
secret_choice = ["bicicle", "banana", "unicycle", "jack-o-lantern", "ice", "cream", "one", "everything", "nothing", "invincibility", "hangman", "peeled", "baking", "popping", "master", "magic", "jumping", "trampoline", "octopus", "thousand", "unboxing", "makeover", "zebra", "yoga", "lolipop"]
secret = choice(secret_choice)
length = len(secret)
guess = "-" * length
print(guess)
while guess != secret:
    print("Type in a letter or a whole word.")
    player_guess = input()
    if player_guess == secret:
        print("You got the whole word!")
        break
    elif player_guess in secret:
        print("Yesss!")
        guess = update_guess(secret, player_guess, guess)
        print(guess)
    else:
        print("Misunderstood or no letter.")
