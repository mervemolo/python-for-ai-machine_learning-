import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import graphviz
df=pd.read_csv("data.csv",na_values="?")
df.columns=df.columns.str.strip()
df=df.fillna(df.mean())
print(df.head(3))
y=df["num"]
x=df.drop("num",axis=1)
tree=DecisionTreeClassifier()
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.3)
model=tree.fit(x_train,y_train)
print(model.score(x_test,y_test))
print(
model.predict([[24,0,2,130,200,0,0,140,0,3,0,0,2]]))

dot=export_graphviz(model,feature_names=x.columns,filled=True)
gorsel=graphviz.Source(dot)
print(gorsel)