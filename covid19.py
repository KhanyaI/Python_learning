import csv
import random
import numpy as np 
import pandas as pd
import string
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize,sent_tokenize
nltk.download('punkt')
from nltk.corpus import stopwords
stopword = stopwords.words('english') 
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE


def wordprocess(file):

		stemmer = WordNetLemmatizer()
		for text in file:
			#print(text)
			text_nopunct = "".join([char.lower() for char in text if char not in string.punctuation]) 
			text_token = nltk.word_tokenize(text_nopunct)
			text_nostop = [word for word in text_token if word not in stopword]
			finalwords = [stemmer.lemmatize(word) for word in text_nostop]
			return finalwords


def vectorize(words):
	
	x_train ,x_test = train_test_split(preprocess,test_size=0.2)  
	vectorizer = TfidfVectorizer()
	tfidf_transform = vectorizer.fit_transform(x_train)
	feature_names = vectorizer.get_feature_names()
	
	
	"""
	Elbow curve
	K = range(1,50)
	distance = []
	for k in K:
		kmtest = KMeans(n_clusters=k)
		kmtest = kmtest.fit(tfidf_transform)
		distance.append(kmtest.inertia_)

	"""
	
	model = KMeans(n_clusters=30, init='k-means++', max_iter=100,n_init=1)
	model.fit(tfidf_transform)
	centroids = model.cluster_centers_

	testing = vectorizer.transform(x_test)
	labels = model.fit_predict(tfidf_transform)
	prediction = model.predict(testing)
	#print("Tested word is",x_test[0]) # just an example
	#print("Text belongs to cluster number {0}".format(prediction))
	

	"""
	for i in range(1):
		print('Cluster %d:' % i)
		for ind in range(len(centroids)):
			print('names',feature_names[ind])
	"""



if __name__ == '__main__':
	metadata_df = pd.DataFrame(pd.read_csv('/Users/ifrahkhanyaree/Desktop/HomeDS/CORD-19-research-challenge/metadata.csv',engine='python'))
	metadata_df = metadata_df.iloc[:, [0,1,2,7,8,9,10]]
	metadata_df.sha.dropna(inplace=True)
	metadata_df.abstract.dropna(inplace=True)
	preprocess = wordprocess(metadata_df.abstract)
	vectorize(preprocess)






