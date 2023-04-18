import pandas as pd
import statistics
import numpy
import os

data = []
folder = "../twitterData"
count = 0
filenum = 0
maxfile = ""
minfile = ""
maxnum = 0
minnum = 1200
filedata = []

for foldername in os.listdir(folder):
    target = os.path.join(folder, foldername)
    if foldername != ".DS_Store" and foldername != "FaultyFiles":
        for filename in os.listdir(target):
            if filename.endswith(".csv"):
                #print(os.path.join(target, filename))
                dataframe = pd.read_csv(os.path.join(target, filename), header=None)
                if len(dataframe.index) > maxnum:
                    maxnum = len(dataframe.index)
                    maxfile = filename.split("_")[0]
                elif len(dataframe.index) < minnum:
                    minnum = len(dataframe.index)
                    minfile = filename.split("_")[0]
                count += len(dataframe.index)
                filenum += 1
                filedata.append([filename.split("_")[0], len(dataframe.index)])
            else:
                continue
    else:
        continue

print(count)
print(filenum)
print(maxfile, maxnum)
print(minfile, minnum)

print(sorted(filedata,key=lambda l:l[1], reverse=True))
