codon_to_protein_map = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }

codon_length = 3

def proteins(strand):
    nucleotide = [strand[i:i+codon_length] for i in range(0, len(strand), codon_length)]
    polypeptide = []
    for codon in nucleotide:
        if codon_to_protein_map[codon] == "STOP":
            break
        polypeptide.append(codon_to_protein_map[codon])
    return polypeptide

