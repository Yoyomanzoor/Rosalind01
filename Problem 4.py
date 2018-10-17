a = 1
b = 7
d = 0
print(b-a)
for i in range(b-a+1):
    if a % 2 == 1:
        d += a
    a += 1
print(d)