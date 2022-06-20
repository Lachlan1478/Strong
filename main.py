from fastquant import get_crypto_data, get_stock_data
#import Setup
#import NeuralNet
from cryptocmd import CmcScraper
import pandas as pd
import jeff


def getData(Ticker, Start, End, Crypto = True):
    if(Crypto):
        data1 = CmcScraper("BTC", Start, End)
        data = data1.get_dataframe()
    else:
        data = get_stock_data(Ticker, Start, End)
    return data


def main():
    BTC = getData("BTC/USDT", "01-01-2020", "01-01-2022")
    #Reverse data to chronological order
    BTC = BTC.iloc[::-1]

    data = pd.DataFrame(BTC)
    print(BTC)

    Model = jeff.Init(BTC)
    Model.Features()


    #ORG = getData("ORG.AX", "2020-01-01", "2022-01-01", Crypto=False)

    #M1 = Setup.Init(BTC)
    #M1.Features()

    #Model1 = NeuralNet.NN(BTC)
    #Model1.M1()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
