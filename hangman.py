from random import choice

print("""H A N G M A N""")
words = ['python', 'java', 'kotlin', 'javascript']
word = choice(words)
word_shown = f'{"-" * (len(word))}'

TRIES = 8
GUESSES = ''
menu = input('Type "play" to play the game, "exit" to quit:')
if menu == 'play':
    pass
elif menu == 'exit':
    exit()


while True:
    if TRIES == 0:
        print("You lost!")
        break

    while True:
        ui = input(f'\n{word_shown}\nInput a letter: ')
        if len(ui) != 1:
            print('You should input a single letter')
        elif not ui.islower():
            print("Please enter a lowercase English letter")
        elif ui in GUESSES:
            print("You've already guessed this letter")
        else:
            break

    GUESSES += ui

    if ui in word:
        for idx, letter in enumerate(word):
            if letter == ui:
                word_shown = word_shown[:idx] + letter + word_shown[idx+1:]
        if '-' not in word_shown:
            print('You guessed the word!\nYou survived!')
            break
    else:
        print("That letter doesn't appear in the word")
        TRIES -= 1
