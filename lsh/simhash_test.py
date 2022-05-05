import pytest
from lsh import simhash, hamming_distance, char_ngrams


def test_str():
    """Strings test"""
    features = lambda x: [ngram.encode("utf-8") for ngram in char_ngrams(x, 1)]
    a = "Hello World!"
    b = "Hello Wrld!"
    sh1 = simhash(features(a))
    sh2 = simhash(features(b))
    # The Hamming distance between the hashes of the features of a and b
    # should be greater than zero
    assert hamming_distance(sh1, sh2) > 0

    sh3 = simhash(features(a))
    # Hashes of the same features should be equal
    assert hamming_distance(sh1, sh3) == 0


def test_str_special():
    """Special characters test"""
    features = lambda x: [char.encode("utf-8") for char in x]
    a = "hunden gør"
    b = "hunden gor"
    # ø and o are not the same characters and, with UTF-8 encoding, should
    # not return the same hashes
    assert simhash(features(a)) != simhash(features(b))


def test_int():
    """Integers test"""
    features = lambda x: [integer.to_bytes(2, "big") for integer in x]
    a = [123]
    b = [456]
    sh1 = simhash(features(a))
    sh2 = simhash(features(b))
    # The Hamming distance between the hashes of the features of a and b
    # should be greater than zero
    assert hamming_distance(sh1, sh2) > 0

    sh3 = simhash(features(a))
    # Hashes of the same features should be equal
    assert hamming_distance(sh1, sh3) == 0


def test_int_overflow():
    """Integer overflow test"""
    features = lambda x: [integer.to_bytes(1, "big") for integer in x]
    a = [255]
    b = [256]
    sh1 = simhash(features(a))
    with pytest.raises(OverflowError):
        features(b)


def test_int_signed():
    """Signed vs. unsigned integers test"""
    x = 7
    uint8 = int.to_bytes(x, 1, "big")
    int8 = int.to_bytes(x, 1, "big", signed=True)
    # 7 is always represented as b'\x07'
    assert uint8 == int8

    a = -1
    b = 255
    sh1 = simhash([int.to_bytes(a, 1, "big", signed=True)])
    sh2 = simhash([int.to_bytes(b, 1, "big")])
    # Different integers can yield the same hash if signed and unsigned
    # representations are mixed
    assert sh1 == sh2
