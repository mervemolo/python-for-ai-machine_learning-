# import pandas as pd
# from sklearn.linear_model import LinearRegression

# df=pd.read_csv("Audi_A1_listings.csv")
# # print(df.head(3))
# df=df.drop(columns=["index","href","MileageRank","PriceRank","PPYRank","Score"])
# print(df.info())
# df.columns=["yil","kasa","mil","motor","ps","vites","yakit","sahip","fiyat","ppy"]
# # print(df.head(3))
# df["motor"]=df["motor"].str.replace("L","")
# df["motor"]=df["motor"].astype(float)

# df=pd.get_dummies(df,columns=["kasa","vites","yakit",],drop_first=True)
# # print(df.head(3))
# lm=LinearRegression()
# y=df["fiyat"]
# x=df.drop("fiyat",axis=1)
# model=lm.fit(x,y)
# print(model.predict([[2017,30000,1.6,110,1,2600,0,1]]))
# print(model.score(x,y))


# from sklearn.linear_model import LinearRegression
# import pandas as pd
# df=pd.read_csv("student_performance.csv")
# print(df.head(3))
# df.columns=["saat","not"]
# print(df.head(3))
# y=df["not"]
# x=df[["saat"]]
# lm=LinearRegression()
# model=lm.fit(x,y)
# print(model.predict([[1.2]]))
# print(model.coef_)
# print(model.intercept_)
# print(model.score(x,y))
