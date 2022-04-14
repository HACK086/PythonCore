import random

print('H A N G M A N')
print()
words = ['python', 'java', 'swift', 'javascript']
word = random.choice(words)


win = 0
lose = 0
count5=0
while count5 == 0:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if command == 'play':
        attempts = 8
        wrong_choices = []
        encrypted = len(word) * '-'
        while attempts > 0:
            print(encrypted)
            print('Input a letter: ')
            letter = input()
            if len(letter) > 1 or len(letter) == 0:
                print('Please, input a single letter.')
            if letter.islower() is False and len(letter) != 0:
                print('Please, enter a lowercase letter from the English alphabet.')
            if (letter in encrypted or letter in wrong_choices) and len(letter) != 0:
                print('You\'ve already guessed this letter.')
                continue
            if letter not in word and letter.islower() is True and len(letter) == 1:
                print("That letter doesn't appear in the word.")
                wrong_choices.append(letter)
                attempts -= 1
            if letter in word:
                i = 0
                while i < len(word):
                    if word[i] == letter:
                        encrypted = encrypted[:i] + letter + encrypted[i + 1:]
                    i += 1
            if '-' not in encrypted:
                print(f'You guessed the word {word}!')
                print('You survived!')
                win += 1
                attempts = 0
                break
            if attempts == 0:
                print('You lost!')
                lose +=1
    elif command == 'results':
        print("You won:",win, "times.")
        print("You lost:", lose, "times.")
    elif command == 'exit':
        count5 = 1