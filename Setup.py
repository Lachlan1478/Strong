import pandas as pd
import statsmodels as sm
import statistics


class Init():
    def __init__(self, data):
        self.data = data

    def getTarget(self, data, bound):
        temp = []
        for i in range(0, len(data)):
            if (data[i] > bound):
                temp.append(2)
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
        #Target
        Target = self.getTarget(self.data['5dFutPct'], 1)

        #Features
        FeatureNames = ['5dStdev', '10dStdev', 'Close', 'Volume', 'Market Cap']
        self.data[FeatureNames[0]] = self.getStdev(self.data['5dFutPct'], 5)
        self.data[FeatureNames[1]] = self.getStdev(self.data['5dFutPct'], 10)

        Features = self.data[FeatureNames]

        size = int(0.7 * Features.shape[0])

        trainFeat = Features[:size]
        testFeat = Features[size:]

        size = int(0.7 * Target.shape[0])

        trainTarg = Target[:Target]
        testTarg = Target[Target:]

        return trainFeat, testFeat, trainTarg, testTarg