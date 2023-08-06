"""Module for interacting with Haddad et al, 2008"""

import os
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import StandardScaler

import pyrfume
from . import features
from .base import DATA_DIR
GOOGLE_DIR = DATA_DIR / 'google_2019'


def get_google_embeddings():
    emb_raw = pyrfume.load_data(GOOGLE_DIR / 'embeddings.csv')
    emb = emb_raw[[x for x in list(emb_raw) if 'emb_' in x]]
    emb = emb.dropna()
    return emb

def get_google_distances(embeddings):
    emb = get_google_embeddings()
    # Compute distance matrix.  
    # This will give basically the same low-D embedding as using raw high-dimensional embeddings does
    dist = pdist(emb, metric='euclidean')
    dist = squareform(dist)
    distances = pd.DataFrame(dist, index=emb.index, columns=emb.index)
    return distances
