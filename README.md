# finance-yield-curve-pca
PCA analysis of US Treasury yield curves using Python

Overview

This project performs Principal Component Analysis (PCA) on US Treasury yields across multiple maturities.
The goal is to identify the underlying factors that drive yield-curve movements (typically level, slope, curvature).

This type of analysis is widely used in:
- Interest rate modelling
- Fixed-income risk management
- Factor modelling
- Macro-driven quant strategies

The project is fully modular and written in production-style Python.

Features:
- Downloads historical US Treasury yields from FRED
- Cleans and structures yield curve data
- Computes PCA using NumPy (eigen-decomposition of covariance matrix)

Produces:
- Eigenvalues
- Eigenvectors (loadings)
- Principal component scores
- Explained variance ratios

Generates financial plots:
- PCA factor loadings
- Scree plot


How It Works:

1. Data Loading - treasury yields are retrieved using pandas_datareader from the FRED database.

2. PCA is implemented manually.
The function:
- Centers the data
- Computes the covariance matrix
- Applies np.linalg.eigh
- Sorts eigenvalues/vectors
- Returns scores for each date

3. Plots loading of data onto principal components and scree plots


Results:
Typical PCA on yield curves yields the classic structure:

PC1: Level (parallel shift of the curve)
PC2: Slope (steepening / flattening)
PC3: Curvature (butterfly movements)

Requirements:
- Python 3.10+
- datetime
- numpy
- pandas
- pandas_datareader
- matplotlib

Running the Project:
From the project root:
python -m examples.run_full_PCA
This executes the full pipeline end-to-end.
