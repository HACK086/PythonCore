import random
print("Enter the number of friends joining (including you):")
a=int(input())
d=0
l={}
if a<1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    while(d<a):
        b=input()
        l[b]=0
        d+=1

    print("Enter the total bill value:")
    c = int(input())
    pol = c/a
    for key in l:
        l[key] = round(pol,2)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    abc = input()
    if abc == 'No':
        print("No one is going to be lucky")
        print(l)
    elif abc == 'Yes':
        name = random.choice(list(l.keys()))
        print(name, 'is the lucky one!')
        coun = round(c/(len(l)-1),2)
        for i in l:
            l[i] = coun
        l[name] = 0
        print(l)



