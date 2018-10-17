f_dataset = open("Problem 10.txt", "r").read()
s = f_dataset.split("\n")
s1 = s[0]
s2 = s[1]
count = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        count += 1

f_answer = open("Problem 10 answer.txt", "w").write(str(count))