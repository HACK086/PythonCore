import random
# rock - камень
# paper - бумага
# scissors - ножницы
count = 0
with open('C:\\Users\\abfaz\\Desktop\\kkk.txt', 'r') as file:
    rating = {line.split()[0]: int(line.split()[1]) for line in file.readlines()}
name = input('Enter your name: ')
print(f'Hello, {name}')
score = rating.get(name, 0)
if name == 'Tim':
    score = 350
elif name == 'Jane':
    score = 200
elif name == 'Alex':
    score = 400
else :
    score = 0
new_objects = input().split(',')
if len(new_objects) > 2:
    objects = new_objects
print('Okay, let\'s start')
while count == 0:
    a = {1: 'rock', 2: 'paper', 3: 'scissors'}
    b = random.randint(1, 3)
    c = input()
    if c == '!rating':
        print(f'Your rating: {score}')
    elif c == 'rock' and a[b] == 'paper':
        print('Sorry, but the computer chose paper')
    elif c == 'rock' and a[b] == 'scissors':
        print('Well done. The computer chose scissors and failed')
        score = score + 100
    elif c == 'rock' and a[b] == 'rock':
        print("There is a draw (rock)")
        score = score + 50

    elif c == 'paper' and a[b] == 'scissors':
        print('Sorry, but the computer chose scissors')
    elif c == 'paper' and a[b] == 'rock':
        print('Well done. The computer chose rock and failed')
        score = score + 100
    elif c == 'paper' and a[b] == 'paper':
        print("There is a draw (paper)")
        score = score + 50

    elif c == 'scissors' and a[b] == 'rock':
        print('Sorry, but the computer chose rock')
    elif c == 'scissors' and a[b] == 'paper':
        print('Well done. The computer chose paper and failed')
        score = score + 100
    elif c == 'scissors' and a[b] == 'scissors':
        print("There is a draw (scissors)")
        score = score + 50
    elif c == '!exit':
        print('Bye!')
        count = 1
    else:
        print('Invalid input')



