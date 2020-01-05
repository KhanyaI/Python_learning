import csv
import numpy as np 
import pandas as pd
import random as rd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



df = pd.DataFrame(pd.read_csv('/Users/ifrahkhanyaree/Desktop/HomeDS/Mall_Customers.csv'))
df.rename({'Annual Income (k$)':'Income','Spending Score (1-100)':'Score'},axis=1, inplace=True)
data = df[['Age' , 'Score']].values
#print(data[2,:])

"""
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
print(kmeans.cluster_centers_)

plt.scatter(df['Age'], df['Score'], s =50, c= 'b')
plt.scatter(25.775 , 50.775,s=200, c='g', marker='s')
plt.scatter(30.1754386, 82.3508771, s=200, c='y', marker='s')
plt.scatter(60.36666667, 51.16666667, s=200, c='c', marker='s')
plt.scatter(43.1, 12.2, s=200, c='k', marker='s')
plt.scatter(44.96969697, 39.1515151, s=200, c='r', marker='s')

plt.show()

"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### Without sklearn

## Pseudo code  

#while True:
	#create clusters by randomly assigning points to closest centroids by computing euclidean distance 
		#from each data point to each centroid
		#smallest distance will be placed in group of that centroid
	#create new centroids by averaging clusters 
	#if centroids dont change
		#break


m=data.shape[0] #number of training examples
n=data.shape[1] # number of features
iterations = 100
K = 4 # no of clusters

##Initialize centroids
Centroids =np.array([]).reshape(n,0) # initalize empty array of 2 rows
rd.seed(m-1) # set this so the initial clusters don't change when re-running the script
for i in range(0,K):
	rand = rd.randint(0,m-1)# pick random integers from 0 to 199
	Centroids = np.c_[Centroids, data[rand]]# stack columns to get 2D array. Picks data points with index random integers, will give 2 rows (of 5 numbers each)

print('Initial',Centroids) # first set of centroids

## Calculate Euclidian Distance - find minimum distance from data point to a centroid

for i in range(1):
	euclidian_distance =np.array([]).reshape(m,0) # initalize an empty array with 200 rows 
	for k in range(K):#loop through number of clusters
		dist_calc=(data-Centroids[:,k])**2# euclidian distance formula, subtract each data point from each of the five centroids, square them
		dist = np.sum(dist_calc,axis=1)
		euclidian_distance = np.c_[euclidian_distance,dist]
	min_distance_centroid_number = np.argmin(euclidian_distance,axis=1)+1
	data_arranged_by_clusters ={}
	for k in range(K):
		data_arranged_by_clusters[k+1]=np.array([]).reshape(2,0)
	for i in range(m):
		data_arranged_by_clusters[min_distance_centroid_number[i]]=np.c_[data_arranged_by_clusters[min_distance_centroid_number[i]],data[i]]
	for k in range(K):
		data_arranged_by_clusters[k+1]=data_arranged_by_clusters[k+1].T
	for k in range(1):
		Centroids[:,k]=np.mean(data_arranged_by_clusters[k+1],axis=0)

#print('Final',data_arranged_by_clusters)

color=['red','blue','green','cyan','magenta']
labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
for k in range(K):
    plt.scatter(data_arranged_by_clusters[k+1][:,0],data_arranged_by_clusters[k+1][:,1],c=color[k],label=labels[k])
plt.scatter(Centroids[0,:],Centroids[1,:],s=100,c='yellow',label='Centroids')
plt.xlabel('Age')
plt.ylabel('Spending score')
plt.legend()
plt.show()
   



