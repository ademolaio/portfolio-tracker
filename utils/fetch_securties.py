import yfinance as yf
import pandas as pd

from models.column_headers import *

def fetch_securities(securities_dict):
    for securities, data in securities_dict.items():
        stock = yf.Ticker(securities)
        info = stock.info

        names.append(info.get('longName', 'N/A'))


    df = pd.DataFrame({
        'Ticker': securities_dict.keys(),
        'Name': names,
    })

    return df

