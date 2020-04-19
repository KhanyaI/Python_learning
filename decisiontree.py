from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn import tree
import pandas as pd
import numpy as np
import graphviz
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus


df = pd.DataFrame(pd.read_csv('/Users/ifrahkhanyaree/Desktop/HomeDS/Kaggle/bank.csv'))
features_x= df[['job','marital','loan','balance','duration']]
X = pd.get_dummies(features_x)
featurenames = ['balance', 'duration', 'job_admin.', 'job_blue-collar',
       'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
       'job_self-employed', 'job_services', 'job_student', 'job_technician',
       'job_unemployed', 'job_unknown', 'marital_divorced', 'marital_married',
       'marital_single', 'loan_no', 'loan_yes']
y = df.deposit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) # 70% training and 30% test
clf = DecisionTreeClassifier(max_depth=5)
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


max_depth_range = list(range(1, 11))
accuracy = []
i = 0
for depth in max_depth_range:
	clf = DecisionTreeClassifier(max_depth = depth, 
                             random_state = 0)
	clf.fit(X_train, y_train)
	score = clf.score(X_test, y_test)
	accuracy.append(score)
	i = i+1
print(accuracy,i)

"""
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,filled=True, rounded=True,special_characters=True,feature_names=featurenames)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png()) 
"""
