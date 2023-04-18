import pandas as pd
import statistics
import numpy
import os

data = []
folder = "../twitterData/2020_03"

for filename in os.listdir(folder):
    if filename.endswith(".csv"):
        #print(os.path.join(folder, filename[:-4]))
        dataframe = pd.read_csv(os.path.join(folder, filename), header=None)
        #print(dataframe)
        dataframe = dataframe[1]
        data.append([filename[:-4].split('_')[0], statistics.mean(dataframe), statistics.stdev(dataframe)])
    else:
        continue

#dataframe=pd.read_csv("march20_march21.csv", header=None)
#dataframe=dataframe[1]
#print(statistics.mean(dataframe))
#print(statistics.stdev(dataframe))

print(data)

npArray = numpy.array(data)
numpy.savetxt('../firstWave/march.csv', npArray, delimiter=',', fmt='%s')

#dataframe.to_csv("ready_march20_march21.csv", index=False, header=None)