from __future__ import division
import csv
import pandas as pd


#Reading UserProfile
userpro = "userprofile.csv"
fields = []
rows = []
with open(userpro, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)
D0 = {'userid':[],'lat':[],'long':[],'smoker':[],'budget':[]}
#print("Total no. of rows: %d"%(csvreader.line_num))
for row in rows[:csvreader.line_num]:
    #print(row[0],row[1],row[2],row[3],row[17])
    D0['userid'].append(row[0])
    D0['lat'].append(row[1])
    D0['long'].append(row[2])
    D0['smoker'].append(row[3])
    D0['budget'].append(row[17])
    #print('\n')
df = pd.DataFrame(D0)
grouped0 = df.groupby('userid').agg(lambda x: x.tolist())







#Reading UserCuisine
usercui = "usercuisine.csv"
fields = []
rows = []
with open(usercui, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

D1 = {'userid':[],'cuisine':[]}
#print("Total no. of rows: %d"%(csvreader.line_num))
for row in rows[:csvreader.line_num]:
    #print(row[0],row[1])
    D1['userid'].append(row[0])
    D1['cuisine'].append(row[1])
    #print('\n')
#print (D1)


df = pd.DataFrame(D1)
grouped1 = df.groupby('userid').agg(lambda x: x.tolist())




#Reading UserPay
userpay = "userpayment.csv"
fields = []
rows = []
with open(userpay, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

#print("Total no. of rows: %d"%(csvreader.line_num))


D2 = {'userid':[],'payment':[]}
#print("Total no. of rows: %d"%(csvreader.line_num))
for row in rows[:csvreader.line_num]:
    #print(row[0],row[1])
    D2['userid'].append(row[0])
    D2['payment'].append(row[1])
    #print('\n')
#print (D2)
df = pd.DataFrame(D2)
grouped2 = df.groupby('userid').agg(lambda x: x.tolist())



F0 = grouped0.T.to_dict()
F1 = grouped1.T.to_dict()
F2 = grouped2.T.to_dict()



grouped0.to_csv('a.csv', sep=',')
grouped1.to_csv('b.csv', sep=',')
grouped2.to_csv('c.csv', sep=',')

p = pd.read_csv("a.csv")
q = pd.read_csv("b.csv")
r = pd.read_csv("c.csv")
merged = p.merge(q, on="userid", how="inner")
merged.to_csv("merged.csv", index=False)

t = pd.read_csv("merged.csv")
mergedf = r.merge(t, on="userid",how="inner")
mergedf.to_csv("mergedf.csv", index=False)











#Resturant
userpro = "geoplaces2.csv"
fields = []
rows = []
with open(userpro, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)
D0 = {'placeid':[],'lat':[],'long':[],'name':[],'smoking_area':[],'price':[]}
#print("Total no. of rows: %d"%(csvreader.line_num))
for row in rows[:csvreader.line_num]:
    #print(row[0],row[1],row[2],row[4],row[12],row[15])
    D0['placeid'].append(row[0])
    D0['lat'].append(row[1])
    D0['long'].append(row[2])
    D0['name'].append(row[4])
    D0['smoking_area'].append(row[12])
    D0['price'].append(row[15])
    #print('\n')
df = pd.DataFrame(D0)
grouped0 = df.groupby('placeid').agg(lambda x: x.tolist())
#print grouped0





#Reading ResturantCuisine
usercui = "chefmozcuisine.csv"
fields = []
rows = []
with open(usercui, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

D1 = {'placeid':[],'cuisine':[]}
#print("Total no. of rows: %d"%(csvreader.line_num))
for row in rows[:csvreader.line_num]:
    #print(row[0],row[1])
    D1['placeid'].append(row[0])
    D1['cuisine'].append(row[1])
    #print('\n')
#print (D1)


df = pd.DataFrame(D1)
grouped1 = df.groupby('placeid').agg(lambda x: x.tolist())
#print grouped1



#Reading ResturantPayment
userpay = "chefmozaccepts.csv"
fields = []
rows = []
with open(userpay, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

D2 = {'placeid':[],'payment':[]}
#print("Total no. of rows: %d"%(csvreader.line_num))
for row in rows[:csvreader.line_num]:
    #print(row[0],row[1])
    D2['placeid'].append(row[0])
    D2['payment'].append(row[1])
    #print('\n')
#print (D2)
df = pd.DataFrame(D2)
grouped2 = df.groupby('placeid').agg(lambda x: x.tolist())

#print grouped2



#Ratings
userrat = "rating_final.csv"
fields = []
rows = []
with open(userrat, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

D1 = {'placeid':[],'rating':[]}

for row in rows[:csvreader.line_num]:

    D1['placeid'].append(row[1])
    agg = int(row[2])+int(row[3])+int(row[4])
    rat = (agg/3)
    norm = (rat/2 )*(5)  #result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value) normalise for 0-1
    D1['rating'].append(norm)


df = pd.DataFrame(D1)
grouped3 = df.groupby('placeid').mean()















F0 = grouped0.T.to_dict()
F1 = grouped1.T.to_dict()
F2 = grouped2.T.to_dict()
F3 = grouped3.T.to_dict()



grouped0.to_csv('x.csv', sep=',')
grouped1.to_csv('y.csv', sep=',')
grouped2.to_csv('z.csv', sep=',')
grouped3.to_csv('w.csv', sep=',')

p = pd.read_csv("x.csv")
q = pd.read_csv("y.csv")
r = pd.read_csv("z.csv")
s = pd.read_csv("w.csv")


merged = p.merge(q, on="placeid", how="inner")
merged.to_csv("mergedr.csv", index=False)

t = pd.read_csv("mergedr.csv")
mergedf = r.merge(t, on="placeid",how="inner")
mergedf.to_csv("mergedfr.csv", index=False)

t = pd.read_csv("mergedfr.csv")
mergedf = s.merge(t, on="placeid",how="inner")
mergedf.to_csv("mergedfr.csv", index=False)










