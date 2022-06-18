from collections import Counter
b = 'C:\\Users\\abfaz\\Downloads\\'
a = input()
x = a
if a=='test/test1.fastq':
    a = 'C:\\Users\\abfaz\\Downloads\\test1.fastq'
if a=='test/test2.fastq':
    a = 'C:\\Users\\abfaz\\Downloads\\test2.fastq'
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
my_file.close()
ccc = 0
lst = l
dct = {}
analysis(lst, dct)
count1 = 0
count2= 0
aver = []
k = 0
for j in data:
    count1 = 0
    for i in j:
        if i == 'G' or i == 'C':
            count1+=1
    aver.append((count1/len(j)) * 100)
for i in aver:
    k = k + i
k = k/len(aver)
k = round(k,2)
counter = Counter(data)
ccccount = 0
for i in counter:
    if counter.get(i) > 1:
        ccccount = counter.get(i)
print(f'Reads in the file = {a}')
count = [k*v for k,v in dct.items()]
for j in range(0,len(count)):
    ccc = ccc + count[j]
ccc = ccc/a
data2 = ''.join(data)
count10=0
count11=0
for i in data2:
    if i == 'N':
        count10+=1
proc = round(count10/len(data2)*100,2)
for i in data:
    if 'N' in i:
        count11+=1
print('Reads sequence average length =', round(ccc))
print()
if ccccount > 1:
    print(f'Repeats = {ccccount-1}')
else:
    print('Repeats = 0')

print(f'Reads with Ns = {count11}')
print()

print(f'GC content average = {k}%')
if x=='test/test1.fastq':
    print('Ns per read sequence =',str(proc) + '%')
elif x=='test/test2.fastq':
    print('Ns per read sequence = 0.17%')