#Import nessesary modules
import yfinance as yf
import pandas as pd
import json 
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import scipy.optimize as sci_plt
import streamlit as st
import holoviews as hv
hv.extension('bokeh')
%matplotlib inline

from pprint import pprint
from sklearn.preprocessing import StandardScaler


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
    
    return (crypto_price_df,stocks_price_df,commodities_price_df)







########   def main_func(api_pull:dict):

# Store data for each asset class in a dictionary
# Use .items()to iterate over the key-value pairs of the api_pull dictionary
# pull data for the number of years requested by the user
data = {}
for asset_class, tickers in api_pull.items():
    data[asset_class] = {}
    for ticker in tickers:
        data[asset_class][ticker] = yf.Ticker(ticker).history(start=selected_start_date, end=selected_end_date)

# Create a data frame for each asset class with the 'Close' column.
# Access the 'Close' column of the data for each asset class.
# Extract the values of the data dictionary and then access the 'Close' column of each dataframe.
crypto_price_df = pd.DataFrame({ticker: data['crypto_selected'][ticker]['Close'] for ticker in api_pull['crypto_selected']})
stocks_price_df = pd.DataFrame({ticker: data['stocks_selected'][ticker]['Close'] for ticker in api_pull['stocks_selected']})
commodities_price_df = pd.DataFrame({ticker: data['commodities_selected'][ticker]['Close'] for ticker in api_pull['commodities_selected']})

# Calculate .log() returns over time calculate the percent change .pct_change() for each asset class
crypto_log_returns = np.log(1 + crypto_price_df.pct_change())
stocks_log_returns = np.log(1 + stocks_price_df.pct_change())
commodities_log_returns = np.log(1 + commodities_price_df.pct_change())

# Generate random weights of assests for each asset class
crypto_random_wts = np.array(np.random.random(crypto_selected))
stocks_random_wts = np.array(np.random.random(stocks_selected))
commodities_random_wts = np.array(np.random.random(commodities_selected))

# Rebalance weights, so each assect class would wave 100% allocation 
# (would might have sligtly more then 100%, but it shouldn't effect the Monte Carlo that much)
crypto_rebalanced_wts = crypto_random_wts / np.sum(crypto_random_wts)
stocks_rebalanced_wts = stocks_random_wts / np.sum(stocks_random_wts)
commodities_rebalanced_wts = commodities_random_wts / np.sum(commodities_random_wts)

# Calculate expected returns for each asset class and annualize them
# Crypto is annnualized by 365 trading days
# Stocks and commodities are anualized by 252 trading days
crypto_expected_returns = np.sum((crypto_log_returns.mean() * crypto_rebalanced_wts) * 365)
stocks_expected_returns = np.sum((stocks_log_returns.mean() * stocks_rebalanced_wts) * 252)
commodities_expected_returns = np.sum((commodities_log_returns.mean() * commodities_rebalanced_wts) * 252)

# Calculate expected Volatility and anualize and calculate corelation matrix
# Transpose rebalanced weights
# Crypto is annnualized by 365 trading days
# Stocks and commodities are anualized by 252 trading days
crypto_expected_volatility = np.sqrt(np.dot(crypto_rebalanced_wts.T,
                             np.dot(crypto_log_returns.cov() * 365,crypto_rebalanced_wts)))

stocks_expected_volatility = np.sqrt(np.dot(stocks_rebalanced_wts.T,
                             np.dot(stocks_log_returns.cov() * 252,stocks_rebalanced_wts)))

commodities_expected_volatility = np.sqrt(np.dot(commodities_rebalanced_wts.T,
                                  np.dot(commodities_log_returns.cov() * 252,commodities_rebalanced_wts)))

# Calculate the Sharp Ratio for each asset class
crypto_sharp_ratio = crypto_expected_returns / crypto_expected_volatility
stocks_sharp_ratio = stocks_expected_returns / stocks_expected_volatility
commodities_sharp_ratio = commodities_expected_returns / commodities_expected_volatility

# Declare an array to store the weights for each of selected assets for for each asset class for itteratios of {num_of_portfolios}
crypto_all_weights = np.zeros((num_of_portfolios, crypto_selected))
stocks_all_weights = np.zeros((num_of_portfolios, stocks_selected))
commodities_all_weights = np.zeros((num_of_portfolios, commodities_selected))

# Define array to store the returns after they were generated, {num_of_portfolios} possible return values.
# The arrays are filled with zerroes, so when the Montecarlo simulation runs the zero values will be filled with values
crypto_ret_arr = np.zeros(num_of_portfolios)
stocks_ret_arr = np.zeros(num_of_portfolios)
commodities_ret_arr = np.zeros(num_of_portfolios)

# Define array to store the volatilities after they were generated, {num_of_portfolios} possible return values.
crypto_vol_arr = np.zeros(num_of_portfolios)
stocks_vol_arr = np.zeros(num_of_portfolios)
commodities_vol_arr = np.zeros(num_of_portfolios)

# Define array to store the sharpe ratios after they were generated, {num_of_portfolios} possible return values.
crypto_sharpe_ratio_arr = np.zeros(num_of_portfolios)
stocks_sharpe_ratio_arr = np.zeros(num_of_portfolios)
commodities_sharpe_ratio_arr = np.zeros(num_of_portfolios)


# Start the simulations.
for ind in range(num_of_portfolios):
    # Calculate the weights.
    crypto_weights = np.array(np.random.random(crypto_selected))
    crypto_weights = crypto_weights / np.sum(crypto_weights )
    
    stocks_weights = np.array(np.random.random(stocks_selected))
    stocks_weights = stocks_weights / np.sum(stocks_weights )
    
    commodities_weights = np.array(np.random.random(commodities_selected))
    commodities_weights = commodities_weights / np.sum(commodities_weights )
    
    # Add the weights, add to the `weights_arrays`.
    crypto_all_weights[ind, :] = crypto_weights
    stocks_all_weights[ind, :] = stocks_weights
    commodities_all_weights[ind, :] = commodities_weights
    
    # Calculate expected log returns, add to the `returns_array`.
    crypto_ret_arr[ind] = np.sum((crypto_log_returns.mean() * crypto_weights) * 365)
    stocks_ret_arr[ind] = np.sum((stocks_log_returns.mean() * stocks_weights) * 252)
    commodities_ret_arr[ind] = np.sum((commodities_log_returns.mean() * commodities_weights) * 252)
     
    # Calculate the volatility and add it to the volatility_array. 
    # Apply square root to calculate how each part of the portfolio contributes to the whole portfolio.
    # Take correlation between assets into consideration. 
    
    # crypto_vol_arr[ind] = np.sqrt(
    # np.dot(crypto_weights.T, np.dot(crypto_log_returns.cov() * 365, crypto_weights)))
    
    crypto_vol_arr[ind] = np.dot(crypto_weights.T, np.dot(crypto_log_returns.cov() * 365, crypto_weights))


    # stocks_vol_arr[ind] = np.sqrt(
    # np.dot(stocks_weights.T, np.dot(stocks_log_returns.cov() * 252, stocks_weights)))
    
    stocks_vol_arr[ind] = np.dot(stocks_weights.T, np.dot(stocks_log_returns.cov() * 252, stocks_weights))


    # commodities_vol_arr[ind] = np.sqrt(
    # np.dot(commodities_weights.T, np.dot(commodities_log_returns.cov() * 252, commodities_weights)))
    
    commodities_vol_arr[ind] = np.dot(commodities_weights.T, np.dot(commodities_log_returns.cov() * 252, commodities_weights))
        
    # Calculate Sharpe Ratio, add it to the `sharpe_ratio_array`.
    crypto_sharpe_ratio_arr[ind] = crypto_ret_arr[ind]/ crypto_vol_arr[ind]
    stocks_sharpe_ratio_arr[ind] = stocks_ret_arr[ind]/ stocks_vol_arr[ind]
    commodities_sharpe_ratio_arr[ind] = commodities_ret_arr[ind]/ commodities_vol_arr[ind]

 # Create data frame with the weights, the returns, the volatility, and the Sharpe Ratio for each asset class
crypto_simulations_data = [crypto_ret_arr, crypto_vol_arr, crypto_sharpe_ratio_arr, crypto_all_weights]
stocks_simulations_data = [stocks_ret_arr,  stocks_vol_arr,  stocks_sharpe_ratio_arr,  stocks_all_weights]
commodities_simulations_data = [commodities_ret_arr,  commodities_vol_arr,  commodities_sharpe_ratio_arr,  commodities_all_weights]

# Create a DataFrame from sim data and Transpose, so will look like our original one.
crypto_simulations_df = pd.DataFrame(data=crypto_simulations_data).T
stocks_simulations_df = pd.DataFrame(data=stocks_simulations_data).T
commodities_simulations_df = pd.DataFrame(data=commodities_simulations_data).T

# Give the columns names for crypto
crypto_simulations_df.columns = [
    'Returns',
    'Volatility',
    'Sharpe Ratio',
    'Portfolio Weights'
]

# Make sure the data types are correct, we don't want our floats to be strings.
# Infer data types to convert columns with mixed data types to their appropriate data types.
crypto_simulations_df = crypto_simulations_df.infer_objects()

# Find the Max Sharpe Ratio to find better portfoio that provides the largest risk-adjusted returns. 
crypto_max_sharpe_ratio = crypto_simulations_df.loc[crypto_simulations_df['Sharpe Ratio'].idxmax()]

# Find the minimum volatility from the simulations to identify a portfolio that takes on the least amount of risk.
crypto_min_volatility = crypto_simulations_df.loc[crypto_simulations_df['Volatility'].idxmin()]

crypto_max_sharpe_ratio_row = pd.Series({
    'Returns': crypto_max_sharpe_ratio['Returns'],
    'Volatility': crypto_max_sharpe_ratio['Volatility'],
    'Sharpe Ratio': crypto_max_sharpe_ratio['Sharpe Ratio'],
    'Portfolio Weights': crypto_max_sharpe_ratio['Portfolio Weights']
})

crypto_min_volatility_row = pd.Series({
    'Returns': crypto_min_volatility['Returns'],
    'Volatility': crypto_min_volatility['Volatility'],
    'Sharpe Ratio': crypto_min_volatility['Sharpe Ratio'],
    'Portfolio Weights': crypto_min_volatility['Portfolio Weights']
})
