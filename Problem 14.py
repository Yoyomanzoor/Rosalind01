from Bio import ExPASy, SwissProt

f_dataset = open("Problem 14.txt").read()

f_IDs = [f_dataset]
sequence_collection = ""
i = 0
outfile = ""

if "\n" in f_dataset:
    f_IDs = f_dataset.split("\n")

for item in f_IDs:
    handle = ExPASy.get_sprot_raw(f_IDs[i])
    record = SwissProt.read(handle)
    sequence_collection += record.sequence + "\n"
    i += 1

seq_col_list = sequence_collection.split("\n")

for j in range(len(seq_col_list)):
    outfile += f_IDs[j - 1] + "\n"
    for m in range(len(seq_col_list[j])):
        if seq_col_list[j][m] == "N" and seq_col_list[j][m+1] != "P" and (seq_col_list[j][m+2] == "S" or seq_col_list[j][m+2] == "T") and seq_col_list[j][m+3] != "P":
            outfile += str(m+1) + " "
    outfile += "\n"

print(outfile)

preoutfile_list = outfile.split("\n")

for item in preoutfile_list:
    pass