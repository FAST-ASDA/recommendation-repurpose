#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import math

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

df = 0
vectorizer = 0
model = 0
dfBigCluster = 0
vectorizerCluster = 0
modelCluster = 0
largestClusterId = 0


def preprocess():
    global df
    global model
    global vectorizer
    global dfBigCluster
    global modelCluster
    global vectorizerCluster
    global largestClusterId
    df = pd.read_csv('assets/finalData.csv')
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit_transform(df['title'].values.astype('U'))
    fp = open('assets/recommender_model_kmeans.pkl', 'rb')
    model = pickle.load(fp)
    k = 150
    for i in range(k):
        if(len(df[model.labels_ == i]) > len(df[model.labels_ == largestClusterId])):
            largestClusterId = i

    dfBigCluster = df[model.labels_ == largestClusterId]
    vectorizerCluster = TfidfVectorizer(stop_words='english')
    vectorizerCluster.fit_transform(dfBigCluster['title'].values.astype('U'))
    fp2 = open('assets/resolveBigCluster.pkl', 'rb')
    modelCluster = pickle.load(fp2)
    return


def parseLink(imageList):
    imageList = str(imageList)
    first = -1
    sec = -1
    cur = ""
    for i in range(len(imageList)):
        if(imageList[i] == "'"):
            if(first == -1):
                first = i
            else:
                sec = i
                if(sec-first-1 <= 1):
                    first = -1
                    sec = -1
                else:
                    return imageList[first+1:sec]
    return cur


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    msg = "This is a flask app"
    return msg


@app.route('/getrecommendation', methods=['GET'])
def getrecommendationt():
    title = request.args.get('title', default='*', type=str)
    print(title)
    y = vectorizer.transform([title])
    clusterId = model.predict(y)
    df_cluster = df
    print("Cluster id:: ", clusterId)
    if(clusterId == largestClusterId):
        y = vectorizerCluster.transform([title])
        clusterId = modelCluster.predict(y)
        df_cluster = dfBigCluster[modelCluster.labels_ == clusterId]
        print("Small Cluster Id: ", clusterId)
    else:
        df_cluster = df[model.labels_ == clusterId]
    result = []
    sample = df_cluster.sample(25)
    for i in range(len(sample)):
        item = sample.iloc[i]
        # print(item,type(item))
        if(item['notThrift'] == 0):
            continue
        if(len(result) >= 15):
            break
        obj = {
            'title': str(item['title']),
            'brand': str(item['brand']),
            'productId': int(item['productId']),
        }
        if(type(item['price']) == str or math.isnan(float(item['price'])) == False):
            obj['price'] = str(item['price'])
        # print(type(item['imageURLHighRes']))
        if(type(item['imageURLHighRes']) == str):
            # print(item['imageURLHighRes'])
            # link=parseLink(item['imageURLHighRes'])
            link = item['imageURLHighRes']
            obj['imageURL'] = link
        result.append(obj)
    # print(result)

    result = {
        'data': result
    }
    return result


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
preprocess()

if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
