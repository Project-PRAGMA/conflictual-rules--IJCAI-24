import numpy as np

def pref_a_b(profile, a, b, weights=None):
    if weights is None:
        weights = np.ones(len(profile))
    return np.sum([weights[i] for i in range(len(profile)) if profile[i][a] > profile[i][b]])

def matrix_pref(profile, weights=None):
    matrix = np.zeros((len(profile[0]), len(profile[0])))
    for i in range(len(profile[0])):
        for j in range(len(profile[0])):
            if i == j:
                continue
            matrix[i][j] = pref_a_b(profile, i, j, weights)

    return matrix.T


def getAlpha(profile, a, b, weights=None):
    if weights is None:
        weights = np.ones(len(profile))
    n_ab = pref_a_b(profile, a,b, weights)
    return 2*min(n_ab, np.sum(weights)-n_ab)/np.sum(weights)


def getBeta(profile, a, b, weights = None):
    if weights is None:
        weights = np.ones(len(profile))
    _, m = profile.shape
    return np.sum([np.abs((profile[i][a] - profile[i][b])*weights[i]) for i in range(len(profile))])/(np.sum(weights)*(m-1))


def getGamma(profile, a, b, weights = None):
    if weights is None:
        weights = np.ones(len(profile))
    _, m = profile.shape
    Sab = pref_a_b(profile, a, b, weights)
    Sba = pref_a_b(profile, b, a, weights)
    x_a_b = np.sum([(profile[i][a] - profile[i][b])*weights[i] for i in range(len(profile)) if profile[i][a] > profile[i][b]])
    x_b_a = np.sum([(profile[i][b] - profile[i][a])*weights[i]  for i in range(len(profile)) if profile[i][b] > profile[i][a]])
    if Sab*Sba == 0:
        return 0
    return min((x_a_b*Sba)/(Sab*x_b_a), (x_b_a*Sab)/(Sba*x_a_b))


def getImbalance(profile, a, b, weights = None):
    if weights is None:
        weights = np.ones(len(profile))
    _, m = profile.shape
    x_a_b = np.sum([(profile[i][a] - profile[i][b])*weights[i] for i in range(len(profile)) if profile[i][a] > profile[i][b]])
    x_b_a = np.sum([(profile[i][b] - profile[i][a])*weights[i]  for i in range(len(profile)) if profile[i][b] > profile[i][a]])
    return abs(x_a_b - x_b_a)/(x_a_b + x_b_a)


def getSwapDistance(profile, a, b, weights = None):
    if weights is None:
        weights = np.ones(len(profile))
    _, m = profile.shape
    x_a_b = np.sum([(profile[i][a] - profile[i][b])*weights[i] for i in range(len(profile)) if profile[i][a] > profile[i][b]])
    x_b_a = np.sum([(profile[i][b] - profile[i][a])*weights[i]  for i in range(len(profile)) if profile[i][b] > profile[i][a]])
    return min(x_a_b, x_b_a)