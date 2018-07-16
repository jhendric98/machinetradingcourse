import pandas as pd
import matplotlib.pyplot as plt


def max_close(symbol):
    """Return the max Close for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df.Close.max()


def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data

    return df["Volume"].mean()


def test_run():
    df = pd.read_csv('data/AAPL.csv')
    print(df.head())
    print(df.tail(5))
    print(df[10:21])
    print(max_close('AAPL'))

    print(get_mean_volume('IBM'))

    df['Adj Close'].plot()
    plt.show()


if __name__ == '__main__':
    test_run()