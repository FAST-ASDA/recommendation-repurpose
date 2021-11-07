#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import math

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

df=0
vectorizer=0
model=0
def preprocess():
    global df
    df=pd.read_csv('assets/repurpose_data_id.csv')
    global vectorizer
    vectorizer=TfidfVectorizer(stop_words='english')
    inp=vectorizer.fit_transform(df['title'].values.astype('U'))
    fp= open('assets/recommender_model_kmeans.pkl', 'rb')
    global model 
    model= pickle.load(fp)
    return
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
            

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    msg="This is a flask app"
    return msg


@app.route('/getrecommendation',methods=['GET'])
def getrecommendationt():
    title = request.args.get('title', default = '*', type = str)
    print(title)
    # title='sexy'
    global vectorizer
    global model
    y=vectorizer.transform([title])
    clusterId=model.predict(y)
    df_cluster=df[model.labels_ == clusterId]
    sample=df_cluster.head(10)
    result=[]
    for i in range(len(sample)):
        item=sample.iloc[i]
        # print(item,type(item))
        if(item['notThrift']==0):
            continue
        if(len(result)>=5):
            break
        obj={
            'title':str(item['title']),
            'brand':str(item['brand']),
            'productId':int(item['productId']),
        }
        if(type(item['price'])==str or math.isnan(float(item['price']))==False):
            obj['price']=str(item['price'])
        # print(type(item['imageURLHighRes']))
        if(type(item['imageURLHighRes'])==str):
            print(item['imageURLHighRes'])
            link=parseLink(item['imageURLHighRes'])
            obj['imageURL']=link
        result.append(obj)
    sample=df_cluster.sample(20)
    for i in range(len(sample)):
        item=sample.iloc[i]
        # print(item,type(item))
        if(item['notThrift']==0):
            continue
        if(len(result)>=10):
            break
        obj={
            'title':str(item['title']),
            'brand':str(item['brand']),
            'productId':int(item['productId']),
        }
        if(type(item['price'])==str or math.isnan(float(item['price']))==False):
            obj['price']=str(item['price'])
        print(type(item['imageURLHighRes']))
        if(type(item['imageURLHighRes'])==str):
            print(item['imageURLHighRes'])
            link=parseLink(item['imageURLHighRes'])
            obj['imageURL']=link
        result.append(obj)
    print(result)
        
    result={
        'data':result
    }
    return result


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    preprocess()
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
