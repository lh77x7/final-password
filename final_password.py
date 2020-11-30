import random

atempts = 7

# heroes = ['Rocky Balboa', 'James Bond', 'Han Solo',
#'Robin Hood', 'Superman', 'Maximus',
#'Legolas', 'Batman', 'Wolverine',
#'Forest Gump', 'Iron Man', 'Jack Sparrow',
#'Indiana Jones', 'Tyler Durden', 'Captain America',
#'Luke Skywalker'
# ]

#names of heroe's == 5
heroes = ['rocky', 'james',
'robin','tyler'
]

title = random.choice(heroes)
clue = list('?????')
square_symbol = u'\u2B1C'

guessed_word_correctly = False

def update_clue(guessed_letter, title, clue):
    index = 0
    while index<len(title):
        if guessed_letter == title[index]:
            clue[index] = guessed_letter
        index += 1

while atempts > 0:
    print(clue)
    print('Attempts left:' + square_symbol * atempts)
    guess=input('Guess letter or whole word: ')

    if guess == title:
        guessed_word_correctly = True
        break

    if guess in title:
        update_clue(guess, title, clue)
    else:
        print('Incorrect. You lose an atempt')
        atempts -= 1

if guessed_word_correctly:
    print('You are right! The heroes was ' + title)
else:
    print('You are wrong! The heroes was ' + title)
