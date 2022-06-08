import numpy as np
from hashlib import md5
from typing import Iterable, Optional

# Maximum value of the permutation parameters and next largest prime number
MAX = (2**32) - 1
PRIME = 4294967311

class MinHasher():
    """
    MinHash locality sensitive hash function
    
    Parameters:
        - d: Number of dimensions of the MinHash vector (defaults to 128)
        - seed: A seed to initialize the RNG used to generate
        the parameters of the permutation function
    """
    def __init__(self, d=128, seed: Optional[int]=None):
        self.d = d
        rng = np.random.default_rng(seed)
        # Parameters of the permutation function
        self.a = rng.integers(0, MAX, size=d)
        self.b = rng.integers(0, MAX, size=d)

    def hash(self, s: Iterable[bytes]):
        """
        Compute the hash of a sequence of byte arrays.
        
        Arguments:
            - s: An iterable (e.g. a list, set) of byte arrays.
        
        Returns:
            - The hash as a Numpy array.
        """
        vec = np.full(self.d, MAX)
        for element in s:
            # 32-bit MD5 hash
            digest = md5(element).hexdigest()
            h = int(digest[:8], 16)
            # Min-wise independent permutation
            out = (self.a * h + self.b) % PRIME
            vec = np.minimum(vec, out)
        return vec

def approx_jaccard_distance(a: np.ndarray, b: np.ndarray):
    """
    Approximate Jaccard distance of two sets based on their MinHash vectors.
    
    Arguments:
        - a, b: The arrays representing the MinHash vectors to be compared.

    Returns:
        - Approximate Jaccard distance as a float
    """
    assert a.shape == b.shape
    return 1 - np.count_nonzero(a == b) / a.shape[0]
