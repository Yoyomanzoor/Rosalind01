from Bio import ExPASy, SwissProt

f_dataset = open("Problem 14.txt").read()

f_IDs = [f_dataset]
if "\n" in f_dataset:
    f_IDs = f_dataset.split("\n")

sequence_collection = ""
i = 0
for item in f_IDs:
    handle = ExPASy.get_sprot_raw(f_IDs[i])
    record = SwissProt.read(handle)
    sequence_collection += record.sequence + "\n"
    i += 1

seq_col_list = sequence_collection.split("\n")

NGlyc_motif_locations = ""
ID_marker = []
NGlyc_motif_counter = 0
for j in range(len(seq_col_list)):
    for m in range(len(seq_col_list[j])):
        if seq_col_list[j][m] == "N" and seq_col_list[j][m+1] != "P" and (seq_col_list[j][m+2] == "S" or seq_col_list[j][m+2] == "T") and seq_col_list[j][m+3] != "P":
            NGlyc_motif_locations += str(m + 1) + " "
            NGlyc_motif_counter += 1
    if NGlyc_motif_counter > 0:
        NGlyc_motif_locations += "\n"
        ID_marker.append(j)
    NGlyc_motif_counter = 0

NGlyc_locations_list = NGlyc_motif_locations.split("\n")

outfile = ""
for n in range(len(ID_marker)):
    outfile += f_IDs[ID_marker[n]] + "\n" + NGlyc_locations_list[n] + "\n"

print(outfile)