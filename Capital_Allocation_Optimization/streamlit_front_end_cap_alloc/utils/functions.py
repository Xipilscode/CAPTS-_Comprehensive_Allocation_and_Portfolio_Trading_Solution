#Import nessesary modules
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import scipy.optimize as sci_plt
import streamlit as st
import holoviews as hv
hv.extension('bokeh')
# %matplotlib inline



# from pprint import pprint
# from sklearn.preprocessing import StandardScaler


# Define trading days constant
CRYPTO_TRADING_DAYS = 365
STOCKS_COMMODITIES_TRADING_DAYS = 252


def fetch_asset_data(api_pull: dict, selected_start_date, selected_end_date) -> dict:
    """Fetches historical data for selected assets based on the api_pull dictionary
    
    Args:
    api_pull (dict): a dictionary containing selected asset classes and their respective tickers
    selected_start_date (str): selected start date of the historical data 
    selected_end_date (str): selected end date of the historical data 
    
    Returns:
    dict: a dictionary containing asset class names as keys and their respective price data as Pandas dataframes
    """
    data = {}
    for asset_class, tickers in api_pull.items():
        data[asset_class] = {}
        for ticker in tickers:
            data[asset_class][ticker] = yf.Ticker(ticker).history(start=selected_start_date, end=selected_end_date)
        
    return data


def create_price_df(data: dict, api_pull: dict):
    """Creates a dataframe for each asset class with the 'Close' column
    
    Args:
    data (dict): a dictionary containing asset class names as keys and their respective price data as Pandas dataframes
    api_pull (dict): a dictionary containing selected asset classes and their respective tickers
    
    Returns:
    DataFrame:  DataFrames for asset classes and their respective price dataframes with the 'Close' column
    """
    crypto_price_df = pd.DataFrame({ticker: data['crypto'][ticker]['Close'] for ticker in api_pull['crypto']})
    stocks_price_df = pd.DataFrame({ticker: data['stocks'][ticker]['Close'] for ticker in api_pull['stocks']})
    commodities_price_df = pd.DataFrame({ticker: data['commodities'][ticker]['Close'] for ticker in api_pull['commodities']})
    
    return crypto_price_df,stocks_price_df,commodities_price_df

def calculate_log_returns(crypto_price_df, stocks_price_df, commodities_price_df):
    """
    Calculate the log returns for each asset class dataframe.

    Args:
        crypto_price_df (DataFrame): DataFrame of cryptocurrency prices.
        stocks_price_df (DataFrame): DataFrame of stock prices.
        commodities_price_df (DataFrame): DataFrame of commodity prices.

    Returns:
        tuple: A tuple of pandas.DataFrame objects containing the log returns for each asset class.
    """

    crypto_log_returns = np.log(1 + crypto_price_df.pct_change())
    stocks_log_returns = np.log(1 + stocks_price_df.pct_change())
    commodities_log_returns = np.log(1 + commodities_price_df.pct_change())
    return crypto_log_returns, stocks_log_returns, commodities_log_returns


def generate_random_weights(selected_tickers):
    """
    Generates an array of random weights for a given number of tickers.

    Args:
    - selected_tickers: int. The number of tickers for which the weights need to be generated.

    Returns:
    - numpy array of shape (selected_tickers,). An array of random weights between 0 and 1.
    """
    random_weights = np.array(np.random.random(selected_tickers))
    return random_weights

def rebalance_weights(random_wts):
    """
    Rebalances the given array of random weights so that each asset class has a 100% allocation.

    Args:
    - random_wts: numpy array. The array of random weights to be rebalanced.

    Returns:
    - numpy array. The rebalanced array of weights, where each asset class has a 100% allocation.
    """
    # Divide each weight by the sum of all weights to get the percentage allocation for each asset class
    rebalanced_wts = random_wts / np.sum(random_wts)
    return rebalanced_wts

def calculate_expected_returns(log_returns, rebalanced_wts):
    """
    Calculate expected returns for an asset class and annualize them
    param log_returns: numpy array of log returns for an asset class
    param rebalanced_wts: numpy array of weights for each asset in the asset class
    return: expected returns for the asset class
    Crypto is annnualized by 365 trading days
    Stocks and commodities are anualized by 252 trading days
    """
    if log_returns is crypto_log_returns and rebalanced_wts is crypto_rebalanced_wts:
        trading_days = CRYPTO_TRADING_DAYS
    else:
        trading_days = STOCKS_COMMODITIES_TRADING_DAYS

    expected_returns = np.sum((log_returns.mean() * rebalanced_wts) * trading_days)

    return expected_returns

def calculate_expected_volatility(log_returns, rebalanced_wts):
    """
    Calculates the expected volatility based on the logarithmic returns and rebalanced weights.

    Parameters:
    log_returns (pandas.DataFrame): A DataFrame containing the logarithmic returns for the asset.
    rebalanced_wts (numpy.ndarray): An array containing the rebalanced weights for the asset.

    Returns:
    expected_volatility (float): The expected volatility for the asset.
    """

    if log_returns is crypto_log_returns and rebalanced_wts is crypto_rebalanced_wts:
        trading_days = CRYPTO_TRADING_DAYS
    else:
        trading_days = STOCKS_COMMODITIES_TRADING_DAYS

    expected_volatility = np.sqrt(np.dot(rebalanced_wts.T,
                             np.dot(log_returns.cov() * trading_days, rebalanced_wts)))

    return expected_volatility

def calculate_sharpe_ratio(expected_returns, expected_volatility):
    """
    Calculates the Sharpe Ratio given expected returns and volatility.

    Args:
    expected_returns (float): The expected return of the asset.
    expected_volatility (float): The expected volatility of the asset.

    Returns:
    float: The Sharpe Ratio of the asset.
    """
    sharpe_ratio = expected_returns / expected_volatility
    return sharpe_ratio

# Monte Carlo simulation
def mc_sim(num_of_portfolios, log_returns, num_selected_tickers):
    """
    Initializes the Monte Carlo simulation.
    Initializes the arrays used in the Monte Carlo simulation.
    """
    # Declare an array to store the weights for each selected asset for each asset class
    all_weights = np.zeros((num_of_portfolios, num_selected_tickers))
    
    # Define arrays to store the returns, volatilities, and Sharpe ratios for each asset class
    ret_arr = np.zeros(num_of_portfolios)
    vol_arr = np.zeros(num_of_portfolios)
    sharpe_ratio_arr = np.zeros(num_of_portfolios)
    
    # Run the Monte Carlo simulation
    for ind in range(num_of_portfolios):
        
        # Calculate the weights.
        weights = np.array(np.random.random(num_selected_tickers))
        weights = weights / np.sum(weights)

        # Add the weights, add to the `weights_arrays`.
        all_weights[ind, :] = weights

        # Calculate expected log returns, add to the `returns_array`.
        if ret_arr is crypto_ret_arr:
            ret_arr[ind] = np.sum((log_returns.mean() * weights) * CRYPTO_TRADING_DAYS)
        else: 
            ret_arr[ind] = np.sum((log_returns.mean() * weights) * STOCKS_COMMODITIES_TRADING_DAYS)

        # Calculate the volatility and add it to the volatility_array. 
        # Apply square root to calculate how each part of the portfolio contributes to the whole portfolio.
        # Take correlation between assets into consideration. 
        if vol_arr is crypto_vol_arr:
            vol_arr[ind] = np.dot(weights.T, np.dot(log_returns.cov() * CRYPTO_TRADING_DAYS, weights))
        else:
            vol_arr[ind] = np.dot(weights.T, np.dot(log_returns.cov() * STOCKS_COMMODITIES_TRADING_DAYS, weights))

        sharpe_ratio_arr[ind] = ret_arr[ind] / vol_arr[ind]
    
    return all_weights, ret_arr, vol_arr, sharpe_ratio_arr
    



