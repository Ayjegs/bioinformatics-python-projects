# This is my working sequence; The idea of this project is to write a small Python program that takes a DNA sequence and reports useful biological information from it.


# This is my working DNA sequence
dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"


# Checking the legth of the sequence
seq_len = len(dna)
print (f'The length of the working sequence is {seq_len}.')


# Confirming if its all in uppercase
if (dna == dna.upper()):
    print ('The working sequence is in uppercase')


#How many A, T, G, and C bases are in it?
no_of_A = dna.count ('A')
no_of_T = dna.count ('T')
no_of_G = dna.count ('G')
no_of_C = dna.count ('C')

no_of_bases = f'There are {no_of_A} adenine residue, {no_of_T} thymine residue, {no_of_G} guanine residue, and {no_of_C} cytosine residue. This gives a total number of {seq_len} residues in the working sequence'

print (no_of_bases)


# Which bases are present?
bases_present = set(dna)
print(f'The bases present are: {bases_present}')


#Does it contain a start codon like "ATG"?
if (dna.startswith('ATG')):
    print("Yes, the working sequence starts with the start codon 'ATG'")
else:
    print('No, the working sequence does not contain a start codon')


# What does the sequence look like if you reverse it?
reversed_seq = dna[::-1]
print(f'The reversed sequence is : {reversed_seq}.')


# Can you split it into codons (groups of 3)
for codons in range(0, len(dna), 3):
    codon = dna[codons:codons+3]
    if len(codon) == 3:
        print(codon)
   

#Is it a valid DNA sequence or does it contain weird characters?
valid_bases = ('A', 'T', 'G', 'C')

if (set(dna).issubset(valid_bases)):
    print('The sequence contains only valid bases')
else:
    print (f'This is not a valid DNA sequence, the invalid characters are {set(dna).difference(valid_bases)}.')
    
    
#Calculate the GC content in the working sequence
gc_content = ((no_of_G + no_of_C) / len(dna)) * 100
print(f'The GC content in the working sequnece is {round(gc_content, 1)}%.')