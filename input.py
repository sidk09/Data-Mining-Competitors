import pandas as pd
import geopy.distance
import re

id = raw_input('Enter place id for which you want competitors: ')
id = int(id)
exist = pd.read_csv('mergedfru.csv')


D={}
for index, row in exist.iterrows():
    D[row[6]]=[row[2],row[3]]

cuisine=""
rating=""
price=""
payment=""
smoking=""

for index, row in exist.iterrows():
    if(id==row[6]):
        cuisine = row[1]
        rating = row[8]
        price = row[7]
        payment = row[5]
        smoking = row[9]





try:

    D[id]

    lat = D[id][0][2:9]
    long = D[id][1][2:9]

    lat = float(lat)
    long = float(long)


    r_comp = {'rid':[]}

    for x in D.keys():

        lat1 = D[x][0][2:9]
        long1 = D[x][1][2:9]
        lat1 = float(lat1)
        long1 = float(long1)
        coords_1 = (lat, long)
        coords_2 = (lat1, long1)
        if geopy.distance.vincenty(coords_1, coords_2).km < 5 and geopy.distance.vincenty(coords_1, coords_2).km>0:
            r_comp['rid'].append(x)





    scores  ={}

    for x in r_comp.keys():
        for y in r_comp[x]:


            for index, row in exist.iterrows():

                if(y==row[6]):     #competitors id sai cuisine
                     score = 0



                     if(re.sub('[\(\)\{\}\[\]<>]', '', cuisine) in re.sub('[\(\)\{\}\[\]<>]', '', row[1])):   #cuisine

                        score += 0.40



                     if(row[8]>=rating):
                         score += 0.30

                     if(row[7]==price):
                         score += 0.15


                     if(len(row[5])>8):
                         score += 0.05


                     if(row[9]==smoking):
                         score += 0.10

                     scores[y]=score


    print "The k competitors are-"
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)


    for i in sorted_scores:
        for index, row in exist.iterrows():

            if (i[0] == row[6]):  # competetior id sai cuisine
                print row[4]




#04cui+2rat+2pri+1pay+1smo




except Exception as e:
    print(e)
