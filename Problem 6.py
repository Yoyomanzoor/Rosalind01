string_a = (open('Problem 6.txt', 'r')).read()
counts = dict()
s = ''
for i in string_a.split():
    counts[i] = counts.get(i, 0) + 1
for key, value in dict.items(counts):
    s += key + ' ' + str(value) + '\n'

open('Problem 6 answer.txt', 'w').write(s)