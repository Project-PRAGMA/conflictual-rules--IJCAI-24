import numpy as np
from cvrpy.rules import ConflictingRule
from cvrpy import pref_a_b, getAlpha, getBeta

class MaxPolar(ConflictingRule):

    def __init__(self, p):
        self.p = p

    def score_pair(self, a, b):
        profile = self.profile
        weights =  self.weights
        alpha = getAlpha(profile, a, b, weights)
        beta  = getBeta(profile, a, b, weights)

        return alpha*beta**self.p 
    





