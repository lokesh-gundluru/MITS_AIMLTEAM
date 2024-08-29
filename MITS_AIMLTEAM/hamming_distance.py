# MITS_AIMLTEAM/MITS_AIMLTEAM/hamming.py

from .abstract import SimilarityMetric


class HammingDistance(SimilarityMetric):
    """
    Computes the Hamming Distance between two equal-length strings.
    """

    def compute(self, str1, str2):
        if len(str1) != len(str2):
            raise ValueError("Strings must be of the same length")

        return sum(el1 != el2 for el1, el2 in zip(str1, str2))
