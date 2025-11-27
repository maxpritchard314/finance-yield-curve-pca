import datetime as dt
import src.data_loader as dl
import src.PCA_methods as mt
import src.plotting as plot

# Conduct PCA on US treasury data from 01/01/2015 until the present day.
# Use 1, 2, 3, 5, 7, 10 and 30 year maturities.

tickers = ['DGS1','DGS2','DGS3','DGS5','DGS7','DGS10','DGS30']
s = dt.datetime(2015, 1, 1)
e = dt.datetime.today()

df = dl.load_treasury_data(tickers, start=s, end=e)

eigen_values, eigen_vectors, explained_variance, scores = mt.run_full_PCA(df)

print("PC1 is given by:", eigen_vectors[:,0])

plot.plot_pcs(df, eigen_vectors)
plot.plot_spec_pcs(df, eigen_vectors, number=3)
plot.plot_scree(explained_variance)





