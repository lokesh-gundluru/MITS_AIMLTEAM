def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    # Calculate the Hamming distance if the lengths are equal
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))
