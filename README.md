# CAPTS:_Comprehensive_Allocation_and_Portfolio_Trading_Solution

This project aims to provide a comprehensive and integrated solution for portfolio allocation, financial analysis and algorithmic trading of three asset classes (crypto, commodities, stocks), consisting of the following sub-projects:

## Sub-Project 1: Capital Allocation Optimization
The objective of this project is to gather, clean, and analyze data for crypto, commodities, and stocks, leveraging financial APIs such as CoinMarketCap and CryptoCompare with Pandas. The data will be structured and saved in JSON format, and analyzed and visualized with Numpy and PyViz. The analyzed data will be stored in SQL for future use.

## Sub-Project 2: Machine Learning for Portfolio Optimization
In this project, machine learning algorithms will be applied to analyze and optimize the portfolio. Techniques such as linear regression, decision trees, and clustering will be used to identify patterns and make predictions about future price movements. Financial metrics, such as Sharpe ratio and Sortino ratio, will also be employed to evaluate and optimize the portfolio.

## Sub-Project 3: GRID Bot for Backtesting and Trading
In this project, a GRID bot will be developed for backtesting and bug fixing using a paper trading platform. The bot will use the data collected in the first project and insights from the second project to make trades based on various financial strategies, including mean reversion and trend following. The bot's performance will be optimized through algorithmic trading strategies.






---

## Technologies

This application is written with Python 3.7 and uses:
   * Jupyter notebook
   * pandas library
   * pathlib module
   * %matplotlib inline
   * yfinance
   

---

## Installation Guide

1. To ceate new conda development environment run the following code in terminal :
```python
conda create --name anaconda
```
2. To install Jupyter lab: 
```python
conda pip install jupyterlab
```
3. To install Pandass lybrarie:
```python
conda pip install pandas
```
4. To install yfinance:
```python
conda pip install yfinance

```
5.Open **CAPTS-Comprehensive_Allocation_and_Portfolio_Trading_Solution** file in Jupyter notebook.  
  
---

## Instructions



---

## Contributors
Alexander Likhachev, Alphonso Logan, Cary Gutknecht, Markeis Reed, Julio Rodriguez




---

## License

MIT

Copyright (c) [2023] [CAPTS]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
