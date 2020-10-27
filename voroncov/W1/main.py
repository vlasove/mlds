import pandas as pd 

df = pd.read_csv('titanic.csv', index_col = 'PassengerId')
print("Male:", df['Sex'].value_counts()['male'])
print("Female:", df['Sex'].value_counts()['female'])

print("Percent survived:", sum(df["Survived"])/ len(df["Survived"]) * 100)
print("Percent of first class:", df["Pclass"].value_counts()[1]/ len(df["Pclass"]) * 100)

print("Age avg:", df["Age"].mean())
print("Age median:", df["Age"].median())


print(df[['SibSp', 'Parch']].corr())


"""
Поиск самого популярного женского имени
"""
names = list(df[df['Sex'] == 'female']['Name'])
unique_names = {}
for name in names:
    if '(' in name:
        prep = name.split('(')[-1].split() 
        name = prep[:-1] + [prep[-1][:-1]]
    else:
        name = name.split('.')[1].split()
    for n in name:
        if n in unique_names:
            unique_names[n] += 1
        else:
            unique_names[n] = 1
unique_tuple = sorted([(v, k) for k, v in unique_names.items()], reverse=True)
print(unique_tuple[:5])

