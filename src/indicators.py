import pandas as pd
import pandas_ta as ta


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Compute basic technical indicators and return new DataFrame."""
    df = df.copy()
    df['SMA_20'] = df['Close'].rolling(20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['RSI_14'] = ta.rsi(df['Close'], length=14)
    macd = ta.macd(df['Close'])
    df['MACD'] = macd['MACD_12_26_9']
    df['MACD_signal'] = macd['MACDs_12_26_9']
    return df
