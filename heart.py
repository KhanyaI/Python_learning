import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier






df = pd.read_csv("/Users/ifrahkhanyaree/Python_env/classification/heart.csv")
X = df.values
A = X[:,4]
B = X[:,11]
C = np.vstack((A,B))
C2 = np.transpose(C)
print (C2)
Y = df.sex
neighbours = KNeighborsClassifier(5)
neighbours.fit(C2,Y)
end = neighbours.predict([[200,3]])
end2 = neighbours.score(C2,Y)
print (end,end2)

#sns.countplot(x ="ca",hue="sex",data = df)
#plt.show()
#print (df.isnull().values.any())
#print(df.info())
#trial = df.loc[: , "oldpeak"]
#check_ca = df.ca.unique()


