import random
import sys
def isnumber():
    while True:
        answer = input()
        if answer.isdigit() or (len(answer) > 0 and answer[0] == "-" and answer[1:].isdigit()):
            yes = int(answer)
            break
        else:
            print("Incorrect format.")
    return yes

def arithmetic():
    operations = ["+", "-", "*"]
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    oper = random.choice(operations)
    # a, oper, b = input().split()
    if oper == "+":
        print(a, oper, b)
        calc = a + b
    elif oper == "-":
        print(a, oper, b)
        calc = a - b
    elif oper == "*":
        print(a, oper, b)
        calc = a * b
    return "Right!" if isnumber() == calc else "Wrong!"

def math_level():
    while True:
        print("""
        Which level do you want? Enter a number:
        1 - simple operations with numbers 2-9
        2 - integral squares of 11-29
        """)
        choice = isnumber()
        if choice in [1, 2]:
            break
        else:
            print("Incorrect format.")
            continue
    return choice

def int_squares():
    c = random.randint(11, 29)
    print(c)
    calc = c ** 2
    return "Right!" if isnumber() == calc else "Wrong!"

def main():
    difficulty = math_level()
    level_description = {1: 'simple operations with numbers 2-9', 2: 'integral squares 11-29'}

    if difficulty == 1:
        count = 1
        n = 0
        while count <= 5:
            x = arithmetic()
            print(x)
            if x == "Right!":
                n += 1
            count += 1
    else:
        count = 1
        n = 0
        while count <= 5:
            x = int_squares()
            print(x)
            if x == "Right!":
                n += 1
            count += 1

    print("Your mark is " + str(n) + "/5. Would you like to save the result? Enter yes or no.")
    save = input()
    if save in ['yes', 'YES', 'y', 'Yes']:
        print("What is your name?")
        name = input()
        try:
            results_file = open('results.txt', 'a', encoding='utf-8')
            results_file.write("{}: {}/5 in level {} ({}).".format(name, n, difficulty, level_description[difficulty]))
        except IOError:
            results_file = open('results.txt', 'w', encoding='utf-8')
            results_file.write("{}: {}/5 in level {} ({}).".format(name, n, difficulty, level_description[difficulty]))
        print("The results are saved in \"results.txt\".")
        results_file.close()
        sys.exit()
    else:
        sys.exit()
main()