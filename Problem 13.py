f_dataset = open("Problem 13.txt", "r").read()

codon_dictionary = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop", "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M", "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

def complement_strand(sequence):
    reverseStrand = ""
    for i in range(len(sequence)):
        if sequence[i] == "A":
            reverseStrand += "T"
        elif sequence[i] == "T":
            reverseStrand += "A"
        elif sequence[i] == "C":
            reverseStrand += "G"
        elif sequence[i] == "G":
            reverseStrand += "C"
    return reverseStrand

def find_ORFs(sequence):
    ORF1 = ""
    ORF2 = ""
    ORF3 = ""

    for i in range(int(len(sequence_reverse_complement) / 3)):
        j = i
        placement = (j * 3)
        if sequence_reverse_complement[placement:placement + 3] in codon_dictionary:
            ORF1 += codon_dictionary[sequence_reverse_complement[placement:placement + 3]]
        placement = ((j * 3) + 1)
        if sequence_reverse_complement[placement:placement + 3] in codon_dictionary:
            ORF2 += codon_dictionary[sequence_reverse_complement[placement:placement + 3]]
        placement = ((j * 3) + 2)
        if sequence_reverse_complement[placement:placement + 3] in codon_dictionary:
            ORF3 += codon_dictionary[sequence_reverse_complement[placement:placement + 3]]
    return ORF1, ORF2, ORF3

sequence = ""
f_list = f_dataset.split("\n")

for i in range(len(f_list)):
    if f_list[i][0] == "A" or f_list[i][0] == "C" or f_list[i][0] == "G" or f_list[i][0] == "T":
        sequence = f_list[i]



current_read = ""

ORF1 = ""
ORF2 = ""
ORF3 = ""

for i in range(int(len(sequence)/3)):
    j = i
    placement = (j*3)
    if sequence[placement:placement+3] in codon_dictionary:
        ORF1 += codon_dictionary[sequence[placement:placement + 3]]
    placement = ((j*3)+1)
    if sequence[placement:placement+3] in codon_dictionary:
        ORF2 += codon_dictionary[sequence[placement:placement + 3]]
    placement = ((j*3)+2)
    if sequence[placement:placement + 3] in codon_dictionary:
        ORF3 += codon_dictionary[sequence[placement:placement + 3]]

sequence_complement = complement_strand(sequence)

sequence_reverse_complement = ""
for i in range(len(sequence_complement)):
    sequence_reverse_complement += sequence_complement[len(sequence_complement) - (i + 1)]

ORF4 = ""
ORF5 = ""
ORF6 = ""

for i in range(int(len(sequence_reverse_complement) / 3)):
    j = i
    placement = (j*3)
    if sequence_reverse_complement[placement:placement + 3] in codon_dictionary:
        ORF4 += codon_dictionary[sequence_reverse_complement[placement:placement + 3]]
    placement = ((j*3)+1)
    if sequence_reverse_complement[placement:placement + 3] in codon_dictionary:
        ORF5 += codon_dictionary[sequence_reverse_complement[placement:placement + 3]]
    placement = ((j*3)+2)
    if sequence_reverse_complement[placement:placement + 3] in codon_dictionary:
        ORF6 += codon_dictionary[sequence_reverse_complement[placement:placement + 3]]

print(ORF1)
print(ORF2)
print(ORF3)
print(ORF4)
print(ORF5)
print(ORF6)

