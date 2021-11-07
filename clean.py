import numpy as np
import pandas as pd

def parseLink(imageList):
    imageList=str(imageList)
    first=-1
    sec =-1
    cur=""
    for i in range(len(imageList)):
        if(imageList[i]=="'"):
            if(first==-1):
                first=i
            else:
                sec=i
                if(sec-first-1<=1):
                    first=-1
                    sec=-1
                else :
                    return imageList[first+1:sec]
    return cur

df=pd.read_csv('assets/repurpose_data_id.csv')
for i in range(len(df)):
        item=df.iloc[i]
        # print(item,type(item))
        if(i%1000==0):
            print("Processing " + str(i)+ "th row...")
        if(type(item['imageURLHighRes'])==str):
            # print(item['imageURLHighRes'])
            link=parseLink(item['imageURLHighRes'])
            # print(link)
            df.at[i,'imageURLHighRes']=link

            # df.iloc[i]['imageURLHighRes']=link
            # print(df.iloc[i]['imageURLHighRes'])
print(df['imageURLHighRes'].head(36))

df.to_csv('assets/finalData.csv')