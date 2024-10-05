import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("titanic.csv")
print(df)
#gender distrubition
ex1=(df["Sex"]=="male").sum()/(df["Name"].count()) 
print("male percentage:"+str(round(ex1*100,2))+"  female percantage:"+str(round(100-ex1*100,2)))

#dead man percantage
ex2=((df["Sex"]=="male") & (df["Survived"]==0)).sum()/(df["Sex"]=="male").sum()
print("male dead percentage:"+str(round(ex2*100,2))+"  male survived percantage:"+str(round(100-ex2*100,2)))

#dead female percantage
ex3=((df["Sex"]=="female") & (df["Survived"]==0)).sum()/(df["Sex"]=="female").sum()
print("female dead percentage:"+str(round(ex3*100,2))+"  female survived percantage:"+str(round(100-ex3*100,2)))

#percantege of survived person by seat class and gender
group=df.groupby(["Pclass","Sex"])
survived=group["Survived"].sum()
passengers=group["Survived"].count()
percentage=(survived/passengers)*100


print(round(percentage,2))
percentage.unstack().plot(kind='bar',stacked=False,figsize=(10,6))
plt.title('Pclass ve cinsiyete gore haytta kalma orani')
plt.ylabel('Hayatta kalma yuzdesi')
plt.xlabel("Pclass")
plt.xticks(rotation=0)
plt.legend(title='Cinsiyet')
plt.show()

#survived person number by age
group=df.groupby("Age")
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]  # Yaş aralıkları
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
group = df.groupby('AgeGroup')
alivedAges=group["Survived"].sum()
countAllages=group["Name"].count()
percentage=alivedAges/countAllages*100
print(round(percentage,2))
percentage.plot(kind='bar',stacked=False,figsize=(10,6))
plt.title('Yasa gore haytta kalma orani')
plt.ylabel('Hayatta kalma yuzdesi')
plt.xlabel("Yas")
plt.xticks(rotation=0)
plt.legend(title='Yas')
plt.show()

#how much money paid by an average by survived persons
ex4=df.groupby("Survived")["Fare"].mean()
print(ex4)

#woman and man passenger number
ex5=df.groupby("Sex")["Name"].count()
print(ex5)

#average of  below 18 years old surviving percantage
ex6=((df["Age"]<18) & (df["Survived"]==1)).sum()/(df["Age"]<18).sum()
print(round(ex6,2)*100)

#percentage of survived persons by port
ex7=df.groupby("Embarked")["Survived"].mean()
print(ex7)

#oldest and youngest passangers
oldestPsgnr=df.loc[df["Age"].max()]
oldestPsgnrs=df[df["Age"]>70]
youngestPsgnr=df.loc[df["Age"].idxmin()]
print(oldestPsgnr)

#family size of survived number
df["FamilySize"]=df["SibSp"]+df["Parch"]+1
familysizesurvive=df.groupby("FamilySize")["Survived"].mean()*100
print(familysizesurvive)

#average money paid by  age range
group=df.groupby("Age")
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]  
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
ageGroupTicketPrice=df.groupby('AgeGroup')["Fare"].mean()
ageGroupTicketPrice.plot(kind="bar",figsize=(10,6))
plt.scatter(df['Age'],df['Fare'])
plt.title('Yasa gore ortalama bilet fyati ')
plt.ylabel('Ortalama ucret')
plt.xlabel("Yas")
plt.xticks(rotation=0)
plt.legend(title='Yas')
plt.show()


