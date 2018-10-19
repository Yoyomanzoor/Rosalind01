import re
from collections import OrderedDict

codon_dictionary = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop", "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M", "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

def find_seq(dataset):
    seq_from_data = ""
    f_list = dataset.split("\n")
    for i in range(len(f_list)):
        if f_list[i][0] == "A" or f_list[i][0] == "C" or f_list[i][0] == "G" or f_list[i][0] == "T":
            seq_from_data = f_list[i]

    return seq_from_data

def find_complement_strand(sequence):
    complement_strand = ""
    for i in range(len(sequence)):
        if sequence[i] == "A":
            complement_strand += "T"
        elif sequence[i] == "T":
            complement_strand += "A"
        elif sequence[i] == "C":
            complement_strand += "G"
        elif sequence[i] == "G":
            complement_strand += "C"

    return complement_strand

def reverse_seq_order(sequence):
    reverse_sequence = ""
    for i in range(len(sequence)):
        reverse_sequence += sequence[len(sequence_complement) - (i + 1)]

    return reverse_sequence

def find_ORFs(sequence):
    ORF1 = ""
    ORF2 = ""
    ORF3 = ""

    for i in range(int(len(sequence) / 3)):
        j = i
        placement = (j * 3)
        if sequence[placement:placement + 3] in codon_dictionary:
            ORF1 += codon_dictionary[sequence[placement:placement + 3]]
        placement = ((j * 3) + 1)
        if sequence[placement:placement + 3] in codon_dictionary:
            ORF2 += codon_dictionary[sequence[placement:placement + 3]]
        placement = ((j * 3) + 2)
        if sequence[placement:placement + 3] in codon_dictionary:
            ORF3 += codon_dictionary[sequence[placement:placement + 3]]

    return ORF1, ORF2, ORF3

def find_start_in_ORFs(OTF_list):
    sequence_start_seqments = ""
    k = 0
    for i in range(len(ORF_set)):
        for j in range(len(ORF_set[i])):
            if ORF_set[i][j] == "M":
                for l in range(len(ORF_set[i]) - j):
                    sequence_start_seqments += ORF_set[i][j + l]
                sequence_start_seqments += "\n"
    return sequence_start_seqments

def split(delimiters, string, maxsplit=0):
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

f_dataset = open("Problem 13.txt", "r").read()

sequence = find_seq(f_dataset)

sequence_complement = find_complement_strand(sequence)

sequence_reverse_complement = reverse_seq_order(sequence_complement)

ORF_set = find_ORFs(sequence) + find_ORFs(sequence_reverse_complement)

start_segments_unspliced = find_start_in_ORFs(ORF_set)

start_segments_list = start_segments_unspliced.split("\n")

start_segments_filtered = []
for i in range(len(start_segments_list)):
    if "Stop" in start_segments_list[i]:
        start_segments_filtered += start_segments_list[i].split("Stop", 0)

segments_str = ""
for i in range(len(start_segments_filtered)):
    segments_str += start_segments_filtered[i] + "\n"

delimiters = "\n", "op"
segments_list = split(delimiters, segments_str)

segments_filtered = ""

for i in range(len(segments_list)):
    if "M" in segments_list[i] and "St" in segments_list[i]:
        segments_filtered += segments_list[i] + "\n"

delimiters = "\n", "St"
f_answer_list = split(delimiters, segments_str)

f_answer_list = [x for x in f_answer_list if "op" not in x]

f_answer_list = list(set(f_answer_list))

f_answer = ""
for i in range(len(f_answer_list)):
    f_answer += f_answer_list[i] + "\n"

print(f_answer)