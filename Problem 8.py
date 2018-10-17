f_problem_string = open("Problem 8.txt", "r").read()

print(f_problem_string)

complement = ""

for i in range(len(f_problem_string)):
    if f_problem_string[i] == "A":
        complement += "T"
        #f_problem_string = f_problem_string.replace(f_problem_string[i], "T")
    elif f_problem_string[i] == "T":
        complement += "A"
        #f_problem_string = f_problem_string.replace(f_problem_string[i], "A")
    elif f_problem_string[i] == "C":
        complement += "G"
        #f_problem_string = f_problem_string.replace(f_problem_string[i], "G")
    elif f_problem_string[i] == "G":
        complement += "C"
        #f_problem_string = f_problem_string.replace(f_problem_string[i], "C")

reverse_complement = complement[::-1]

print(complement + " = complement")
print(reverse_complement + " = reverse complement")

f_answer = open("Problem 8 answer.txt", "w")
f_answer.write(f_problem_string)