from Bio import ExPASy
from Bio import SwissProt

f_ID = open("Problem 12.txt", "r").read()

handle = ExPASy.get_sprot_raw(f_ID)
record = SwissProt.read(handle)

GO_Bio_Processes = []
temp_list = []

for item in record.cross_references:
    if item[0] == 'GO':
        temp_list = item[2].split(":")
        if temp_list[0] == 'P':
            GO_Bio_Processes.append(temp_list[1])

f_answer = ""

for i in range(len(GO_Bio_Processes)):
    f_answer += GO_Bio_Processes[i] + "\n"

open("Problem 12 answer.txt", "w").write(f_answer)