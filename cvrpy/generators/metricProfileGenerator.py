from cvrpy.generators.generator import Generator
from cvrpy.generators.metric import *
import numpy as np

class MetricGenerator(Generator):

    def __init__(self, votersGenerator, candidatesGenerator):
        self.votersGenerator = votersGenerator
        self.candidatesGenerator = candidatesGenerator

    def __call__(self, n_voters, m_candidates):
        voters_positions = self.votersGenerator(n_voters)
        candidates_positions = self.candidatesGenerator(m_candidates)
        self.voters_positions = voters_positions
        self.candidates_positions = candidates_positions
        return np.array([np.argsort(np.argsort(
            np.linalg.norm(voter_position - candidates_positions, axis=1))) for voter_position in voters_positions])

