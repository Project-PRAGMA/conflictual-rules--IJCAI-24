from cvrpy.generators.generator import Generator
import numpy as np

class MetricPositionsGenerator:

    def __init__(self, dimensions=2):
        self.dimensions = dimensions

    def __call__(self, n):
        raise NotImplementedError
    

class UniformPositionsGenerator(MetricPositionsGenerator):
    
    def __call__(self, n):
        return np.random.uniform(size=(n, self.dimensions))
    



class GaussianPositionsGenerator(MetricPositionsGenerator):
        
        def __init__(self, dimensions, sigma=1):
            super().__init__(dimensions)
            self.sigma = sigma
    
        def __call__(self, n):
            return np.random.normal(loc=0.5, size=(n, self.dimensions), scale=self.sigma)
        


class MultiGaussianPositionsGenerator(MetricPositionsGenerator):
    
    def __init__(self, dimensions, centers, sigma=1):
            super().__init__(dimensions)
            self.sigma = sigma
            self.centers = centers
    def __call__(self, n):
        centers = self.centers
        sigma = self.sigma
        dimensions = self.dimensions
        positions = np.zeros((n, dimensions))
        for i in range(n):
            r = np.random.randint(len(centers))
            positions[i] = np.random.normal(loc=centers[r], size=(1, dimensions), scale=sigma)

        return positions