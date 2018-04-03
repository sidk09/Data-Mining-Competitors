from statistics import mode
import csv
import pandas as pd


mergedf = pd.read_csv("mergedf.csv")
D={'userid':[],'payment':[],'budget':[],'lat':[],'long':[],'smoker':[],'cuisine':[]}

for index, row in mergedf.iterrows():
    D['userid'].append(row[0])
    D['payment'].append(row[1])
    D['budget'].append(row[2])
    D['lat'].append(row[3])
    D['long'].append(row[4])
    D['smoker'].append(row[5])
    D['cuisine'].append(row[6])

print mergedf

for index, row in mergedf.iterrows():
    if (row[1][2]=='?'):
        row[1] = ['cash']

    if (row[2][2]=='?'):
        row[2] = mode(D['budget'])

    if (row[5][2] == '?'):
        row[5] = mode(D['smoker'])

print mergedf
mergedf.to_csv("mergedfu.csv")