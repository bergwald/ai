# Locality Sensitive Hash Functions

Numpy implementations of the [SimHash](https://en.wikipedia.org/wiki/SimHash) and [MinHash](https://en.wikipedia.org/wiki/MinHash) locality sensitive hash functions.

## Examples

**MinHash**

```python
from lsh import MinHasher, approx_jaccard_distance, jaccard_distance, char_ngrams

features = lambda x: set([ngram.encode("utf-8") for ngram in char_ngrams(x)])
a = features("Dostoïevski")
b = features("Fyodor Dostoyevsky")

hasher = MinHasher(seed=0)
vec1 = hasher.hash(a)
vec2 = hasher.hash(b)

print(f"Real Jaccard distance: {jaccard_distance(a, b)}")
print(f"Approximate Jaccard Distance: {approx_jaccard_distance(vec1, vec2)}")
```
```
Real Jaccard distance: 0.75
Approximate Jaccard Distance: 0.7421875
```

**Simhash**

```python
from lsh import simhash, hamming_distance, char_ngrams

features = lambda x: [ngram.encode("utf-8") for ngram in char_ngrams(x, 1)]
a = "Hello World!"
b = "Hello Wxrld!"

sh1 = simhash(features(a))
sh2 = simhash(features(b))

print(hamming_distance(sh1, sh2))
```
```
4
```

## Directory Structure

- `minhash.py`: Implementation of MinHash
- `minhash_test.py`: Tests for MinHash
- `simhash.py`: Implementation of Simhash
- `simhash_test.py`: Tests for Simhash
- `utils.py`: bitwise Hamming distance, Jaccard distance, and character n-grams functions

## References

- Charikar, M. (2002). Similarity Estimation Techniques from Rounding Algorithms. [PDF](https://www.cs.princeton.edu/courses/archive/spr04/cos598B/bib/CharikarEstim.pdf)
- Broder, A. Z., Charikar, M., Frieze, A. M., Mitzenmacher, M. (2000). Min-Wise Independent Permutations [PDF](https://dl.acm.org/doi/pdf/10.1145/276698.276781)
