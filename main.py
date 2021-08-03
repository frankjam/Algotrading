import urllib.request
import talib
import pandas as pd
import yfinance as yf

ticker = "BTC-USD"
def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False

if(connect()):
    print( '\t***connected***\n' )
    data = yf.download(ticker, start="2021-01-01", end="2021-04-30")
else: 
    print('no internet!')

close = data['Close']
rsi = talib.RSI(close, timeperiod=14)
i = 0
for rs in rsi:
    if(rs<=30):
        print(f'\nOversold \n\t***BUY*** Rsi is :{rs} at {i}')
    if(rs>=70):
        print(f'\nOverbought \n\t***SELL*** Rsi is :{rs} at {i}')
    i = i + 1