import csv
import numpy as np
import pandas as pd
import random as rd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def setdataset(pathtofile,column1,column2):
	df = pd.DataFrame(pd.read_csv(pathtofile))
	data = df[[column1 , column2]].values
	m=data.shape[0] 
	n=data.shape[1]
	return data, m, n

def initCentroids(dataset,training,features,clusters):
	Centroids =np.array([]).reshape(features,0)
	rd.seed(training-1)
	for i in range(0,clusters):
		rand = rd.randint(0,training-1)
		Centroids = np.c_[Centroids, dataset[rand]]
	return Centroids

def EuclidDis(dataset,training,features,clusters,centroids):
	for i in range(clusters):
		euclidian_distance =np.array([]).reshape(training,0) 
	for k in range(clusters):
		dist_calc=(dataset-centroids[:,k])**2
		dist = np.sum(dist_calc,axis=1)
		euclidian_distance = np.c_[euclidian_distance,dist]
	min_distance_centroid_number = np.argmin(euclidian_distance,axis=1)+1
	data_arranged_by_clusters ={}
	
	for k in range(clusters):
		data_arranged_by_clusters[k+1]=np.array([]).reshape(2,0)
	for i in range(training):
		data_arranged_by_clusters[min_distance_centroid_number[i]]=np.c_[data_arranged_by_clusters[min_distance_centroid_number[i]],dataset[i]]
	for k in range(clusters):
		data_arranged_by_clusters[k+1]=data_arranged_by_clusters[k+1].T
	for k in range(clusters):
		centroids[:,k]=np.mean(data_arranged_by_clusters[k+1],axis=0)
	return data_arranged_by_clusters


def plotting(data_clusters,clusters,centroids):
	color=['red','blue','green','cyan','magenta']
	labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
	for k in range(clusters):
		plt.scatter(data_clusters[k+1][:,0],data_clusters[k+1][:,1],c=color[k],label=labels[k])
	plt.scatter(centroids[0,:],centroids[1,:],s=100,c='yellow',label='Centroids')
	plt.xlabel('Age')
	plt.ylabel('Spending score')
	plt.legend()
	plt.show()


if __name__ == "__main__":
	iterations = 100
	K = 4 
	dataset,data_rows,data_features = setdataset('/Users/ifrahkhanyaree/Desktop/HomeDS/Kaggle/Mall_Customers.csv', 'Annual Income (k$)', 'Spending Score (1-100)')
	make_centroids = initCentroids(dataset,data_rows,data_features,K)
	calc_euclid = EuclidDis(dataset,data_rows,data_features,K,make_centroids)
	theplot = plotting(calc_euclid,K,make_centroids)
