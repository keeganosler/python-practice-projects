# dna analysis matches the sample codons to codons obtained from one of three suspects' dna test files

sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
    dna_data = ""
    with open(dna_file, "r") as f:
        for line in f:
            dna_data += line
    return dna_data

def create_codons(dna):
    codons = []
    for i in range(0, len(dna), 3):
        if((i+3) < len(dna)):
            codons.append(dna[i:i+3])
    return codons

def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
           matches += 1
    return matches   

def is_criminal(sample):
    dna_data = read_dna(sample)
    codons = create_codons(dna_data)
    num_matches = match_dna(codons)
    if(num_matches >= 3):
        print("There are %s codon matches with this suspect. Continue investigation." %(num_matches))
    else:
        print("%s total matches. Probably not the one." %(num_matches))


is_criminal('suspect2.txt')


