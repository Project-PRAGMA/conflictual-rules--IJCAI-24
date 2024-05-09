import numpy as np
import matplotlib.pyplot as plt

### Plot heatmap of scores,

def plot_heatmap(matrix, title, candidats, reorder=None):
    if reorder:
        matrix = matrix[reorder]
        matrix = matrix[::][:,reorder]
        candidats = [candidats[i] for i in reorder]
    _, m = matrix.shape
    fig, ax = plt.subplots(figsize=(8,6))
    # minimum value not equal to 0:
    minval = np.min(matrix[np.nonzero(matrix)])
    im = ax.imshow(matrix, cmap='autumn', vmin=minval)
    ax.set_xticks(np.arange((m)))
    ax.set_yticks(np.arange((m)))
    ax.set_xticklabels(candidats)
    ax.set_yticklabels(candidats)

    
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")
    ax.set_title(title)
    # number on each cell
    for i in range((m)):
        for j in range((m)):
            text = ax.text(j, i, int(matrix[i, j]),
                        ha="center", va="center", color="k", fontsize=8)     


    ## Show color scale 

    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Score", rotation=-90, va="bottom")
       
    fig.tight_layout()
    plt.show()