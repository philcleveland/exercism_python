dna_to_rna_map = {
    "G" : "C",
    "C" : "G",
    "T" : "A",
    "A" : "U"
}

def to_rna(dna_strand):
    return "".join([dna_to_rna_map[nuc] for nuc in dna_strand])