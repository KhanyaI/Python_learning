import csv
import numpy as np
import pandas as pd
import random as rd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class KmeansML(object):

	def __init__(self, dataset,clusters=4,iterations=100):
		self.raw = dataset
		self.clusters = clusters
		self.iterations = iterations

	def setdataset(self, listofcols=[]):
		self.listofcols = listofcols
		df = pd.DataFrame(pd.read_csv(self.raw))
		self.data = df[self.listofcols].values
		self.samples= self.data.shape[0]
		self.features= self.data.shape[1]


	def initCentroids(self):
		Centroids = np.array([]).reshape(self.features,0)
		rd.seed(self.samples-1)
		for i in range(0,self.clusters):
			rand = rd.randint(0,self.samples-1)
			Centroids = np.c_[Centroids, self.data[rand]]
		return Centroids

	def EuclidDis(self,Centroids):
		for i in range(self.clusters):
			euclidian_distance =np.array([]).reshape(self.samples,0) 
		for k in range(self.clusters):
			dist_calc=(self.data- Centroids[:,k])**2
			dist = np.sum(dist_calc,axis=1)
			euclidian_distance = np.c_[euclidian_distance,dist]
		min_distance_centroid_number = np.argmin(euclidian_distance,axis=1)+1
		data_arranged_by_clusters ={}
	
		for k in range(self.clusters):
			data_arranged_by_clusters[k+1]=np.array([]).reshape(self.features,0)
		for i in range(self.samples):
			data_arranged_by_clusters[min_distance_centroid_number[i]]=np.c_[data_arranged_by_clusters[min_distance_centroid_number[i]],self.data[i]]
		for k in range(self.clusters):
			data_arranged_by_clusters[k+1]=data_arranged_by_clusters[k+1].T
		for k in range(self.clusters):
			Centroids[:,k]=np.mean(data_arranged_by_clusters[k+1],axis=0)
		return data_arranged_by_clusters


	def plotting(self,Centroids,data_arranged_by_clusters,onecolindex,othercolindex,onecolname,othercolname):
		self.onecolindex = onecolindex
		self.othercolindex = othercolindex
		self.onecolname = onecolname
		self.othercolname = othercolname
		color=['red','blue','green','cyan','magenta']
		labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
		for k in range(self.clusters):
			plt.scatter(data_arranged_by_clusters[k+1][:,self.onecolindex],data_arranged_by_clusters[k+1][:,self.othercolindex],c=color[k],label=labels[k])
		plt.scatter(Centroids[self.onecolindex,:],Centroids[self.othercolindex,:],s=100,c='yellow',label='Centroids')
		plt.xlabel(self.onecolname)
		plt.ylabel(self.othercolname)
		plt.legend()
		plt.show()


if __name__ == '__main__':
	kmeansobj = KmeansML('/Users/ifrahkhanyaree/Desktop/HomeDS/Kaggle/Mall_Customers.csv')
	kmeansobj.setdataset(["Age","Annual Income (k$)","Spending Score (1-100)"])
	centroids = kmeansobj.initCentroids()
	#pd.DataFrame(centroids).to_csv("/Users/ifrahkhanyaree/Desktop/centroids.csv",header = None)
	dist = kmeansobj.EuclidDis(centroids)
	#w = csv.writer(open("eucliddist.csv", "w"))
	#for key, val in dist.items():
	#	w.writerow([key, val])
	plot = kmeansobj.plotting(centroids,dist,0,1,"Age","Spending Score (1-100)")



