# AS05
# Hangman

import random

def man(strikes):
    if strikes == 0:
        print(" /---|")
        print(" |   |")
        print(" |    ")
        print(" |    ")
        print("_|_   ")
    elif strikes == 1:
        print(" /---|")
        print(" |   O")
        print(" |    ")
        print(" |    ")
        print("_|_   ")
    elif strikes == 2:
        print(" /---|")
        print(" |   O")
        print(" |   |")
        print(" |    ")
        print("_|_   ")
    elif strikes == 3:
        print(" /---|")
        print(" |   O")
        print(" |  /|")
        print(" |    ")
        print("_|_   ")
    elif strikes == 4:
        print(" /---|")
        print(" |   O")
        print(" |  /|\ ")
        print(" |    ")
        print("_|_   ")
    elif strikes == 5:
        print(" /---|")
        print(" |   O")
        print(" |  /|\ ")
        print(" |  /  ")
        print("_|_   ")
    else:
        print(" /---|")
        print(" |   O")
        print(" |  /|\ ")
        print(" |  / \ ")
        print("_|_   ")


wordlist = ["tree", "sky", "computer", "apple", "stapler", "fan"]
strikes = 0
alreadyguessed = []

word = list(random.choice(wordlist))
display = list(("_" * len(word)))

while True:
    print("".join(display))
    print(alreadyguessed)
    guess = input("What letter will you guess?")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = word[i]
    else:
        print("That was incorrect\n")
        strikes = strikes + 1
        alreadyguessed.append(guess)
    man(strikes)
    if strikes > 5:
        print("You Lose!")
        print(f"The word was: {''.join(word)}")
        break
    if display == word:
        print("You Win!")
        print(f"The word was: {''.join(word)}")
        break
