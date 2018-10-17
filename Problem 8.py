f_problem_string = open("Problem 8.txt", "r").read()

complement = ""

for i in range(len(f_problem_string)):
    if f_problem_string[i] == "A":
        complement += "T"
    elif f_problem_string[i] == "T":
        complement += "A"
    elif f_problem_string[i] == "C":
        complement += "G"
    elif f_problem_string[i] == "G":
        complement += "C"

reverse_complement = complement[::-1]

f_answer = open("Problem 8 answer.txt", "w")
f_answer.write(reverse_complement)