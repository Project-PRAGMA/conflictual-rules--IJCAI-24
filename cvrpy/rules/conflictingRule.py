import numpy as np

class ConflictingRule(object):

    def score_pair(self, a, b):
        raise NotImplementedError
    
    def matrix_score(self):
        n, m = self.profile.shape
        matrix = np.zeros((m,m))
        for i in range(m):
            for j in range(i+1,m):
                matrix[i][j] = self.score_pair(i,j)

        return matrix + matrix.T
    
    def selected_pair(self):
        n, m = self.profile.shape
        return np.unravel_index(np.argmax(self.matrix_score(), axis=None),(m,m))
    
    def __call__(self, profile, weights=None):
        self.profile = np.array(profile)
        if weights is None:
            weights = np.ones(len(profile))
        self.weights = weights
        return self
    
    def num_ties(self):
        return np.sum(self.matrix_score() == np.max(self.matrix_score()))