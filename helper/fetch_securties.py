import yfinance as yf
import pandas as pd
import mibian  # Added mibianlib for Greeks and implied volatility calculation

from models.exchange_mapping import *
from models.column_headers import *


def fetch_securities(securities_dict):
    # Clear lists to avoid previous data retention
    names.clear()

    for securities, data in securities_dict.items():
        stock = yf.Ticker(securities)
        info = stock.info

        names.append(info.get('longName', 'N/A'))


    # Create the DataFrame with the Greeks and Implied Volatility included
    df = pd.DataFrame({
        'Ticker': securities_dict.keys(),
        'Name': names,

    })

    return df