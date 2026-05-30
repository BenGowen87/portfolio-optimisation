import yfinance as yf
import pandas as pd
import numpy as np

def get_downloaded_data():
    # Download stock price data for each asset
    tickers = ["AAPL", "MSFT", "NVDA", "SPY"]

    data = yf.download(
        tickers,
        start="2019-01-01",
        end="2024-01-01"
    )
    
    return data


def get_returns_data():
    # Download stock price data again
    data = get_downloaded_data()

    # Create a DataFrame containing daily returns for each asset
    returns_df = pd.DataFrame(data["Close"].squeeze().pct_change())

    # drops the first row of the dataframe as null values for the first day
    returns_df = returns_df.dropna()

    return returns_df


def get_simulated_portfolios():
    from src.data_utils import get_returns_data

    #gets the returns data frame
    returns_df = get_returns_data()
    #caluclates the mean returns for each asset
    mean_returns = returns_df.mean()
    #creates the covariance matrix between each of the assets
    cov_matrix = returns_df.cov()

    #simulate the portfolios
    num_portfolios = 10000

    portfolio_returns = []
    portfolio_volatilities = []
    portfolio_weights = []
    portfolio_sharpe_ratios = []

    for i in range(num_portfolios):
        weights = np.random.random(4)
        weights = weights / np.sum(weights)

        portfolio_return = np.sum(mean_returns * weights)

        portfolio_volatility = np.sqrt(
            np.dot(weights.T, np.dot(cov_matrix, weights))
        )

        sharpe_ratio = portfolio_return / portfolio_volatility

        portfolio_returns.append(portfolio_return)
        portfolio_volatilities.append(portfolio_volatility)
        portfolio_weights.append(weights)
        portfolio_sharpe_ratios.append(sharpe_ratio)


    # create a data frame storing the portfolio return and portfolio volatility for each simulated portfolio
    portfolio_results = pd.DataFrame({
        "Return": portfolio_returns,
        "Volatility": portfolio_volatilities,
        "Apple Weight": [w[0] for w in portfolio_weights],
        "Microsoft Weight": [w[1] for w in portfolio_weights],
        "Nvidia Weight": [w[2] for w in portfolio_weights],
        "S&P500 Weight": [w[3] for w in portfolio_weights],
        "Sharpe ratio": portfolio_sharpe_ratios
    })

    return portfolio_results