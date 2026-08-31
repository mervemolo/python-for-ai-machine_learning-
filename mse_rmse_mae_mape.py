import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error

df=pd.read_csv("insurance.csv")
# print(df.head(3))
df=pd.get_dummies(df,columns=["sex","smoker","region"],drop_first=True)
# print(df.head(3))
y=df["charges"]
x=df.drop("charges",axis=1)
lm=LinearRegression()
model=lm.fit(x,y)
print(model.score(x,y))
print(model.predict([[19,26,0,1,1,0,0,1]]))
df_hata=pd.DataFrame()
df_hata["y"]=y
# print(df_hata)
y_tahmin=model.predict(x)
df_hata["tahmin"]=y_tahmin
df_hata["error"]=y-y_tahmin
# print(df_hata.head(3))
df_hata["squared_error"]=df_hata["error"]**2

df_hata["abs_error"]=np.abs(df_hata["error"])

df_hata["percent_error"]=np.abs((y-y_tahmin)/y)
print(df_hata.head(3))
print(df_hata.mean())

print(mean_squared_error(y,y_tahmin))
print(mean_absolute_error(y,y_tahmin))
print(mean_absolute_percentage_error(y,y_tahmin))