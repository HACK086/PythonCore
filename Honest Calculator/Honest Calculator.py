import re
obsh_msg = ["Enter an equation",
            "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            " ... lazy",
            " ... very lazy",
            " ... very, very lazy",
            "You are",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]
def is_one_digit(x):
    if re.match(r'\d(\.0)?$', x) and 10 > int(float(x)) > -10:
        return True
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(str(v1)) and is_one_digit(str(v2)):
        msg = msg + obsh_msg[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + obsh_msg[7]
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + obsh_msg[8]
    if msg != "":
        msg = obsh_msg[9] + msg
    print(msg)


count = 0
result = 0
memory = 0
while count == 0:
    print(obsh_msg[0])
    calc = input().split()
    try:
        x = int(calc[0])
    except:
        try:
            x = float(calc[0])
        except:
            x = calc[0]
    try:
        y = int(calc[2])
    except:
        try:
            y = float(calc[2])
        except:
            y = calc[2]
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    oper = calc[1]
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        if oper == '+' or oper == '-' or oper == '*' or oper == '/':
            check(x, y, oper)
            if oper == '+':
                result = x + y
            elif oper == '-':
                result = x - y
            elif oper == '*':
                result = x * y
            else:
                if oper == '/' and y == 0:
                    print(obsh_msg[3])
                else:
                    result = x / y
            if oper == '+' or oper == '-' or oper == '*' or (oper == '/' and y != 0):
                print(float(result))
                count2 = 0
                while count2 == 0:
                    print(obsh_msg[4])
                    answer = input()
                    if answer == 'y':
                        if is_one_digit(result):
                            msg_index = 10
                            count4 = 0
                            while count4 == 0:
                                print(obsh_msg[msg_index])
                                answer = input()
                                if answer == 'y':
                                    if msg_index < 12:
                                        msg_index +=1
                                    else:
                                        count4 = 1
                                        memory = result
                                        count3 = 0
                                        while count3 == 0:
                                            print(obsh_msg[5])
                                            answer = input()
                                            if answer == 'y':
                                                count2 = 1
                                                count3 = 1
                                            else:
                                                if answer == 'n':
                                                    count3 = 1
                                                    count2 = 1
                                                    count = 1
                                                else:
                                                    continue
                                else:
                                    if answer == 'n':
                                        count4 = 1
                                        count3 = 0
                                        while count3 == 0:
                                            print(obsh_msg[5])
                                            answer = input()
                                            if answer == 'y':
                                                count2 = 1
                                                count3 = 1
                                            else:
                                                if answer == 'n':
                                                    count3 = 1
                                                    count2 = 1
                                                    count = 1
                                                else:
                                                    continue
                        else:
                            memory = result
                            count3 = 0
                            while count3 == 0:
                                print(obsh_msg[5])
                                answer = input()
                                if answer == 'y':
                                    count2 = 1
                                    count3 = 1
                                else:
                                    if answer == 'n':
                                        count3 = 1
                                        count2 = 1
                                        count = 1
                                    else:
                                        continue

                    else:
                        if answer != 'n':
                            continue
                    if answer == 'n' or answer == 'y':
                        count3 = 0
                        while count3 == 0:
                            print(obsh_msg[5])
                            answer = input()
                            if answer == 'y':
                                count2 = 1
                                count3 = 1
                            else:
                                if answer == 'n':
                                    count3 = 1
                                    count2 = 1
                                    count = 1
                                else:
                                    continue

        else:
            print(obsh_msg[2])
    else:
        print(obsh_msg[1])