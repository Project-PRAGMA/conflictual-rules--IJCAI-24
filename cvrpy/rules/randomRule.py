from cvrpy.rules import ConflictingRule
import numpy as np

class RandomPair(ConflictingRule):

    def score_pair(self, a, b):
        return np.random.uniform(0, 1)