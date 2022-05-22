from fastquant import get_crypto_data, get_stock_data
import Setup
from cryptocmd import CmcScraper


def getData(Ticker, Start, End, Crypto = True):
    if(Crypto):
        data1 = CmcScraper("BTC", Start, End)
        data = data1.get_dataframe()
        print(data)
        print("here")
    else:
        data = get_stock_data(Ticker, Start, End)
    return data


def main():
    BTC = getData("BTC/USDT", "01-01-2020", "01-01-2022")

    #ORG = getData("ORG.AX", "2020-01-01", "2022-01-01", Crypto=False)
    print(BTC)

    M1 = Setup.Init(BTC)
    a,b,c,d = M1.Features()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
