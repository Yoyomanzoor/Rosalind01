from Bio import ExPASy, SwissProt

def find_multiple_sequences_from_UniProtIDs(ID_list):
    sequences = ""
    i = 0
    for item in ID_list:
        handle = ExPASy.get_sprot_raw(ID_list[i])
        record = SwissProt.read(handle)
        sequences += record.sequence + "\n"
        i += 1
    return sequences


def find_NGlyc_motifs(sequence_list):
    NGlyc_motif_locations = ""
    ID_marker = []
    NGlyc_motif_counter = 0
    for j in range(len(sequence_list)):
        for m in range(len(sequence_list[j])):
            if sequence_list[j][m] == "N" and sequence_list[j][m + 1] != "P" and (sequence_list[j][m + 2] == "S" or sequence_list[j][m + 2] == "T") and sequence_list[j][m + 3] != "P":
                NGlyc_motif_locations += str(m + 1) + " "
                NGlyc_motif_counter += 1
        if NGlyc_motif_counter > 0:
            NGlyc_motif_locations += "\n"
            ID_marker.append(j)
        NGlyc_motif_counter = 0
    return NGlyc_motif_locations, ID_marker


def make_outfile(accession_IDs_list, ID_markers_list, motif_locations_list):
    outfile = ""
    for n in range(len(ID_markers_list)):
        outfile += accession_IDs_list[ID_markers_list[n]] + "\n" + motif_locations_list[n] + "\n"
    print(motif_locations_list)
    return outfile


f_dataset = open("Problem 14.txt").read()

f_IDs = [f_dataset]
if "\n" in f_dataset:
    f_IDs = f_dataset.split("\n")

sequence_collection = find_multiple_sequences_from_UniProtIDs(f_IDs)

seq_col_list = sequence_collection.split("\n")

NGlyc_motif_locations, ID_marker = find_NGlyc_motifs(seq_col_list)

NGlyc_locations_list = NGlyc_motif_locations.split("\n")

outfile = make_outfile(f_IDs, ID_marker, NGlyc_locations_list)

open("Problem 14 answer.txt", "w").write(outfile)