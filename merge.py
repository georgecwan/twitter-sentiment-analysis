import pandas as pd
import statistics
import numpy
import os

data = []
folder = '/Users/georgew/PycharmProjects/apResearch/firstWave'

for filename in os.listdir(folder):
    if filename.endswith(".csv"):
        print(os.path.join(folder, filename))
        dataframe = pd.read_csv(os.path.join(folder, filename), header=None)
        #print(dataframe)
        data.append(dataframe)
    else:
        continue

final = pd.concat(data)

print(final)

npArray = numpy.array(final)
numpy.savetxt('data.csv', npArray, delimiter=',', fmt='%s')