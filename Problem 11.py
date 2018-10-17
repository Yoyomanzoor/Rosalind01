import json
from Bio import SeqIO, Entrez
Entrez.email = "smanzoor@luc.edu"

f_dataset = open("Problem 11.txt", "r").read()
f_list = f_dataset.split(" ")
accessId = ""
fasta_files = dict()

for i in range(len(f_list)):
    accessId = f_list[i]
    handle = Entrez.efetch(db="nucleotide", rettype="fasta", id=accessId)
    fasta_files[handle.read()] = f_list[i]

f_answer = open("Problem 11 answer.txt", "w").write(min(fasta_files, key=len))

#with open("Problem 11 answer.txt", "w") as fp:
#    json.dump(fasta_files, fp)

# sequences = dict()
# seqFragments = []
# for line in fasta_files[f_list[0]]:
#     if line.startswith('>'):
#         if seqFragments:
#             sequence = ''.join(seqFragments)
#             sequences[id] = sequence
#         seqFragments = []
#         id = line.rstrip()[1:]
#     else:
#         seq = line.rstrip()
#         seqFragments.append(seq)
# if seqFragments:
#     sequence = ''.join(seqFragments)
#     sequences[id] = sequence
# print(sequence)