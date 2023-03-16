import MetaTrader5 as mt5
import pandas as pd
from classes import Bot
from threading import Thread
import pandas_ta as ta
import matplotlib.pyplot as plt


symbol = ['EURUSD',"USDJPY","USDCAD"] # Tradeable symbols
timeframe = 15 # integer value representing minutes
start_bar = 0 # initial position of first bar
num_bars = 500 # number of bars

def strategy(symbol):
    for x in range(len(symbol)):
        bars = mt5.copy_rates_from_pos(symbol[x], timeframe, start_bar, num_bars)
        df = pd.DataFrame(bars)
        df['EMA'] = pd.DataFrame(df["close"]).ta.ema(length=14)
        
        if (df["close"].iloc[-1]) > (df['EMA'].iloc[-1]):
            direction = "buy"
        else:
            direction = "sell"
        print(direction)
        plt.plot(df.index, df['close'],df['EMA'])
        plt.show()
        globals()[f"direction{x}"] = direction
        

strategy(symbol)


bot1 = Bot(symbol[0],0.1,3,4,direction0)
bot2 = Bot(symbol[1],0.1,3,4,direction1)
bot3 = Bot(symbol[2],0.1,3,4,direction2)

def b1():
    bot1.run()
def b2():
    bot2.run()
def b3():
    bot3.run()

thread1 = Thread(target=b1)
thread2 = Thread(target=b2)
thread3 = Thread(target=b3)

mt5.initialize(login = 51147707,server = "ICMarketsEU-Demo",password ="XYPcfgAw")

thread1.start()
thread2.start()
thread3.start()










