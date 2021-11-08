import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pickle
import os

print("Importing Data...")
df = pd.read_csv('assets/finalData.csv')
print("Vectorize...")
vectorizer = TfidfVectorizer(stop_words='english')
inp = vectorizer.fit_transform(df['title'].values.astype(str))

k = 150
print("Training...")
model = 0
if(os.path.exists("assets/recommender_model_kmeans.pkl")):
    fp = open('assets/recommender_model_kmeans.pkl', 'rb')
    model = pickle.load(fp)
    print("Model path exists...")
else:
    model = KMeans(n_clusters=k, init='k-means++', n_init=10)
    model.fit(inp)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
largestClusterId = 0
for i in range(k):
    print("Cluster %d:" % i)
    print("Size of cluster :: ", len(df[model.labels_ == i]))
    if(len(df[model.labels_ == i]) > len(df[model.labels_ == largestClusterId])):
        largestClusterId = i
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind])
    print("*"*100)

df2 = df[model.labels_ == largestClusterId]
print("Vectorize 2 ...")
vectorizerCluster = TfidfVectorizer(stop_words='english')
inp = vectorizerCluster.fit_transform(df2['title'].values.astype(str))

k2 = 15
print("Training 2 ...")
model2 = KMeans(n_clusters=k2, init='k-means++', n_init=10)
model2.fit(inp)

print("Top terms per cluster2 :")
order_centroids = model2.cluster_centers_.argsort()[:, ::-1]
terms = vectorizerCluster.get_feature_names()
for i in range(k2):
    print("Cluster %d:" % i)
    print("Size of cluster2 :: ", len(df2[model2.labels_ == i]))
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind])
    print("*"*100)


title = "Men's Trouser"
y = vectorizer.transform([title])
pred = model.predict(y)
if(pred == largestClusterId):
    y = vectorizerCluster.transform([title])
    pred = model2.predict(y)
    print(df2[model2.labels_ == pred].head(10))
else:
    print(df[model.labels_ == pred].head())

print(pred)

title = "Jordans"
y = vectorizer.transform([title])
pred = model.predict(y)
if(pred == largestClusterId):
    y = vectorizerCluster.transform([title])
    pred = model2.predict(y)
    print(df2[model2.labels_ == pred].head(10))
else:
    print(df[pred].head())
    print(df[model.labels_ == pred].head())

print(pred)

if(os.path.exists("assets/recommender_model_kmeans.pkl") == False):
    pickle.dump(model, open("assets/recommender_model_kmeans.pkl", "wb"))
pickle.dump(model2, open("assets/resolveBigCluster.pkl", "wb"))
