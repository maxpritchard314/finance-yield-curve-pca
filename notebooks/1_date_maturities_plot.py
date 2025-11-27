import numpy as np
import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

start = dt.datetime(1980, 1, 1)
end = dt.datetime(1980, 2, 1)

#US Treasuries

US_Rates = web.DataReader(['DGS1','DGS2','DGS3','DGS5','DGS7','DGS10','DGS30'], 'fred', start, end)
US_Rates.dropna(inplace=True)
US_Rates.reset_index(inplace=True)

# Drop index and Date columns to keep only maturities
yields = US_Rates.iloc[1, 1:]  # iloc[0, 2:] means first row, columns from 3rd onward

maturities = yields.index

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.plot(maturities, yields.values, marker='o', linestyle='-')
plt.title(f"US Bond Yield Curve")
plt.xlabel("Maturity")
plt.ylabel("Yield (%)")
plt.grid(True)
plt.show()
