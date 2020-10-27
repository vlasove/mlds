import pandas as pd 

df = pd.read_csv('titanic.csv', index_col = 'PassengerId')
print("Male:", df['Sex'].value_counts()['male'])
print("Female:", df['Sex'].value_counts()['female'])

print("Percent survived:", sum(df["Survived"])/ len(df["Survived"]) * 100)
print("Percent of first class:", df["Pclass"].value_counts()[1]/ len(df["Pclass"]) * 100)

print("Age avg:", df["Age"].mean())
print("Age median:", df["Age"].median())