# MITS_AIMLTEAM/MITS_AIMLTEAM/abstract.py

from abc import ABC, abstractmethod

class SimilarityMetric(ABC):
    """
    Abstract base class for similarity metrics.
    """

    @abstractmethod
    def compute(self, set1, set2):
        pass
