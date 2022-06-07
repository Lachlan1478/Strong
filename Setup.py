import pandas as pd
import statsmodels as sm
import statistics
import json


class Init():
    def __init__(self, data):
        self.data = data

    def getTarget(self, data, bound):
        temp = []
        for i in range(0, len(data)):
            if (data[i] >= bound):
                temp.append(1)
            elif (data[i] < -bound):
                temp.append(0)
            else:
                temp.append(1)
        return temp

    def getStdev(self, data, period):
        risk = []
        for i in range(0, len(data)):
            if (i < period - 1):
                risk.append('NaN')
            else:
                temp = []
                for j in range(0, period):
                    temp.append(data[i - j])
                risk.append(statistics.stdev(temp))
        return risk

    def Features(self):

        self.data['5dFutPct'] = self.data['Close'].pct_change(5)
        # Features
        FeatureNames = ['5dStdev', '10dStdev', 'Close', 'Volume', 'Market Cap']
        self.data[FeatureNames[0]] = self.getStdev(self.data['5dFutPct'], 5)
        self.data[FeatureNames[1]] = self.getStdev(self.data['5dFutPct'], 10)

        self.data['Target'] = self.getTarget(self.data['5dFutPct'], 0)
        self.data.dropna()
        self.data = self.data.sample(frac=1) # shuffle data

        print(self.data)

        Features = self.data[FeatureNames]

        #self.data.to_csv('file_name.csv')

        Target = self.data['Target']

        size = int(0.7 * Features.shape[0])

        trainFeat = Features[:size]
        testFeat = Features[size:]

        trainTarg = Target[:size]
        testTarg = Target[size:]

        return trainFeat, testFeat, trainTarg, testTarg