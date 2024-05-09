from cvrpy.rules import ConflictingRule
import numpy as np
from cvrpy import getSwapDistance

class MaxSwap(ConflictingRule):


    def score_pair(self, a, b):
        return getSwapDistance(self.profile, a, b, self.weights)
    