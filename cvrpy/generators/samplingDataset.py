from cvrpy.generators.generator import Generator
import numpy as np

class SamplingDatasetGenerator(Generator):

    def __init__(self, rankings, weights=None):
        self.rankings = rankings
        self.weights = weights

    def __call__(self, n_voters, m_candidates):
        votes = []
        weights = self.weights
        total_candidates = len(self.rankings[0])
        # chose random candidates 
        candidates = np.random.choice(total_candidates, m_candidates, replace=False)

        for i in range(n_voters):
            # select a random ranking with weight
            if weights is None:
                r = np.random.randint(0, len(self.rankings))
            else:
                r = np.random.choice(len(self.rankings), p=weights/np.sum(weights))
            votes.append(self.rankings[r][candidates])

        return np.array(votes)
    

class SamplingDatasetsGenerator(Generator):

    def __init__(self, rankings_list):
        self.generators = [SamplingDatasetGenerator(rankings) for rankings in rankings_list]

    def __call__(self, n_voters, m_candidates):
        r = np.random.randint(0, len(self.generators))
        return self.generators[r](n_voters, m_candidates)