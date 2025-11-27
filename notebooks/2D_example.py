import numpy as np
import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

start = dt.datetime(2015, 2, 1)
end = dt.datetime(2015,2,6)

#US Treasuries

US_Rates = web.DataReader(['DGS1','DGS2'], 'fred', start, end)
US_Rates.dropna(inplace=True)
US_Rates.reset_index(inplace=True)

X = np.delete(US_Rates.to_numpy(),0,1)

X = np.array(X, dtype=np.float64)

X_centered = X - X.mean(axis=0)

X_cov = np.cov(X_centered, rowvar=False) 
# rowvar = False means that its reading columns as variables and rows as samples, as opposed to the converse
# function computes (1/(n-1)) * X(transposed) * (X), where n is the number of samples for each variable

#print((1/(5-1))*np.matmul(X_centered.T, X_centered)) = print(X_cov) 

e_vals, e_vecs = np.linalg.eigh(X_cov) # gets eigen vectors and values

idx = np.argsort(e_vals)[::-1] # sort eigen values and vectors. 
# eigen vectors will be tansposed, not normalised. 
# so an eigen vectors [x1, x2, ..., xn] is a vector with x1 in the direction of the first variable, 
# x2 in the direction of the second variable and so on.

e_vals = e_vals[idx]
e_vecs = e_vecs[:, idx]

EV1 = abs(float(e_vals[0]))
EV2 = abs(float(e_vals[1]))

denom = EV1 + EV2 
perc1 = (EV1/denom)*100
perc2 = (EV2/denom)*100

print('prevalence of PC1 is', perc1)
print('prevalence of PC2 is', perc2)

PC1 = e_vecs[:,0]
PC2 = e_vecs[:,1]

print('eigenvector of PC1 is', PC1)
print('eigenvector of PC2 is', PC2)



