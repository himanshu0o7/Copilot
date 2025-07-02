import pandas as pd


def generate_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Generate simple trading signals based on indicators.

    Returns DataFrame with a new 'Signal' column:
    1 for buy, -1 for sell, 0 for hold.
    """
    df = df.copy()
    df['Signal'] = 0

    buy_condition = (df['MACD'] > df['MACD_signal']) & (df['RSI_14'] < 70)
    sell_condition = (df['MACD'] < df['MACD_signal']) & (df['RSI_14'] > 30)

    df.loc[buy_condition, 'Signal'] = 1
    df.loc[sell_condition, 'Signal'] = -1
    return df
