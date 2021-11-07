import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pickle

print("Importing Data...")
df=pd.read_csv('assets/finalData.csv')
print("Vectorize...")
vectorizer=TfidfVectorizer(stop_words='english')
inp=vectorizer.fit_transform(df['title'].values.astype(str))

k=150
print("Training...")
model=KMeans(n_clusters=k,init='k-means++',n_init=10)
model.fit(inp)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(k):
    print("Cluster %d:" % i)
    print("Size of cluster :: ",len(df[model.labels_==i]))
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind])
    print("*"*100)

y=vectorizer.transform(['Sexy'])
pred=model.predict(y)
print(pred)

pickle.dump(model,open("assets/recommender_model_kmeans.pkl","wb"))