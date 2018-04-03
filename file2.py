from statistics import mode
import csv
import pandas as pd


mergedfr = pd.read_csv("mergedfr.csv")
D1={'placeid':[],'rating':[],'payment':[],'lat':[],'long':[],'name':[],'price':[],'smoking_area':[],'cuisine':[]}
D2={'placeid':[],'rating':[],'payment':[],'lat':[],'long':[],'name':[],'price':[],'smoking_area':[],'cuisine':[]}

for index, row in mergedfr.iterrows():
    D1['placeid'].append(row[0])
    D1['rating'].append(row[1])
    D1['payment'].append(row[2])
    D1['lat'].append(row[3])
    D1['long'].append(row[4])
    D1['name'].append(row[5])
    D1['price'].append(row[6])
    D1['smoking_area'].append(row[7])
    D1['cuisine'].append(row[8])

for index, row in mergedfr.iterrows():
    D2['placeid'].append(row[0])
    D2['rating'].append("%.2f" % row[1])


    if (row[2][2] == '?'):
        D2['payment'].append(['cash'])
    else:
        D2['payment'].append(row[2])

    D2['lat'].append(row[3])
    D2['long'].append(row[4])
    D2['name'].append(row[5])

    if (row[6][2] == '?'):
        D2['price'].append(mode(D1['price']))
    else:
        D2['price'].append(row[6])

    D2['smoking_area'].append(row[7])

    if (row[8][2] == '?'):
        D2['cuisine'].append(mode(D1['cuisine']))
    else:
        D2['cuisine'].append(row[8])

df = pd.DataFrame(D2)
df.to_csv('mergedfru.csv', sep=',')