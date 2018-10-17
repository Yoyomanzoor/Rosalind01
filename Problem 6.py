string_a = (open('Problem 6.txt', 'r')).read()
counts = dict()
s = ''
for i in string_a.split():
    counts[i] = counts.get(i, 0) + 1
f = open('Problem 6 answer.txt', 'w')
for key, value in dict.items(counts):
    s += key + ' ' + str(value) + '\n'
f.write(s)