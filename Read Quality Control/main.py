a = input()
my_file = open(a)
l = []

data = my_file.read().splitlines()[1::4]
for i in range(0, len(data)):
        l.append(len(data[i]))
a = len(l)


def fill_list(m1, m2, amount, l):
    from random import randint
    for i in range(amount):
        l.append(randint(m1, m2))


def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


lst = l
dct = {}

analysis(lst, dct)
print(f'Reads in the file = {a}:')
for item in sorted(dct):
    print("      with length %d = %d" % (item, dct[item]))
print('Reads sequence average length =', max(dct))
