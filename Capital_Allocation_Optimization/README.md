# Capital_Allocation_Optimization

# Project Title

The objective of this sub-project is to collect, clean, and analyze data for 3 different assets: crypto, commodities, and stocks. The data will be pulled from Yahoo Fiance using Pandas, Numpy and matplotlib will be used for data analysis and visualization. The aim is to pull historical data from one to ten years, decide on an amount to invest in, once done, the user will be able to pick from two different portfolios, the first portfolio will have the maximum Sharpe ratio, giving insight to a portfolio with higher probable returns and higher risk, while the other portfolio will have the minimum volatility having lower returns  and lower risk.


---

## Technologies

This application is written with Python 3.7 and uses:
   * Jupyter notebook
   * pandas library
   * pathlib module
   * %matplotlib inline
   * streamlit
   * Holoviews
   * Numpy
   * Scipy
   * yfinance
   * Streamlit
   

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
3. To install Pandas library:
```python
conda pip install pandas
```
4. To install yfinance:
```python
conda pip install yfinace
```
5. To install streamlit:
```python
conda pip install streamlit
```
4.Open **capital_allocation_optimization.ipynb** file in Jupyter notebook.  
  
---

## Instructions

User will be prompted to input the amount of capital to invest, once entered press "Enter". Next the user will be prompted to input how many years they would like their analysis to cover, once entered, press "Enter". User will then be provided with Returns, Volatility, Sharpe ratios, and potfolio weight distribution for three asset classes: Crypto, Stocks, and Commodities. The user will also be shown visualizations illustrating max & min volatility on scatter plots which show projected Portfolio returns against risk. Thus user can then use this model to decide how much money they would like to invest based on the information provided.

---

## Contributors
Alexander Likhachev, Alphonso Logan, Cary Gutknecht, Markeis Reed, Julio Rodriguez 
---

## License

MIT

Copyright 2023 CAPTS TEAM

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.