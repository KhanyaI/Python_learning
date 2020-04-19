import csv
import pandas as pd 
import matplotlib.pyplot as plt
import sklearn as sk  
import seaborn as sns
import numpy as np

### Basic data analysis
"""
data_csv = pd.read_csv('oasis_longitudinal.csv')
df = pd.DataFrame(data_csv)

#rows_even = df.iloc[::2,:] - was trying to pick out the second visit, did not work because some had 3/4 
#print(rows_even)

#select = df.loc[df['Visit'] == 1] shows all columns for the 1st visit 
#print(select)

a = df.replace(['Demented', 'Nondemented','Converted'],[0,1,1])
a2 = df.replace(['M', 'F'],[0,1])
#print(a)
#print(a.eTIV.max(),a.eTIV.min())

#print(list(a.columns.values))


#null_values = a.isnull().any()
#print(null_values) 

#a.set_index('Visit', inplace=True) # set row label to Visit
#a_try = a.loc[1,['Age','Group']] #only picking age and group from the first visit 



#count_1 = a.groupby(['Age','Group'])['M/F'].count() # grouped by age, what 
#print(count_1)

#print(pd.get_dummies(df.Visit))




#sns.scatterplot(x='eTIV',y='Age',hue='M/F',data=a) 
#sns.countplot(x ='EDUC',hue='M/F',data = a) 
#sns.boxplot(x='CDR', y='Age',data=a) # boxplot of clinical dementia rating with age


#plt.show()


### Correlation matrix
#corrmat = a.corr()
#f, ax = plt.subplots(figsize =(9, 8)) 
#get_fig_corr = sns.heatmap(corrmat, ax = ax, cmap ="YlGnBu", linewidths = 0.1) 

#fig_corr = get_fig_corr.get_figure()
#fig_corr.savefig('corr_mat.png')
#plt.show()

#corr_try = a['nWBV'].corr(a2['M/F'])
#print(corr_try)

## Trying Linear Regression

from sklearn import linear_model
#plt.scatter(a.MMSE, a.nWBV,color='red',marker='+')
#plt.show()
a.dropna(subset=['MMSE'], inplace = True)
#reg = linear_model.LinearRegression()
#print(reg.fit(a[['MMSE']], a.nWBV))
#print(reg.predict([[0.71]]))




### Classification


from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier 

#### SVC

#X_train, X_test,y_train, y_test = train_test_split(a[['MMSE']],a.Group, test_size=0.2)
#model = SVC(gamma = 1)
#X_train =np.array(X_train).reshape((-1,1)) #does not work as well
#X_test = np.array(X_test).reshape((-1,1)) #does not work as well
#model.fit(X_train,y_train)
#print ('Accuracy of SVC is', model.score(X_test,y_test))


#y_predicted = model.predict(X_test)
#from sklearn.metrics import confusion_matrix

#cm = confusion_matrix(y_test, y_predicted)
#plt.figure(figsize = (10,7))
#sns.heatmap(cm, annot=True)
#plt.xlabel('Predicted')
#plt.ylabel('Truth')
#plt.show()

####SVM

#X_train, X_test,y_train, y_test = train_test_split(a[['MMSE']],a.Group, test_size=0.2)
#model_SVC = LinearSVC(max_iter = 50)
#model_SVC.fit(X_train,y_train)
#print ('Accuracy of SVM is', model.score(X_test,y_test))
#y_predicted = model_SVC.predict(X_test)
#print(y_predicted)



######### KNN

#plt.scatter(a['Group'],a['MMSE'])
#plt.show()

#X_train, X_test,y_train, y_test = train_test_split(np.array(a.MMSE),a.Group, test_size=0.2)
#model_KNN = KNeighborsClassifier(n_neighbors=4)
#model_KNN.fit(X_train, y_train) 
#print(model_KNN.predict([[27]]))
#print(model_KNN.predict_proba([[27]]))
#print('Accuracy of KNN is', model_KNN.score(X_test,y_test))




######### NEURAL NETS

#sns.scatterplot(a.Group,a.MMSE)
#plt.show()

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#scaler.fit(X_train)
#X_train = scaler.transform(X_train)
#X_test = scaler.transform(X_test)
#model_NN = MLPClassifier(hidden_layer_sizes = (1,1,1), max_iter=500)
#model_NN.fit(X_train,y_train)
#predictions = model_NN.predict(X_test)
#print('Accuracy is', model_NN.score(X_test,y_test))
from sklearn.metrics import classification_report, confusion_matrix  
#cm = confusion_matrix( y_test,predictions)
#plt.figure(figsize = (10,7))
#sns.heatmap(cm, annot=True)
#plt.xlabel('Predicted')
#plt.ylabel('Truth')
#print(classification_report(y_test,predictions))  


######### Deep Neural Nets

import tensorflow as tf 
X_train, X_test,y_train, y_test = train_test_split(np.array(a.MMSE),np.array(a.Group), test_size=0.2)
X_train = tf.keras.utils.normalize(X_train)
X_train= np.array([item for x in X_train for item in x ])

X_test = tf.keras.utils.normalize(X_test)
X_test= np.array([item for x in X_test for item in x ])

model = tf.keras.models.Sequential()
#model.add(tf.keras.layers.Flatten()

model.add(tf.keras.layers.Dense(300, activation = tf.nn.relu,input_shape=(1,)))
model.add(tf.keras.layers.Dense(300, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation = tf.nn.softmax))

model.compile(optimizer = 'adam' , loss = 'sparse_categorical_crossentropy',metrics = ['accuracy'])
accuracy = model.fit(X_train,y_train,epochs=3)
print ('Accuracy is', accuracy)
val_loss, val_acc = model.evaluate(X_test, y_test)  # evaluate the out of sample data with model
print('Loss is', val_loss)  # model's loss (error)


######### Modularize code into a class
"""
class Person():
	def __init__(self,MMSE,nWBV):
		self.MMSE = MMSE
		self.nWBV = nWBV


class Series():
	def __init__(self, list_of_people):
		self.people = list_of_people

	"""def filter_by_attribute(self, attribute,attribute_value):
		persons_by_group = [person for person in self.people if getattr(person, attribute) == attribute_value]

		return persons_by_group"""

	def clustering(self, clustering_method, **kwargs):
		"""
		this function takes a name of a clustering algorithm and the parameters for that respective algorithm
		store in **kwargs, execute the clustering algorithm with given parameters on self.people

		clustering_method : str
							Denotes the name of the clustering algorithm
		kwargs : dict
				 Denotes the parameters for the given algorithm as keywords
		"""
		
		"""
		np.array(self.people)
		X_train, X_test,y_train, y_test = train_test_split(self.people)
		model = clustering_method.fit(X_train)
		Accuracy = model.score(X_test,y_test)
		print(Accuracy)

"""








if __name__ == '__main__':

	#anything underneath this gets executed first
	data_csv = pd.read_csv('oasis_longitudinal.csv')
	data_csv.dropna(subset=['MMSE'], inplace = True)
	list_of_persons = []
	X= []
	y=[]
	for row in range(0, data_csv.shape[0]):
		new_person = Person(data_csv.iloc[row]['MMSE'],data_csv.iloc[row]['nWBV'])
		list_of_persons.append(new_person)
	
	from sklearn.model_selection import train_test_split
	from sklearn.cluster import KMeans
	X_train, X_test,y_train, y_test = train_test_split(Person)
	print(X_train)

	#series = Series(list_of_persons)
	"""
	demented_group = series.filter_by_attribute("group", "Demented")
	for person in demented_group:
		print(person.group)
	"""	
"""
	
	Series.clustering(KMeans,X_train = , X_test= ...)

"""





	






######### So a class has a df as an attribute and a whole bunch of functions that use the class variable to manipulate and process data


######### Run your program through pep 8 checker to get static code analyisis results












