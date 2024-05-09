from cvrpy.rules import ConflictingRule
import numpy as np

class MaxNashConflict(ConflictingRule):
    """
    A class representing the Nash Conflict rule for conflicting voting rules.

    This rule calculates the score between two alternatives based on the difference in their rankings
    across all voters, weighted by the voters' weights. The score is calculated as the square root of
    the product of the differences in rankings.

    Attributes:
    -----------
    profile : List[List[int]]
        The profile of the voting rule.
    weights : List[float]
        The weights of the voters in the profile.
    """

    def score_pair(self, a, b):
        profile = self.profile
        weights =  self.weights
        x_a_b = np.sum([(profile[i][a] - profile[i][b])*weights[i] for i in range(len(profile)) if profile[i][a] > profile[i][b]])
        x_b_a = np.sum([(profile[i][b] - profile[i][a])*weights[i]  for i in range(len(profile)) if profile[i][b] > profile[i][a]])
        return np.sqrt(x_a_b * x_b_a)