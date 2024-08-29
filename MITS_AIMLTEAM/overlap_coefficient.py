# MITS_AIMLTEAM/MITS_AIMLTEAM/overlap.py

from .abstract import SimilarityMetric

class OverlapCoefficient(SimilarityMetric):
    """
    Computes the Overlap Coefficient between two sets.
    """

    def compute(self, set1, set2):
        intersection = len(set1.intersection(set2))
        min_size = min(len(set1), len(set2))
        return intersection / min_size if min_size != 0 else 0
