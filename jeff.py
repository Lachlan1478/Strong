import statistics

import pandas as pd


class Init():
    def __init__(self, data):
        self.data = data

    def getTarget(self, data, bound):
        temp = []
        for i in range(0, len(data)):
            if (data[i] >= bound):
                temp.append(1)
            else:
                temp.append(0)
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

        df = pd.DataFrame(risk)
        return df

    def Features(self):
        FeatureNames = ['5dStdev', '10dStdev', 'PctChange', 'VolumePct']
        self.data['PctChange'] = self.data['Close'].pct_change(5)
        self.data['5dFutPct'] = self.data['PctChange'].shift(5)
        self.data[FeatureNames[0]] = self.getStdev(self.data['5dFutPct'], 5)
        self.data[FeatureNames[1]] = self.getStdev(self.data['5dFutPct'], 10)
        self.data['VolumePct'] = self.data['Volume'].pct_change(5)

        self.data['Target'] = self.getTarget(self.data['5dFutPct'], 0.01)
        print(self.data['Target'])