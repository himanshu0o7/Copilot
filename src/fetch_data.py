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

    Raises
    ------
    ValueError
        If no data is returned for the given symbol and date range.
    """
    data = yf.download(symbol, start=start, end=end, progress=False)

    if data.empty:
        raise ValueError(
            f"No data returned for symbol '{symbol}' "
            f"from {start} to {end}."
        )

    return data