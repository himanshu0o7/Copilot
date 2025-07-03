# /mount/src/copilot/src/indicators.py

import pandas as pd
import pandas_ta as ta
import numpy as np

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Adds technical indicators to the stock data DataFrame."""
    df.ta.ema(length=20, append=True)
    df.ta.rsi(length=14, append=True)
    
    # Calculate MACD and check if the result is valid
    macd = df.ta.macd(append=False)
    if macd is not None and not macd.empty:
        # If valid, assign the specific columns
        df['MACD'] = macd['MACD_12_26_9']
        df['MACD_signal'] = macd['MACDs_12_26_9']
    else:
        # If not valid (due to insufficient data), fill with NaN
        df['MACD'] = np.nan
        df['MACD_signal'] = np.nan
        
    df.dropna(inplace=True)
    return df