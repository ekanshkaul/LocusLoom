def calculate_gc_content(sequence: str) -> float:
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    total_length = len(sequence)
    
    return ((g_count + c_count) / total_length) * 100

def transcribe_dna(sequence: str) -> str:
    return sequence.upper().replace("T", "U")
#Defining the reverse complement funtion
def reverse_complement(sequence: str) -> str:
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement = ""

    for base in sequence.upper():
        complement = complement + complement_map[base]

    return complement[::-1]

#Dictionary
CODON_TABLE = {
    "AUG": "M", #Methionine (Start codon)
    "UUU": "F", #Phenylalanine
    "UUA": "L", #Leucine
    "GGU": "G", #Glycine 
    "GGC": "G",
    "UAA": "*", #Stop codons (UAA, UAG, UGA)
    "UAG": "*",
    "UGA": "*",
}

#Translate an mRNA sequence into an amino acid string.
def translate_rna(rna_sequence: str) -> str:
    rna = rna_sequence.upper()
    protein = ""

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) < 3   :
            break
        amino_acid = CODON_TABLE.get(codon, "X")
        if amino_acid == "*":
            break
        protein = protein + amino_acid

    return protein