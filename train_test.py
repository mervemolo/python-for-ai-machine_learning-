import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df=pd.read_csv("Audi_A1_listings.csv")
# print(df.head(3))
df=df[["Year","Type","Mileage(miles)","Engine","PS","Transmission","Fuel","Number_of_Owners","Price(£)"]]
df.columns=["Yıl","Kasa","Mil","Motor","PS","Vites","Yakit","Sahip","Fiyat"]
df["Motor"]=df["Motor"].str.replace("L","")
# df["Motor"]=df["Motor"].astype(float)
df["Motor"]=pd.to_numeric(df["Motor"])
df=pd.get_dummies(df,columns=["Kasa","Vites","Yakit"],drop_first=True)
# print(df["Motor"].dtype)
y=df[["Fiyat"]]
x=df.drop("Fiyat",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=28)
lm=LinearRegression()
model=lm.fit(x_train,y_train)
print(model.score(x_test,y_test))
print(model.predict([[2016,30000,1,90,5,0,1]]))
# lm=LinearRegression()
# model=lm.fit(x,y)
# print(model.score(x,y))


