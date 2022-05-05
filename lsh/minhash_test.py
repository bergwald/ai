from lsh import MinHasher, approx_jaccard_distance, jaccard_distance, char_ngrams

def test_str():
    """Strings test"""
    features = lambda x: set([ngram.encode("utf-8") for ngram in char_ngrams(x)])
    a = features("Dostoïevski")
    b = features("Fyodor Dostoyevsky")

    hasher = MinHasher(seed=0)
    vec1 = hasher.hash(a)
    vec2 = hasher.hash(b)
    # The estimated Jaccard distance between a and b should be
    # greater than zero and smaller than one.
    assert 0 < approx_jaccard_distance(vec1, vec2) < 1

    vec3 = hasher.hash(a)
    # The Jaccard distance between two equal sets should be zero.
    assert jaccard_distance(a, a) == 0
    assert approx_jaccard_distance(vec1, vec3) == 0

    c = features("Tennessee Williams")
    vec4 = hasher.hash(c)
    # The Jaccard distance between two disjoint sets should be one.
    assert jaccard_distance(a, c) == 1
    assert approx_jaccard_distance(vec1, vec4) == 1

def test_int():
    """Integers test"""
    features = lambda x: set([i.to_bytes(2, "big", signed=True) for i in x])
    a = features([-10, 8, 326, 42])
    b = features([124, -5, 502, 9, -65, 124])

    hasher = MinHasher(seed=0)
    vec1 = hasher.hash(a)
    vec2 = hasher.hash(b)
    # The Jaccard distance between two disjoint sets should be one.
    assert jaccard_distance(a, b) == 1
    assert approx_jaccard_distance(vec1, vec2) == 1

    vec3 = hasher.hash(a)
    # The Jaccard distance between two equal sets should be zero.
    assert jaccard_distance(a, a) == 0
    assert approx_jaccard_distance(vec1, vec3) == 0
