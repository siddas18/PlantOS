from scipy.ndimage.morphology import binary_fill_holes
import numpy as np

def fill_holes(cluster,labels):
    label0=1-binary_fill_holes(labels == 0).astype(int)
    label1=binary_fill_holes(labels == 1).astype(int)
    if labels[0][0] + labels[0][-1] + labels[-1][-1] + labels[-1][0] > 2:
        cluster[(labels * label0).astype(bool)] = np.asarray([0,0,0])
    else:
        cluster[((1-labels) * (1-label1)).astype(bool)] = np.asarray([0,0,0])
    return cluster
    