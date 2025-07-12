import math
import yfinance as yf
import numpy as np

# top 100 US Company tickers
tickers = [
    "AAPL", "MSFT", "NVDA", "GOOGL", "GOOG", "AMZN", "META"
    # ,  "BRK.B", "TSLA", "LLY",
    # "AVGO", "UNH", "XOM", "JPM", "JNJ", "V", "PG", "MA", "HD", "MRK",
    # "COST", "CVX", "ABBV", "ORCL", "PEP", "KO", "BAC", "WMT", "ADBE", "TMO",
    # "MCD", "CRM", "NFLX", "ACN", "INTC", "DIS", "ABT", "WFC", "CMCSA", "PFE",
    # "LIN", "DHR", "AMD", "TXN", "NEE", "PM", "BMY", "NKE", "IBM", "LOW",
    # "AMGN", "UPS", "HON", "RTX", "SPGI", "SBUX", "UNP", "CAT", "MS", "GS",
    # "MDT", "BLK", "CVS", "DE", "SCHW", "INTU", "PLD", "GE", "AMT", "LMT",
    # "ISRG", "PYPL", "NOW", "C", "QCOM", "ELV", "T", "MO", "BKNG", "TGT",
    # "ADP", "GILD", "DUK", "SO", "VRTX", "MMC", "REGN", "CB", "ZTS", "CL",
    # "USB", "CCI", "SYK", "BDX", "EQIX", "APD", "ICE", "FDX", "ADI"
]


'''
return_t = ln((p_t / p_(t-1)))
log returns are continuously compounded and more accurate for time series return stuff

'''
hist_data = {}
returns = {}
mat = []

for t in tickers:
    data = yf.Ticker(t).history(period="1mo")
    hist_data[t] = data
    close = data['Close']
    
    return_series = np.log(close / close.shift(1))
    returns[t] = return_series.dropna().tolist()
    
date_index = 0
while date_index != len(returns[tickers[0]]):
    row = [returns[t][date_index] for t in tickers]
    mat.append(row)
    date_index += 1

R = np.array(mat)
print(R)
    

# for k, v in hist_data.items():
#     print(k)
#     print(v)
#     print()
    
# for k, v in returns.items():
#     print(k)
#     print(v)
#     print()