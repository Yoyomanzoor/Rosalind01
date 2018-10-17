f_string = open("Problem 7.txt", "r").read()
f_answer = open("Problem 7 answer.txt", "w")
f_answer.write(str(f_string.count("A")) + " " + str(f_string.count("C")) + ' ' + str(f_string.count("G")) + ' ' + str(f_string.count("T")))