import typing
import dataclasses
dicts = {}
l = []
print("Input the number of cards:")
a = int(input())
x = []
for i in range(1,a+1):
    print(f"The term for card #{i}:")
    k = input()
    if k in l:
        while k in l:
            print(f'The term "{k}" already exists. Try again:')
            k = input()
    l.append(k)
    print(f"The definition for card #{i}:")
    o = input()
    if o in x:
        while o in x:
            print(f'The definition "{o}" already exists. Try again:')
            o = input()
    x.append(o)
    dicts[k] = o
    i+=1

for i in range(0, a):
    print(f'Print the definition of "{l[i]}":')
    c = input()
    count = 0
    if c == dicts[l[i]]:
        print("Correct!")
    elif c in x:
        while c != dicts[l[count]]:
            count+=1
        print(f'Wrong. The right answer is "{dicts[l[i]]}", but your definition is correct for "{l[count]}".')
    else:
        print(f'Wrong. The right answer is "{dicts[l[i]]}".')