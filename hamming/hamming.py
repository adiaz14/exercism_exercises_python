def distance(strand_a, strand_b):
    distance = 0
    if len(strand_a) != len(strand_b):
        raise ValueError(
            'error, remenber the Hamming distance is only defined for '
            'sequences of equal length')

    for index in range(len(strand_a)):
        if(strand_a[index-1] != strand_b[index-1]):
            distance = distance + 1
    return distance
