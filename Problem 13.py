f_dataset = open("Problem 13.txt", "r").read()

sequence = ""
f_list = f_dataset.split("\n")

for i in range(len(f_list)):
    if f_list[i][0] == "A" or f_list[i][0] == "C" or f_list[i][0] == "G" or f_list[i][0] == "T":
        sequence = f_list[i]

