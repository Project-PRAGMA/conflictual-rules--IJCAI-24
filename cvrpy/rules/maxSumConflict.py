from cvrpy.rules import ConflictingRule
import numpy as np
from cvrpy import pref_a_b

class MaxSumConflict(ConflictingRule):
    """
    A class representing the MaxSumConflict rule for conflicting voting.

    This rule calculates the score of a pair of alternatives based on the difference in the 
    sum of weights of voters who prefer one alternative over the other.

    Attributes:
    - profile (list): A list of dictionaries representing the preference profile of the voters.
    - weights (list): A list of weights for each voter in the preference profile.
    """

    def score_pair(self, a, b):
        profile = self.profile
        weights =  self.weights
        n_b_a = pref_a_b(profile, b, a, weights)
        n_a_b = pref_a_b(profile, a, b, weights)
        x_a_b = np.sum([(profile[i][a] - profile[i][b])*weights[i] for i in range(len(profile)) if profile[i][a] > profile[i][b]])
        x_b_a = np.sum([(profile[i][b] - profile[i][a])*weights[i] for i in range(len(profile)) if profile[i][b] > profile[i][a]])

        return np.sqrt(x_a_b * n_b_a + x_b_a * n_a_b)
    