import numpy as np
from hashlib import md5
from typing import Iterable, Optional

def simhash(features: Iterable[bytes], weights: Optional[Iterable[int]]=None, f=64):
    """
    SimHash locality sensitive hash function

    Parameters:
        - features: An iterable (e.g. a list, set) of byte arrays.
        - weights: An iterable of integers (default weight value is 1)
        - f: Size in bits of the hash (defaults to 64).

    Returns:
        - The hash as an integer
    """
    w = np.zeros(shape=f, dtype=int)
    if not weights:
        weights = (1,) * len(features)
    for feature, weight in zip(features, weights):
        # f-bit MD5 hash
        digest = md5(feature).digest()
        bits = np.unpackbits(np.frombuffer(digest[:f//8], dtype=">B"))
        # Add/subtract the weight, depending on whether the bit is set 
        wb = np.where(bits == 1, weight, -weight)
        w = w + wb
    # Bits with a positive sum of weights are set to 1
    sh = np.where(w > 0, 1, 0)
    return int.from_bytes(np.packbits(sh).tobytes(), "big")