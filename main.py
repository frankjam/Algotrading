import urllib.request
import talib
import pandas as pd
import yfinance as yf
from datetime import date
ticker = "BTC-USD"
start ='2021-01-01'
end= date.today()

def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False

if(connect()):
    print( '\t***connected***\n' )
    data = yf.download(ticker, start=start, end=end)
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