# portfolio-optimisation

## Project overview

This project investigates portfolio optimisation using historical stock market data from Apple (AAPL), Microsoft (MSFT), Nvidia (NVDA) and the S&P 500 ETF (SPY). Using Python, historical price data is downloaded and analysed to calculate returns, volatility, correlation and covariance between assets.

The project then applies principles from Modern Portfolio Theory to simulate thousands of portfolios with different asset weightings. Portfolio risk and return are evaluated, the Sharpe ratio is used to identify attractive portfolios, and the efficient frontier is constructed to visualise the optimal trade-off between risk and return.

## Key Objectives

- Download and process historical stock market data.
- Calculate and analyse daily returns.
- Compare asset risk using volatility.
- Investigate relationships between assets using correlation and covariance.
- Simulate thousands of portfolios with different asset allocations.
- Identify minimum volatility, maximum return and maximum Sharpe ratio portfolios.
- Construct and analyse the efficient frontier.

## Project structure

Notebook 1 - this notebook downloads stock market data for 4 assests(Apple, Microsoft, Nvdia, S&P500) from Yahoo finance and I plot the closing price of the stock against time.

Notebook 2 - this notebook first analyses the returns for the apples stock by calculating the daily percentage return in which I ploted this against timed and then caluclate its volitilty and its mean. I then repeated the process with the 4 other assets.

Notebook 3 - this notebook calulates the correlation matrix between the 4 assets and created a heat map to visualise the matrix.

Notebook 4 - this notebook first starts by finding the covaraince matrix between the assets and then simulating a portfolio with different weights invested in the 4 assets and calculated the expected daily return and the portfolio volatility. I then similated 10000 portfolios drawing a graph of expected daily return against the portfolios volatility and I analysed the portfolios with the greatest expected return and lowest volatility. I then calulated the sharpe ratio of each of the portfolio and re-drew the graph to show where the highest sharpe ratios appear on the graph.

Notebook 5 - this notebook first finds the most efficient simulated portfolios based on a given level of risk. I then re-drew the graph from notebook 4 to show where the efficient portfolios lie on the graph.

## Limitations

- When calculating the sharpe ratio I assumed the risk free return is 0 where in reality it would not be.
- Only 4 assets where used and analysed.
- I only analysed the data from 2019 to 2024 which means it may not predict future returns

## Extensions

- Use treasury yeilds to get a more accurate value for the risk free return
- Use more than 4 assets in my analysis

## Technologies used

- python
- pandas
- numPy
- Matplotlib
- yfinance

## Keyfindings

- Nvidia achieved the highest average returns but also exhibited the greatest volatility.
- The S&P 500 ETF demonstrated lower risk than the individual technology stocks.
- Diversification reduced portfolio volatility through imperfect correlations between assets.
- The maximum Sharpe ratio portfolio provided the best risk-adjusted return.
- The efficient frontier illustrated the trade-off between portfolio risk and expected return.