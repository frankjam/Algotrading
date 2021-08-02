import urllib.request
import talib
import pandas as pd

def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False

print( 'connected' if connect() else 'no internet!' )

df = pd.read_csv('BTC-USD.csv')
close = df['Close']
rsi = talib.RSI(close, timeperiod=14)
i = 0
for rs in rsi:
    if(rs<=30):
        print(f'\nOversold \n\t***BUY*** Rsi is :{rs} at {i}')
    if(rs>=70):
        print(f'\nOverbought \n\t***SELL*** Rsi is :{rs} at {i}')
    i = i + 1