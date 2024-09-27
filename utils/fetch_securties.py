import yfinance as yf
import pandas as pd

from models.column_headers import *



def fetch_securities(securities_dict):
    names.clear()
    sectors.clear()
    industries.clear()
    shares.clear()
    avg_cost.clear()

    for securities, data in securities_dict.items():
        stock = yf.Ticker(securities)
        info = stock.info

        names.append(info.get('longName', 'N/A'))
        sectors.append(info.get('sector', 'N/A'))
        industries.append(info.get('industry', 'N/A'))
        shares.append(data['shares'])
        avg_cost.append(data['price_paid'])


    df = pd.DataFrame({
        'Ticker': securities_dict.keys(),
        'Name': names,
        'Sectors': sectors,
        'Industry': industries,
        'Shares': shares,
        'Price Paid': avg_cost
    })

    return df