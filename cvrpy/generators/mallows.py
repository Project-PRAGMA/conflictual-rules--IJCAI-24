from cvrpy.generators.generator import Generator
import numpy as np

## Code taken from mapel library

def computeInsertionProbas(i, phi):
    probas = (i + 1) * [0]
    for j in range(i + 1):
        probas[j] = pow(phi, (i + 1) - (j + 1))
    return probas


def weighted_choice(choices):
    total = 0
    for w in choices:
        total = total + w
    r = np.random.uniform(0, total)
    upto = 0.0
    for i, w in enumerate(choices):
        if upto + w >= r:
            return i
        upto = upto + w
    assert False, "Shouldn't get here"


def mallowsVote(m, insertion_probabilites_list, center):
    vote = [center[0]]
    for i in range(1, m):
        index = weighted_choice(insertion_probabilites_list[i - 1])
        vote.insert(index, center[i])
    return vote






class MallowsGenerator(Generator):

    def __init__(self, n_mallows, phi):
        self.n_mallows = n_mallows
        self.phi = phi

    def __call__(self, n_voters, m_candidates):
        mallows_center = []
        for i in range(self.n_mallows):
            mallows_center.append(np.random.permutation(m_candidates))

        self.mallow_center = mallows_center

        phi = self.phi

        insertion_probabilites_list = []
        for i in range(1, m_candidates):
            insertion_probabilites_list.append(computeInsertionProbas(i, phi))

        votes = []
        for i in range(n_voters):
            r = np.random.randint(0, self.n_mallows)
            center = mallows_center[r]
            vote = mallowsVote(m_candidates, insertion_probabilites_list, center)
            votes += [vote]
        return np.array(votes)

            
