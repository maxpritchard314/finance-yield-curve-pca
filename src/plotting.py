import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_pcs(data, eig_vecs):
    """
    Plots the loading of the data onto the principal components

    Args:
        data (pandas data frame): data frame with columns=variables
        eig_vecs (numpy array): ordered array containg columns=eigenvectors of principal components
    """
    pcs = pd.DataFrame(
        eig_vecs,
        index=data.columns[1:],           
        columns=[f"PC{i+1}" for i in range(eig_vecs.shape[1])]
    )

    pcs.plot()
    plt.title("PCA Loadings (Eigenvectors)")
    plt.xlabel("Maturity")
    plt.ylabel("Loading")
    plt.show()

def plot_spec_pcs(data, eig_vecs, number=None):
    """
    Plots the loading of the data onto the first number principal components 
    or principle components that accounts for <=percent% of the variance

    Args:
        data (pandas data frame): data frame with columns=variables
        eig_vecs (numpy array): ordered (descending in variance accounted for) array with columns=eigenvectors of principal components
        number (float): number of PCs which account for the highest variance plotted
    """
    if number is not None:    
        spec_pcs = pd.DataFrame(
            eig_vecs[:,0:number],
            index=data.columns[1:],          
            columns=[f"PC{i+1}" for i in range(3)]
        )
    else:
        spec_pcs = pd.DataFrame(
            eig_vecs,
            index=data.columns[1:],          
            columns=[f"PC{i+1}" for i in range(3)]
        )
    spec_pcs.plot()
    plt.title("PC1, 2 and 3 Loadings")
    plt.xlabel("Maturity")
    plt.ylabel("Loading")
    plt.show()

def plot_scree(explained_variance_ratio):
    """
    Plot the scree plot showing the variance explained by each principal component.

    Args:
        explained_variance_ratio (numpy array): ordered descending list of explained variance ratios of principal components
    """
    explained_data = pd.Series(
        explained_variance_ratio,
        index=[f"PC{i+1}" for i in range(len(explained_variance_ratio))]
        )
    explained_data.plot()
    plt.title("Scree Plot")
    plt.xlabel("Principal Component")
    plt.ylabel("Explained Variance Ratio")
    plt.xticks(range(0, len(explained_variance_ratio) + 1))
    plt.grid(True)
    plt.show()



