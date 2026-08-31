import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=sns.load_dataset("diamonds")

df=pd.get_dummies(df,columns=["cut","color","clarity"],drop_first=True,dtype=int)
print(df.head(3))
y=df["price"]
x=df.drop("price",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.24)
lm=LinearRegression()
model=lm.fit(x_train,y_train)
print(model.score(x_test,y_test))

print(model.score(x_train,y_train))