import pandas as pd
import yfinance as yf


def fetch_stock_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch historical stock data from NSE/BSE via yfinance.

    Parameters
    ----------
    symbol : str
        Ticker symbol with exchange suffix, e.g. ``'INFY.NS'`` or
        ``'500209.BO'``.
    start : str
        Start date in ``YYYY-MM-DD`` format.
    end : str
        End date in ``YYYY-MM-DD`` format.

    Returns
    -------
    pandas.DataFrame
        Historical OHLCV data indexed by date.
    """
    ticker = yf.Ticker(symbol)
    data = ticker.history(start=start, end=end)
    if not isinstance(data, pd.DataFrame):
        raise ValueError("No data returned for symbol %s" % symbol)
    return data
