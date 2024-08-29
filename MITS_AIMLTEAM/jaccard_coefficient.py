# MITS_AIMLTEAM/MITS_AIMLTEAM/jaccard.py

from .abstract import SimilarityMetric

class JaccardCoefficient(SimilarityMetric):
    """
    Computes the Jaccard Coefficient between two sets.
    """

    def compute(self, set1, set2):
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0
