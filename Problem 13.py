f_dataset = open("Problem 13.txt", "r").read()

codon_dictionary = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop", "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M", "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

def find_seq(dataset):
    seq_from_data = ""
    f_list = f_dataset.split("\n")
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

def find_ORFs(seq):
    ORF1 = ""
    ORF2 = ""
    ORF3 = ""

    for i in range(int(len(seq) / 3)):
        j = i
        placement = (j * 3)
        if seq[placement:placement + 3] in codon_dictionary:
            ORF1 += codon_dictionary[seq[placement:placement + 3]]
        placement = ((j * 3) + 1)
        if seq[placement:placement + 3] in codon_dictionary:
            ORF2 += codon_dictionary[seq[placement:placement + 3]]
        placement = ((j * 3) + 2)
        if seq[placement:placement + 3] in codon_dictionary:
            ORF3 += codon_dictionary[seq[placement:placement + 3]]

    return ORF1, ORF2, ORF3

sequence = find_seq(f_dataset)

sequence_complement = find_complement_strand(sequence)

sequence_reverse_complement = reverse_seq_order(sequence_complement)

ORF_set1 = find_ORFs(sequence)
print(ORF_set1)
ORF_set2 = find_ORFs(sequence_reverse_complement)
print(ORF_set2)
