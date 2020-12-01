import random

lives = 9
words = ['rocky', 'james', 'robin','tyler']
secret_word = random.choice(words)
clue = list('?????')
square_symbol = u'\u2B1C'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives left:' + square_symbol * lives)
    guess = input('Guess a letter or whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a live')
        lives = lives - 1

if guessed_word_correctly:
    print('You are right! The heroes was ' + secret_word)
else:
    print('You are wrong! The heroes was ' + secret_word)
