import random

atempts = 5
#names of heroe's == 5
heroes = ['rocky', 'james','robin','tyler', 'micky', 'jimmy']
secret_word = random.choice(heroes)
clue = list('?????')
square_symbol = u'\u2B1C'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1

while atempts > 0:
    print(clue)
    print('Attempts left: ' + square_symbol * atempts)
    guess = input('Guess letter or whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose an atempt')
        atempts = atempts - 1

if guessed_word_correctly:
    print('You are right! The heroes was ' + secret_word)
else:
    print('You are wrong! The heroes was ' + secret_word)
