from cvrpy.rules import ConflictingRule
import numpy as np

class ChamberlainCourant(ConflictingRule):
    
    def score_pair(self, a, b):
        profile = self.profile
        n, m = profile.shape
        weights =  self.weights
        return sum([m-min(profile[i][a], profile[i][b])*weights[i] for i in range(n)])