import random
#Why there are no comments in the code?
print('Which game would you like to play?')
game = input().lower()
while True:
    if game == 'numbers' or game == "rock-paper-scissors":
        break
    else:
        print('Please choose a valid option: Numbers or Rock-paper-scissors?')
        game = input().lower()
if game == 'numbers':
    goal = random.randint(0, 1000000)
    robotcount = 0
    acount = 0
    Draws = 0
    while True:
        print('What is your number?')
        a = input()
        if a == 'exit game':
            print(f"""You won: {acount},
The robot won: {robotcount},
Draws: {Draws}.""")
            break
        try:
            a = int(a)
            if a < 0:
                print("The number can't be negative!")
            elif a > 1000000:
                print("Invalid input! The number can't be bigger than 1000000.")
            else:
                robot = random.randint(0,1000000)
                print(f"The robot entered the number {robot}.")
                print(f"The goal number is {goal}.")
                if abs(goal - robot) < abs(goal - a):
                    print(f"The robot won!")
                    robotcount += 1
                elif abs(goal - robot) > abs(goal - a):
                    print(f"You won!")
                    acount += 1
                else:
                    print("It's a draw!")
                    Draws += 1
        except:
            print("A string is not a valid input!")
elif game == 'rock-paper-scissors':
    robotlistcount = 5
    drawscount = 0
    yourcount = 0
    while True:
        robotlist = ['rock','paper','scissors']
        rand = random.randint(0,2)
        print("What is your move?")
        your = input().lower()
        if your == 'exit game':
            print(f"""You won: {yourcount},
The robot won: {robotlistcount},
Draws: {drawscount}.""")
            break
        elif your == 'rock' and robotlist[rand] == 'scissors' or your == 'scissors' and robotlist[rand] == 'paper' or your == 'paper' and robotlist[rand] == 'rock':
            print(f"The robot chose {robotlist[rand]}")
            print("You won!")
            yourcount += 1
        elif your == 'scissors' and robotlist[rand] == 'rock' or your == 'rock' and robotlist[rand] == 'paper' or your == 'paper' and robotlist[rand] == 'scissors':
            robotlistcount += 1
            print(f"The robot chose {robotlist[rand]}")
            print("The robot won!")
        elif your == 'paper' and robotlist[rand] == 'paper' or your == 'rock' and robotlist[rand] == 'rock' or your == 'scissors' and robotlist[rand] == 'scissors':
            drawscount += 1
            print(f"The robot chose {robotlist[rand]}")
            print("It's a draw!")
        else:
            print("No such option! Try again!")



