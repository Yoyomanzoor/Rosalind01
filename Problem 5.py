f = open('problem 5.txt', 'r')
s = f.read()
slist = s.split('\n')
a = ''
for line in range(len(slist)):
    if line % 2 == 1:
        a += slist[line] + '\n'
print(a)