import numpy as np
import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def run_full_PCA(data):
    """
    Runs the process PCA on data frame. 

    Args:
        data (pandas df): data frame containing data to be analysed, columns=variables, rows=samples

    Returns:
       eigen values of data as 1D numpy array
       eigen vectors of principal components of data as numpy array with columns=eigenvectors
       explained variance of each principal component as ordered list
       loadings of original data onto principal components as pandas data frame
    """
    cov = covariance(centre(data))
    e_val, e_vec = Eigen_Decomposition(cov)
    return e_val, e_vec, Explained_Variance(e_val), Scores(centre(data), e_vec)

def centre(data):
    """
    Convert pandas data frame into centred numpy array

    Args:
        data (pandas df): data frame containing columns=variables, rows=samples
        index should be reset to sample labels - as returned by load_treasury_data

    Returns:
        T x N numpy array for N variables and T samples
    """
    Matrix = np.array(np.delete(data.to_numpy(),0,1), dtype=np.float64) 
    return Matrix - Matrix.mean(axis=0)

def covariance(array):
    """
    Converts centred data matrix to covariance matrix

    Args:
        array (numpy array): data matrix with N variables in columns and T samples in rows
    
    Returns:
        covariance N x N matrix as numpy array. 
    """
    return np.cov(array, rowvar=False)

def Eigen_Decomposition(cov):
    """
    Eigen value and vector decomposition of covariance matrix

    Args:
        cov (numpy array): N x N numpy array, covariance matrix of data

    Returns:
        ordered list of eigen values, numpy array with eigen vectors in columns ordered corresponding to eigen values list
    """
    eig_vals, eig_vecs = np.linalg.eigh(cov) 
    idx = np.argsort(eig_vals)[::-1] 
    return eig_vals[idx], eig_vecs[:, idx]

def Explained_Variance(eig_vals):
    """
    Find the explained variance ratio; shows how much of the total variance each principal component explains

    Args:
        eig_vals (list): ordered list of eigen values corresponding to eigen vectors of principal components

    Returns:
        ordered list of explained variance of the prinicipal components
    """
    return eig_vals / eig_vals.sum()

def Scores(Centred_Matrix, eig_vecs):
    """
    Projects centred data onto principal components

    Args:
        Centred_Matrix (numpy array): numpy array containing centred data. columns=variables, rows=samples
        eig_vecs (numpy array): numpy array with columns=ordered eigenvectors of principal components

    Returns:
        pandas data frame with columns=principal components, rows=dates
    """
    return Centred_Matrix @ eig_vecs



