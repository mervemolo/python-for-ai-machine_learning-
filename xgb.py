import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

df=pd.read_csv("data.csv",na_values="?")
df=df.fillna(df.mean())
df.columns=df.columns.str.strip()
print(df.head(3))
y=df["num"]
x=df.drop("num",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.3)
# tree=DecisionTreeClassifier()
# rf=RandomForestClassifier(n_estimators=200)
rf=xgb.XGBClassifier()
model=rf.fit(x_train,y_train)
print(model.score(x_test,y_test))
deneme=df.sample().drop("num",axis=1)
print(model.predict(deneme))