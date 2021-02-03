import pandas as pandas
import math as math
import matplotlib.pyplot as plt

# file = pandas.read_csv("C:/Users/miked/Documents/5000sin.csv")
# N = 1
# negative = True

def logarithm(file, N, negative):
    m = min(file.iloc[:, N])
    for i in range(len(file.iloc[:, N])):
        if negative == True:
            file.iloc[i, N] = math.log10(file.iloc[i, N] + abs(m) + 0.001)
        else:
            if file.iloc[i, N] > 0:
                file.iloc[i, N] = math.log10(file.iloc[i, N])
            else:
                file.iloc[i, N] = float('NaN')
    return file
#
# log(file, N, False)
#
# plt.plot(file.iloc[:, N])
