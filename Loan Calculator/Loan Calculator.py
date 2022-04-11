import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', nargs="?", default='')
parser.add_argument('--principal', nargs="?", default='')
parser.add_argument('--periods', nargs="?", default='')
parser.add_argument('--interest', nargs="?", default='')
parser.add_argument('--payment', nargs='?', default='')
args = parser.parse_args()
args_state = [args.type, args.principal, args.periods, args.interest, args.payment]

if args_state.count('') != 1 or args.type not in ['annuity', 'diff'] or (args.type == 'diff' and args.payment) \
        or not args.interest or '-' in args.principal or '-' in args.periods or '-' in args.interest \
        or '-' in args.payment:
    print('Incorrect parameters')
else:
    if args.type == 'annuity':
        if args.payment and args.periods and args.interest:
                x = float(input())
                y = int(input())
                z = float(input()) / 1200
                obsh_2 = x / (z * (1 + z) ** y / ((1 + z) ** y - 1))
                print('Your loan principal =', str(obsh_2) + '!')
        elif args.principal and args.periods and args.interest:
            print("Enter the loan principal:")
            x = int(input())
            print("Enter the number of periods:")
            y = int(input())
            print("Enter the loan interest:")
            z = float(input()) / 1200

            obsh_1 = math.ceil(x * z * (1 + z) ** y / ((1 + z) ** y - 1))
            print('Your monthly payment =', str(obsh_1) + '!')
        else:
                print("Enter the loan principal:")
                x = int(input())
                print("Enter the monthly payment:")
                y = float(input())
                print("Enter the loan interest:")
                z = float(input()) / 1200
                month = math.ceil(math.log(y / (y - z * x), 1 + z))
                years = month // 12
                months = month % 12
                if months and years:
                    print('It will take', years, 'years and', months, 'months to repay this loan!')
                elif months:
                    print('It will take', months, 'months to repay this loan!')
                else:
                    print("It will take, years", years, "to repay this loan!")

    else:
        p = int(args.principal)
        n = int(args.periods)
        i = float(args.interest) / 1200
        summa = 0
        for k in range(1, n + 1):
            d = math.ceil(p / n + i * (p - (p * (k - 1) / n)))
            summa += d
            print('Month',str(k)+': payment is', d)
        print('Overpayment =', summa - p)



