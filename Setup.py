import pandas as pd
import statsmodels as sm
import statistics
import json

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


class Init():
    def __init__(self, data):
        self.data = data

    def oneHot(self, data):
        ### Categorical data to be converted to numeric data
        ### integer mapping using LabelEncoder
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(data)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)

        ### One hot encoding
        onehot_encoder = OneHotEncoder(sparse=False)
        onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

        print(onehot_encoded)

        return onehot_encoded


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

            jeff = pd.dataframe(('stddev' + str(period)) = risk)
            print(jeff)
        return risk

    def Features(self):
        # Features
        FeatureNames = ['5dStdev', '10dStdev', 'PctChange', 'VolumePct']
        self.data['PctChange'] = self.data['Close'].pct_change(5) *100
        self.data['5dFutPct'] = self.data['PctChange'].shift(5)
        self.data[FeatureNames[0]] = self.getStdev(self.data['5dFutPct'], 5)
        self.data[FeatureNames[1]] = self.getStdev(self.data['5dFutPct'], 10)
        self.data['VolumePct'] = self.data['Volume'].pct_change(5)*100

        self.data['Target'] = self.getTarget(self.data['5dFutPct'], 0.01)
        print(self.data['Target'])
        self.data.dropna()
        self.data = self.data.sample(frac=1) # shuffle data

        Features = self.data[FeatureNames]

        #self.data.to_csv('file_name.csv')

        Target = self.data['Target']

        size = int(0.7 * Features.shape[0])

        trainFeat = Features[:size]
        testFeat = Features[size:]

        trainTarg = Target[:size]
        testTarg = Target[size:]

        return trainFeat, testFeat, trainTarg, testTarg