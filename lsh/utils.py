def hamming_distance(a: int, b: int, f=64):
    """
    Bitwise hamming distance between two integers.

    Parameters:
        - a, b: integers to compare
        - f: lenght of the integers in bits (defaults to 64)

    Returns:
        - Hamming distance as an integer
    """
    x = (a ^ b) & ((1 << f) - 1)
    distance = 0
    while x:
        distance += 1
        x &= x - 1
    return distance

def jaccard_distance(a: set, b: set):
    """
    Jaccard distance between two sets.
    
    Parameters:
        - a, b: sets to compare

    Returns:
        - Jaccard distance as a float
    """
    coeff = len(a & b) / len(a | b)
    return 1 - coeff

def char_ngrams(s: str, n=3):
    """
    Splits a string into n-grams of n characters.

    Parameters:
        - s: string to split
        - n: lenght of the n-gram in characters (defaults to 3)

    Returns:
        - list of n-grams
    """
    return [s[i:i+n] for i in range(len(s)-n+1)]
