import csv 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(pd.read_csv('/Users/ifrahkhanyaree/Desktop/HomeDS/Code/Kaggle/titanic/train.csv'))
df['Family'] = df['SibSp'] + df['Parch']
##0. Clean data, remove missing values or make them zero? 
df.dropna(subset=['Age','Cabin','Embarked'],inplace=True)
#print(df.isnull().sum())
"""
##1. What places did people come from?
embarked = df.Embarked.value_counts()
embarked = embarked.tolist()
#print('Places people embarked:', type(embarked))
percentages = []
for city in embarked:
	value = (city/183)*100
	percentages.append(value)

##plotting
fig, ax = plt.subplots()
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#909090'
plt.rcParams['axes.labelcolor']= '#909090'
plt.rcParams['xtick.color'] = '#909090'
plt.rcParams['ytick.color'] = '#909090'
plt.rcParams['font.size']=12
color_palette_list = ['#009ACD', '#ADD8E6', '#63D1F4', '#0EBFE9',   
                      '#C1F0F6', '#0099CC']
labels = ['Cherbourg', 'Queenstown',
         'Southampton']
explode = [0,0,0.1]
patches, texts, autotexts = ax.pie(percentages, labels=labels,explode = explode,
       colors=color_palette_list[0:2], autopct='%1.0f%%', 
       shadow=False, startangle=45,labeldistance=1.2)

for text in texts:
    text.set_color('black')
for autotext in autotexts:
    autotext.set_color('black')
plt.setp(autotexts, size=12)

for patch in patches:
	patch.set_edgecolor('white')

ax.axis('equal')
ax.set_title("What cities did people embark from?")
ax.legend(frameon=False, bbox_to_anchor=(1.5,0.8))
#plt.show()

#2.What was the age and sex distribution? Check outliers
df.Sex.value_counts()
df.Age.value_counts()

#3. What was the socio economic distribution? Check outliers
socioeco = df.Pclass.value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(socioeco, labels =['Upper class','Middel class','Lower class'],autopct='%1.2f%%')
ax.set_title('Socioeconomic distribution in the Titanic')
plt.show()


#4. Do 2 and 3 for the different cities
cities = df.groupby(['Embarked','Pclass']).size().reset_index(name='count')
print(cities)
#sns.swarmplot(x=cities["Pclass"] ,y=cities["count"],hue=cities["Embarked"])
sns.barplot(x="Pclass", y="count", hue="Embarked", data=cities)
plt.show()

#Fare distribution for the different cities (correlate with socio eco status)
#print(df['Fare'].describe())
fares = df.groupby(['Embarked','Fare']).size().reset_index(name='Count')
sns.catplot(x="Count", y="Fare", hue="Embarked", kind="swarm", data=fares,height=8,aspect=1.5)
plt.show()

#% of people travelling with siblings, with spouses, with family and alone
no = df.SibSp.value_counts()
#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax.axis('equal')
#ax.pie(no, labels =['0','1','2','3'],autopct='%1.2f%%')
#ax.set_title('Distribution of having siblings or spouses on the titanic')
#plt.show()

sns.barplot(x="Family", y="Sex", hue="Survived", data=df,palette = 'coolwarm')
plt.title('Family - Sex Survival Distribution',size=16)
plt.show()

#Out of those - how did they vary with respect to socio eco status? 
sns.barplot(x="Family", y="Age", hue="Pclass", data=df,palette = 'coolwarm')
plt.title('Family - Class And Age Distribution',size=16)
plt.show()

#8.Age and sex dist by status

sns.barplot(x="Sex", y="Age", hue="Pclass", data=df,palette = 'coolwarm')
plt.title('Age-Sex Distribution by Class',size=16)
plt.show()


#Survival by age and sex
sns.barplot(x="Sex", y="Age", hue="Survived", data=df,palette = 'coolwarm')
plt.title('Age-Sex Survival Distribution',size=16)
plt.show()

#11. Survival with or without family

sns.barplot(x="Family", y="Sex", hue="Survived", data=df,palette = 'coolwarm')
plt.title('Family - Gender Survival Distribution',size=16)
plt.show()
"""





















