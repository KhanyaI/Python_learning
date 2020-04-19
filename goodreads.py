import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import kmeans, vq
from sklearn.cluster import KMeans
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from matplotlib.lines import Line2D
from sklearn.metrics import silhouette_score      


books_df = pd.DataFrame(pd.read_csv('/Users/ifrahkhanyaree/Desktop/HomeDS/books.csv',error_bad_lines = False))

indexNames = books_df[books_df['language_code'] != 'eng' ].index 
books_df.drop(indexNames , inplace=True) # removing rows with this value
books_df_refined = books_df[['title', 'authors', 'average_rating','# num_pages','ratings_count']]

### plot bar graph of most occuring authors

authors = books_df_refined['authors'].value_counts()[:20]

"""
## using seaborn 
sns.barplot(x = authors, y = authors.index, palette='deep')
plt.title("Most Occurring Authors")
plt.xlabel("Number of occurances")
plt.ylabel("Authors")

## using matplotlib

plt.bar(authors.index,authors)
plt.xticks(authors.index, fontsize=4, rotation=30)
plt.title('Most occuring authors')

### pick top books of most occuring authors
grouping = books_df_refined.groupby(['authors','title']).size()
pop_author_books = grouping.sort_values(ascending=False)[:20]
sns.barplot(x = pop_author_books, y = pop_author_books.index, palette='deep')
plt.title("Books by popular authors")
plt.xlabel("Number of occurances")
plt.ylabel("Titles")

### pick books with highest ratings
ratings = books_df_refined.groupby(['title','average_rating']).size()
highest_rated_books = ratings.sort_values(ascending=False)[:20]
figure = sns.barplot(x = highest_rated_books, y = highest_rated_books.index, palette='Set2')
plt.title("Top rated books")
plt.xlabel("Number of occurances")
plt.ylabel("Titles")
figure.set_yticklabels(figure.get_yticklabels(), rotation=10,horizontalalignment='right',fontsize=4.5)


# relationship between ratings and page number 
books_df_refined = books_df_refined[~(books_df_refined['# num_pages']>1000)]
rating_page_df = books_df_refined[['average_rating','# num_pages']]

ax = sns.scatterplot(x="average_rating", y="# num_pages", data=rating_page_df)
plt.show()

corr = rating_page_df.corr()
print(corr)
corr.style.background_gradient(cmap='coolwarm').set_precision(2)
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)



# distribution of ratings
books_df_refined.dropna(0,inplace=True)
ratings = books_df_refined.average_rating
print(ratings)

ratings_dist = []
lst_rates = [0,1,2,3,4,5]
i = 0
while i < len(lst_rates):
	test = (books_df['average_rating'] >= i) & (books_df['average_rating'] < i+1)
	test2 = test.sum()
	#print(test)
	ratings_dist.append(test2)
	i = i+1

ratings_dist = np.array(ratings_dist)
percent = (ratings_dist/10594)*100
percent = np.around(percent,decimals=1)




labels = '0-1', '1-2', '2-3', '3-4', '4-5','5'
explode = explode = (0.05,0.05,0.05,0.05,0.05,0.05)
fig1, ax1 = plt.subplots()
ax1.pie(percent,startangle=90, pctdistance=0.85, explode = explode)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, percent)]
plt.legend( labels, loc = 'best',bbox_to_anchor=(-0.1, 1.),)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
#plt.figure(figsize=(12,12))
#sns.distplot(ratings)


#books_df_refined.plot.pie(y='average_rating', figsize=(5, 5))
#plt.show()



# ratings of top 10 authors

books_df_refined = books_df_refined[books_df_refined['average_rating']>=4.3]
grouping = books_df_refined.groupby(['authors']).size()
pop_author_books = grouping.sort_values(ascending=False)[:20]
sns.barplot(x = pop_author_books, y = pop_author_books.index, palette='deep')
plt.title("Authors")
plt.xlabel("Number of occurances")
plt.ylabel("Titles")
plt.show()



# what book got the most reviews
books_df_refined = books_df_refined.sort_values(by = 'ratings_count', ascending=False)
test = books_df_refined.head(10)
figure = sns.barplot(x = test.ratings_count, y = test.title, palette='Set2')
plt.title("Top reviewed books")
plt.xlabel("Number of occurances")
plt.ylabel("Titles")
plt.show()
"""

## recommendation engine
trial = books_df_refined[['average_rating', 'ratings_count']]
data = np.asarray([np.asarray(trial['average_rating']), np.asarray(trial['ratings_count'])]).T



def calculate_WSS(points, kmax):
  sse = []
  for k in range(1, kmax+1):
    kmeans = KMeans(n_clusters = k).fit(points)
    centroids = kmeans.cluster_centers_
    pred_clusters = kmeans.predict(points)
    curr_sse = 0
    
    # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
    for i in range(len(points)):
      curr_center = centroids[pred_clusters[i]]
      curr_sse += (points[i, 0] - curr_center[0]) ** 2 + (points[i, 1] - curr_center[1]) ** 2
      
    sse.append(curr_sse)
  
  #print(sse)
  x = range(10)
  y = sse
  #plt.plot(x,y)
  #plt.show()
  return sse


calculate_WSS(data,10)

"""
sil = []
kmax = 10

# dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
for k in range(2, kmax+1):
  kmeans = KMeans(n_clusters = k).fit(x)
  labels = kmeans.labels_
  sil.append(silhouette_score(x, labels, metric = 'euclidean'))

 print(sil) #closest to 1 is best

 """
centroids,_ = kmeans(data, 3)
idx, _ = vq(data, centroids)
features = pd.concat([books_df_refined['average_rating'], books_df_refined['ratings_count'],books_df_refined['# num_pages']], axis=1)

min_max_scaler = MinMaxScaler()
features = min_max_scaler.fit_transform(features)
np.round(features, 2)

model = neighbors.NearestNeighbors()
model.fit(features)
distance, indices = model.kneighbors(features)



def get_index_from_name(name):
    return books_df_refined[books_df_refined["title"]==name].index.tolist()[0]


def print_similar_books(query=None):
	found_id = get_index_from_name(query)
	print(found_id)
	"""
	for id in indices[found_id][1:]:
		#print(id)
		print(books_df_refined.iloc[id]["title"])

print_similar_books("The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy  #1)")

"""