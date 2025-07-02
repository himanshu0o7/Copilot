import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def _prepare_features(df: pd.DataFrame, n_lags: int = 5):
    X, y = [], []
    closes = df['Close'].values
    for i in range(n_lags, len(closes)):
        X.append(closes[i - n_lags:i])
        y.append(closes[i])
    return np.array(X), np.array(y)


def predict_next_close(df: pd.DataFrame, n_lags: int = 5) -> float:
    """Train a simple regression model and predict next day's close."""
    if len(df) <= n_lags:
        raise ValueError("Not enough data to make prediction")
    X, y = _prepare_features(df, n_lags)
    model = LinearRegression()
    model.fit(X, y)
    last_values = df['Close'].values[-n_lags:]
    pred = model.predict(last_values.reshape(1, -1))[0]
    return float(pred)
