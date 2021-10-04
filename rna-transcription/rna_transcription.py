def to_rna(dna_strand):
    rna_strand = ""
    dna_strand_array = list(dna_strand)
    for nucleotide in dna_strand_array:
        if (nucleotide == 'G'):
            rna_strand += 'C'
        elif(nucleotide == 'C'):
            rna_strand += 'G'
        elif(nucleotide == 'T'):
            rna_strand += 'A'
        else:
            rna_strand += 'U'
    return rna_strand
