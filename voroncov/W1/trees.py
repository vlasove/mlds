import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('titanic.csv', index_col = 'PassengerId')
target = df['Survived']
df = df[['Pclass', 'Fare', 'Age', 'Sex']]

print(df.head())
