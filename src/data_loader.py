import pandas as pd
import pandas_datareader as web

def load_treasury_data(symbols, start, end):
    """
    Download and clean US Treasury yield data from FRED

    Args:
        symbols (list of str): FRED tickers for maturities eg ['DGS1', 'DGS2', 'DGS10']
        start (datetime): start date for download as list 
        end (datetime): end date for download as list 
    
    Returns cleaned yield curve DataFrame with Date as index and each maturity as a column.
    """
    df = web.DataReader(symbols, 'fred', start, end)
    df = df.dropna()
    df = df.reset_index()
    return df

