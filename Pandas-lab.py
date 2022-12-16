import pandas as pd 
import numpy as np
titanic_data = pd.read_csv("titanic.csv")
titanic_pclass1 = (titanic_data.Pclass == 1)
titanic_pclass_data = titanic_data[titanic_pclass1]
titanic_Survived = (titanic_data.Survived == 1)
titanic_Survived_data = titanic_data[titanic_Survived]
ages = [20 , 21 , 22]
age_dataset = titanic_data[titanic_data['Age'].isin(ages)]
ageclass_dataset = titanic_data[titanic_data['Age'].isin(ages) & (titanic_data['Pclass'] == 1)]
titanic_data_filter = titanic_data.filter(['Name','Sex','Age'])
titanic_data_updated = titanic_data.drop(['Name','Sex','Age'],axis=1)
titanic_pclass1_data = titanic_data[titanic_data.Pclass==1]
titanic_pclass2_data = titanic_data[titanic_data.Pclass==2]
final_data = titanic_pclass1_data.append(titanic_pclass2_data,ignore_index=True)
df1 = final_data[:200]
df2 = final_data[200:]
final_data2=pd.concat([df1,df2],axis =1,ignore_index=True)
age_sorted_data = titanic_data.sort_values(by =['Age','Fare'],ascending=False)
# updated_class = titanic_data.Pclass.apply(lambda x : x + 2)
def mult(x):
    return x*2
updated_class = titanic_data.Pclass.apply(mult)
titanic_data.Fare = np.where(titanic_data.Age > 20 , titanic_data.Fare+5 ,titanic_data.Far )
# print(titanic_data.head())
# print(titanic_pclass1)
# print(titanic_pclass_data.head())
# print(titanic_Survived_data.head())
# print(age_dataset.head())
# print(ageclass_dataset.head())
# print(titanic_data_filter)
# print(titanic_data_updated.head())
# print(titanic_pclass1_data.shape)
# print(titanic_pclass2_data.shape)
# print(final_data.shape)
# print(df1.shape)
# print(df2.shape)
# print(final_data2.shape)
# print(age_sorted_data.head())
# print(updated_class.head())
