#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic04.data", names=cols) #data frame = df
df["class"] = (df["class"] == "g").astype(int)

# Test
# print(df.head())

#for label in cols[:-1] :
#    plt.hist(df[df["class"]==1][label], color='blue', label='gamma', alpha=0.7, density=True)
#    plt.hist(df[df["class"]==0][label], color='red', label='gamma', alpha=0.7, density=True)
#    plt.title(label)
#    plt.ylabel("Probability")
#    plt.xlabel(label)
#    plt.legend()
#    plt.show()

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df)) ])

def scale_datset (dataframe, oversample=False) :
    x = dataframe[dataframe.columns[:-1]].values # Input vector values for a line 
    y = dataframe[dataframe.columns[-1]].values # Output result value (class) for the x vector line

    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    if oversample :
        ros = RandomOverSampler()
        x, y = ros.fit_resample(x,y)
        
    data = np.hstack( (x, np.reshape(y, (len(y), 1))) )

    return data, x, y


# Tests
# print (len (train[train["class"] == 1])) #gama
# print (len (train[train["class"] == 0]))

train, x_train, y_train = scale_datset (train, oversample=True)
valid, x_train, y_train = scale_datset (valid, oversample=False)
test, x_train, y_train = scale_datset (test, oversample=False)

# test
# print (len (y_train))
# print(sum (y_train == 1))
# print(sum (y_train == 0))
