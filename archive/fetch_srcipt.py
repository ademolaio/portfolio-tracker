# import yfinance as yf
# import pandas as pd
#
# from models.exchange_mapping import *
# from models.column_headers import *
#
#
#
# def fetch_securities(securities_dict):
#     names.clear()
#     exchanges.clear()
#     security_types.clear()
#     sectors.clear()
#     industries.clear()
#     shares.clear()
#     avg_cost.clear()
#     cost_basis.clear()
#     close_prices.clear()
#     market_values.clear()
#     gains.clear()
#     analysts_ratings.clear()
#     options_available.clear()
#     options_volumes.clear()
#     implied_volatility.clear()
#     previous_closes.clear()
#     prices.clear()
#     market_caps.clear()
#     pe_ratios.clear()
#     eps.clear()
#     annual_dividends.clear()
#     dividend_yields.clear()
#     volumes.clear()
#     avg_volumes.clear()
#     betas.clear()
#     declaration_dates.clear()
#     ex_dividend_dates.clear()
#     record_dates.clear()
#     payment_dates.clear()
#     earnings_dates.clear()
#     week_52_ranges.clear()
#     opens.clear()
#     bids.clear()
#     asks.clear()
#
#     for securities, data in securities_dict.items():
#         stock = yf.Ticker(securities)
#         info = stock.info
#
#         names.append(info.get('longName', 'N/A'))
#         exchange_code = info.get('exchange', 'N/A')
#         exchanges.append(exchange_dict.get(exchange_code, exchange_code))
#         security_types.append(info.get('quoteType', 'N/A'))
#         sectors.append(info.get('sector', 'N/A'))
#         industries.append(info.get('industry', 'N/A'))
#         shares.append(data['shares'])
#         avg_cost.append(data['avg_cost'])
#
#         # Calculate Cost Basis (avg_cost * shares)
#         if 'avg_cost' in data and 'shares' in data:
#             basis = data['avg_cost'] * data['shares']
#         else:
#             basis = 'N/A'
#         cost_basis.append(basis)
#
#         # Fetch the most recent close price
#         try:
#             recent_close = stock.history(period="1d")['Close'].iloc[-1]  # Most recent close
#         except Exception as e:
#             recent_close = 'N/A'
#         close_prices.append(recent_close)
#
#         # Calculate Cost Basis (previous close * shares)
#         if recent_close != 'N/A' and 'shares' in data:
#             market_value = recent_close * data['shares']  # Shares * Previous Close
#         else:
#             market_value = 'N/A'
#         market_values.append(market_value)
#
#         if market_value != 'N/A' and basis != 'N/A':
#             gain = market_value - basis
#         else:
#             gain = 'N/A'
#         gains.append(gain)
#
#         analysts_ratings.append(info.get('recommendationKey', 'N/A'))
#         options_available.append('Yes' if stock.options else 'No')
#
#         try:
#             if stock.options:
#                 # Get the first available expiration date for options
#                 expiration = stock.options[0]
#                 option_chain = stock.option_chain(expiration)
#                 total_call_volume = option_chain.calls['volume'].sum()  # Sum of call volumes
#                 total_put_volume = option_chain.puts['volume'].sum()  # Sum of put volumes
#                 total_options_volume = total_call_volume + total_put_volume
#             else:
#                 total_options_volume = 'N/A'
#         except Exception as e:
#             total_options_volume = 'N/A'
#         options_volumes.append(total_options_volume)  # Append the options volume
#
#         # Fetch options volume and implied volatility
#         try:
#             if stock.options:
#                 # Get the first available expiration date for options
#                 expiration = stock.options[0]
#                 option_chain = stock.option_chain(expiration)
#
#                 # Fetch implied volatility (average of calls and puts)
#                 avg_implied_volatility = (option_chain.calls['impliedVolatility'].mean() + option_chain.puts[
#                     'impliedVolatility'].mean()) / 2
#                 implied_volatility.append(avg_implied_volatility)
#
#                 # Sum of call and put volumes
#                 total_call_volume = option_chain.calls['volume'].sum()  # Sum of call volumes
#                 total_put_volume = option_chain.puts['volume'].sum()  # Sum of put volumes
#                 total_options_volume = total_call_volume + total_put_volume
#             else:
#                 total_options_volume = 'N/A'
#                 implied_volatility.append('N/A')
#         except Exception as e:
#             total_options_volume = 'N/A'
#             implied_volatility.append('N/A')
#
#         options_volumes.append(total_options_volume)  # Append the options volume
#
#         previous_closes.append(info.get('previousClose', 'N/A'))
#         prices.append(info.get('price', 'N/A'))
#         week_52_ranges.append(info.get('fiftyTwoWeekRange', 'N/A'))
#         opens.append(info.get('opens', 'N/A'))
#         bids.append(info.get('bids', 'N/A'))
#         asks.append(info.get('asks', 'N/A'))
#         market_cap = info.get('marketCap', 'N/A')
#         if market_cap != 'N/A' and market_cap is not None:
#             market_cap = '{:,}'.format(market_cap)
#         market_caps.append(market_cap)
#         pe_ratios.append(info.get('trailingPE', 'N/A'))
#         eps.append(info.get('trailingEps', 'N/A'))
#         annual_dividends.append(info.get('annualDividend', 'N/A'))
#         dividend_yields.append(info.get('dividendYield', 'N/A'))
#         volumes.append(info.get('volume', 'N/A'))
#         avg_volumes.append(info.get('averageVolume', 'N/A'))
#         betas.append(info.get('beta', 'N/A'))
#         declaration_dates.append(info.get('dividendDeclaredDate', 'N/A'))
#         ex_dividend_dates.append(info.get('exDividendDate', 'N/A'))
#         record_dates.append(info.get('dividendRecordDate', 'N/A'))
#         payment_dates.append(info.get('dividendPaymentDate', 'N/A'))
#         earnings_dates.append(info.get('earningsDate', 'N/A'))
#
#
#     df = pd.DataFrame({
#         'Ticker': securities_dict.keys(),
#         'Name': names,
#         'Exchange': exchanges,
#         'Security Type': security_types,
#         'Sectors': sectors,
#         'Industry': industries,
#         'Shares': shares,
#         'Avg Cost': avg_cost,
#         'Cost Basis': cost_basis,
#         'Close Price': close_prices,
#         'Market Value': market_values,
#         'Gain': gains,
#         'Analysts Rating': analysts_ratings,
#         'Options Available': options_available,
#         'Options Volume': options_volumes,
#         'Implied Volatility': implied_volatility,
#         'Previous Close': previous_closes,
#         'Prices': prices,
#         'Week 52 Range': week_52_ranges,
#         'Opens': opens,
#         'Bids': bids,
#         'Asks': asks,
#         'Market Cap': market_caps,
#         'PE Ratio': pe_ratios,
#         'EPS': eps,
#         'Annual Dividends': dividend_yields,
#         'Dividend Yields': dividend_yields,
#         'Volumes': volumes,
#         'Avg Volume': avg_volumes,
#         'Betas': betas,
#         'Declaration Dates': declaration_dates,
#         'Ex Dividend Dates': ex_dividend_dates,
#         'Record Dates': record_dates,
#         'Payment Dates': payment_dates,
#         'Earnings Dates': earnings_dates,
#
#     })
#
#     return df


# import yfinance as yf
# import pandas as pd
#
# from models.exchange_mapping import *
# from models.column_headers import *
#
#
# def fetch_securities(securities_dict):
#     names.clear()
#     exchanges.clear()
#     security_types.clear()
#     sectors.clear()
#     industries.clear()
#     shares.clear()
#     avg_cost.clear()
#     cost_basis.clear()
#     close_prices.clear()
#     market_values.clear()
#     gains.clear()
#     analysts_ratings.clear()
#     options_available.clear()
#     options_volumes.clear()
#     previous_closes.clear()
#     prices.clear()
#     market_caps.clear()
#     pe_ratios.clear()
#     eps.clear()
#     annual_dividends.clear()
#     dividend_yields.clear()
#     volumes.clear()
#     avg_volumes.clear()
#     betas.clear()
#     declaration_dates.clear()
#     ex_dividend_dates.clear()
#     record_dates.clear()
#     payment_dates.clear()
#     earnings_dates.clear()
#     week_52_ranges.clear()
#     opens.clear()
#     bids.clear()
#     asks.clear()
#     implied_volatility.clear()  # New list for storing implied volatility
#
#     for securities, data in securities_dict.items():
#         stock = yf.Ticker(securities)
#         info = stock.info
#
#         names.append(info.get('longName', 'N/A'))
#         exchange_code = info.get('exchange', 'N/A')
#         exchanges.append(exchange_dict.get(exchange_code, exchange_code))
#         security_types.append(info.get('quoteType', 'N/A'))
#         sectors.append(info.get('sector', 'N/A'))
#         industries.append(info.get('industry', 'N/A'))
#         shares.append(data['shares'])
#         avg_cost.append(data['avg_cost'])
#
#         # Calculate Cost Basis (avg_cost * shares)
#         if 'avg_cost' in data and 'shares' in data:
#             basis = data['avg_cost'] * data['shares']
#         else:
#             basis = 'N/A'
#         cost_basis.append(basis)
#
#         # Fetch the most recent close price
#         try:
#             recent_close = stock.history(period="1d")['Close'].iloc[-1]  # Most recent close
#         except Exception as e:
#             recent_close = 'N/A'
#         close_prices.append(recent_close)
#
#         # Calculate Cost Basis (previous close * shares)
#         if recent_close != 'N/A' and 'shares' in data:
#             market_value = recent_close * data['shares']  # Shares * Previous Close
#         else:
#             market_value = 'N/A'
#         market_values.append(market_value)
#
#         if market_value != 'N/A' and basis != 'N/A':
#             gain = market_value - basis
#         else:
#             gain = 'N/A'
#         gains.append(gain)
#
#         analysts_ratings.append(info.get('recommendationKey', 'N/A'))
#         options_available.append('Yes' if stock.options else 'No')
#
#         # Fetch options volume and implied volatility
#         try:
#             if stock.options:
#                 # Get the first available expiration date for options
#                 expiration = stock.options[0]
#                 option_chain = stock.option_chain(expiration)
#
#                 # Fetch implied volatility (average of calls and puts)
#                 avg_implied_volatility = (option_chain.calls['impliedVolatility'].mean() + option_chain.puts[
#                     'impliedVolatility'].mean()) / 2
#                 implied_volatility.append(avg_implied_volatility)
#
#                 # Sum of call and put volumes
#                 total_call_volume = option_chain.calls['volume'].sum()  # Sum of call volumes
#                 total_put_volume = option_chain.puts['volume'].sum()  # Sum of put volumes
#                 total_options_volume = total_call_volume + total_put_volume
#             else:
#                 total_options_volume = 'N/A'
#                 implied_volatility.append('N/A')
#         except Exception as e:
#             total_options_volume = 'N/A'
#             implied_volatility.append('N/A')
#
#         options_volumes.append(total_options_volume)  # Append the options volume
#
#         previous_closes.append(info.get('previousClose', 'N/A'))
#         prices.append(info.get('price', 'N/A'))
#         week_52_ranges.append(info.get('fiftyTwoWeekRange', 'N/A'))
#         opens.append(info.get('opens', 'N/A'))
#         bids.append(info.get('bids', 'N/A'))
#         asks.append(info.get('asks', 'N/A'))
#         market_cap = info.get('marketCap', 'N/A')
#         if market_cap != 'N/A' and market_cap is not None:
#             market_cap = '{:,}'.format(market_cap)
#         market_caps.append(market_cap)
#         pe_ratios.append(info.get('trailingPE', 'N/A'))
#         eps.append(info.get('trailingEps', 'N/A'))
#         annual_dividends.append(info.get('annualDividend', 'N/A'))
#         dividend_yields.append(info.get('dividendYield', 'N/A'))
#         volumes.append(info.get('volume', 'N/A'))
#         avg_volumes.append(info.get('averageVolume', 'N/A'))
#         betas.append(info.get('beta', 'N/A'))
#         declaration_dates.append(info.get('dividendDeclaredDate', 'N/A'))
#         ex_dividend_dates.append(info.get('exDividendDate', 'N/A'))
#         record_dates.append(info.get('dividendRecordDate', 'N/A'))
#         payment_dates.append(info.get('dividendPaymentDate', 'N/A'))
#         earnings_dates.append(info.get('earningsDate', 'N/A'))
#
#     df = pd.DataFrame({
#         'Ticker': securities_dict.keys(),
#         'Name': names,
#         'Exchange': exchanges,
#         'Security Type': security_types,
#         'Sectors': sectors,
#         'Industry': industries,
#         'Shares': shares,
#         'Avg Cost': avg_cost,
#         'Cost Basis': cost_basis,
#         'Close Price': close_prices,
#         'Market Value': market_values,
#         'Gain': gains,
#         'Analysts Rating': analysts_ratings,
#         'Options Available': options_available,
#         'Options Volume': options_volumes,
#         'Implied Volatility': implied_volatility,  # Add implied volatility column
#         'Previous Close': previous_closes,
#         'Prices': prices,
#         'Week 52 Range': week_52_ranges,
#         'Opens': opens,
#         'Bids': bids,
#         'Asks': asks,
#         'Market Cap': market_caps,
#         'PE Ratio': pe_ratios,
#         'EPS': eps,
#         'Annual Dividends': dividend_yields,
#         'Dividend Yields': dividend_yields,
#         'Volumes': volumes,
#         'Avg Volume': avg_volumes,
#         'Betas': betas,
#         'Declaration Dates': declaration_dates,
#         'Ex Dividend Dates': ex_dividend_dates,
#         'Record Dates': record_dates,
#         'Payment Dates': payment_dates,
#         'Earnings Dates': earnings_dates,
#
#     })
#
#     return df


import yfinance as yf
import pandas as pd
import mibian  # Added mibianlib for Greeks and implied volatility calculation

from models.exchange_mapping import *
from models.column_headers import *


def fetch_securities(securities_dict):
    # Clear lists to avoid previous data retention
    names.clear()
    exchanges.clear()
    security_types.clear()
    sectors.clear()
    industries.clear()
    shares.clear()
    avg_cost.clear()
    cost_basis.clear()
    close_prices.clear()
    market_values.clear()
    gains.clear()
    analysts_ratings.clear()
    options_available.clear()
    options_volumes.clear()
    implied_volatility.clear()  # Implied Volatility list
    previous_closes.clear()
    prices.clear()
    market_caps.clear()
    pe_ratios.clear()
    eps.clear()
    annual_dividends.clear()
    dividend_yields.clear()
    volumes.clear()
    avg_volumes.clear()
    betas.clear()
    declaration_dates.clear()
    ex_dividend_dates.clear()
    record_dates.clear()
    payment_dates.clear()
    earnings_dates.clear()
    week_52_ranges.clear()
    opens.clear()
    bids.clear()
    asks.clear()
    deltas.clear()  # Delta
    gammas.clear()  # Gamma
    thetas.clear()  # Theta
    vegas.clear()  # Vega
    rhos.clear()  # Rho

    for securities, data in securities_dict.items():
        stock = yf.Ticker(securities)
        info = stock.info

        names.append(info.get('longName', 'N/A'))
        exchange_code = info.get('exchange', 'N/A')
        exchanges.append(exchange_dict.get(exchange_code, exchange_code))
        security_types.append(info.get('quoteType', 'N/A'))
        sectors.append(info.get('sector', 'N/A'))
        industries.append(info.get('industry', 'N/A'))
        shares.append(data['shares'])
        avg_cost.append(data['avg_cost'])

        # Calculate Cost Basis (avg_cost * shares)
        if 'avg_cost' in data and 'shares' in data:
            basis = data['avg_cost'] * data['shares']
        else:
            basis = 'N/A'
        cost_basis.append(basis)

        # Fetch the most recent close price
        try:
            recent_close = stock.history(period="1d")['Close'].iloc[-1]  # Most recent close
        except Exception as e:
            recent_close = 'N/A'
        close_prices.append(recent_close)

        # Calculate Market Value (close price * shares)
        if recent_close != 'N/A' and 'shares' in data:
            market_value = recent_close * data['shares']  # Shares * Previous Close
        else:
            market_value = 'N/A'
        market_values.append(market_value)

        if market_value != 'N/A' and basis != 'N/A':
            gain = market_value - basis
        else:
            gain = 'N/A'
        gains.append(gain)

        analysts_ratings.append(info.get('recommendationKey', 'N/A'))
        options_available.append('Yes' if stock.options else 'No')

        # Fetch options volume and implied volatility using mibianlib
        try:
            if stock.options:
                # Get the first available expiration date for options
                expiration = stock.options[0]
                option_chain = stock.option_chain(expiration)

                # Implied Volatility (average of calls and puts)
                avg_implied_volatility = (option_chain.calls['impliedVolatility'].mean() +
                                          option_chain.puts['impliedVolatility'].mean()) / 2
                implied_volatility.append(avg_implied_volatility)

                # Greeks calculation using mibianlib (using the first call option as an example)
                first_call = option_chain.calls.iloc[0]
                strike_price = first_call['strike']
                time_to_expiration = (pd.to_datetime(expiration) - pd.Timestamp.today()).days
                risk_free_rate = 1  # Assume a 1% risk-free rate

                # Use mibianlib to calculate Greeks and implied volatility
                option = mibian.BS([recent_close, strike_price, risk_free_rate, time_to_expiration],
                                   volatility=avg_implied_volatility * 100)  # Convert to percentage

                deltas.append(option.callDelta)
                gammas.append(option.gamma)
                thetas.append(option.callTheta)
                vegas.append(option.vega)
                rhos.append(option.callRho)

                # Sum of call and put volumes
                total_call_volume = option_chain.calls['volume'].sum()
                total_put_volume = option_chain.puts['volume'].sum()
                total_options_volume = total_call_volume + total_put_volume
            else:
                total_options_volume = 'N/A'
                implied_volatility.append('N/A')
                deltas.append('N/A')
                gammas.append('N/A')
                thetas.append('N/A')
                vegas.append('N/A')
                rhos.append('N/A')
        except Exception as e:
            implied_volatility.append('N/A')
            deltas.append('N/A')
            gammas.append('N/A')
            thetas.append('N/A')
            vegas.append('N/A')
            rhos.append('N/A')
            total_options_volume = 'N/A'

        options_volumes.append(total_options_volume)

        previous_closes.append(info.get('previousClose', 'N/A'))
        prices.append(info.get('price', 'N/A'))
        week_52_ranges.append(info.get('fiftyTwoWeekRange', 'N/A'))
        opens.append(info.get('opens', 'N/A'))
        bids.append(info.get('bids', 'N/A'))
        asks.append(info.get('asks', 'N/A'))
        market_cap = info.get('marketCap', 'N/A')
        if market_cap != 'N/A' and market_cap is not None:
            market_cap = '{:,}'.format(market_cap)
        market_caps.append(market_cap)
        pe_ratios.append(info.get('trailingPE', 'N/A'))
        eps.append(info.get('trailingEps', 'N/A'))
        annual_dividends.append(info.get('annualDividend', 'N/A'))
        dividend_yields.append(info.get('dividendYield', 'N/A'))
        volumes.append(info.get('volume', 'N/A'))
        avg_volumes.append(info.get('averageVolume', 'N/A'))
        betas.append(info.get('beta', 'N/A'))
        declaration_dates.append(info.get('dividendDeclaredDate', 'N/A'))
        ex_dividend_dates.append(info.get('exDividendDate', 'N/A'))
        record_dates.append(info.get('dividendRecordDate', 'N/A'))
        payment_dates.append(info.get('dividendPaymentDate', 'N/A'))
        earnings_dates.append(info.get('earningsDate', 'N/A'))

    # Create the DataFrame with the Greeks and Implied Volatility included
    df = pd.DataFrame({
        'Ticker': securities_dict.keys(),
        'Name': names,
        'Exchange': exchanges,
        'Security Type': security_types,
        'Sectors': sectors,
        'Industry': industries,
        'Shares': shares,
        'Avg Cost': avg_cost,
        'Cost Basis': cost_basis,
        'Close Price': close_prices,
        'Market Value': market_values,
        'Gain': gains,
        'Analysts Rating': analysts_ratings,
        'Options Available': options_available,
        'Options Volume': options_volumes,
        'Implied Volatility': implied_volatility,
        'Delta': deltas,
        'Gamma': gammas,
        'Theta': thetas,
        'Vega': vegas,
        'Rho': rhos,
        'Previous Close': previous_closes,
        'Prices': prices,
        'Week 52 Range': week_52_ranges,
        'Opens': opens,
        'Bids': bids,
        'Asks': asks,
        'Market Cap': market_caps,
        'PE Ratio': pe_ratios,
        'EPS': eps,
        'Annual Dividends': dividend_yields,
        'Dividend Yields': dividend_yields,
        'Volumes': volumes,
        'Avg Volume': avg_volumes,
        'Betas': betas,
        'Declaration Dates': declaration_dates,
        'Ex Dividend Dates': ex_dividend_dates,
        'Record Dates': record_dates,
        'Payment Dates': payment_dates,
        'Earnings Dates': earnings_dates
    })

    return df