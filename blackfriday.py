import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Read CSV file
df = pd.read_csv('/Users/ifrahkhanyaree/Python_env/kaggle/BlackFriday.csv')
#Replace NaNs with zero
df.fillna(value=0,inplace=True)
#Sum together all the products bought from the 3 different categories
sum = df['Product_Category_1']+df['Product_Category_2'] + df['Product_Category_3']
df['sum'] = sum #Adding sum as a column in the og dataframe
fig = plt.figure(figsize=(8,4))
sns.countplot(df['sum'],hue=df['Age']) #plot sum vs age
plt.xticks(rotation=45)
plt.show()
#df.fillna(value=0,inplace=True)

sns.countplot(df['Purchase'],hue=df['Gender'])#plot sum vs gender
plt.xticks(np.arange(min(df['Purchase']), max(df['Purchase']), 500.0), rotation=45)
plt.show()