import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Tablo 1: Demografik Bilgiler
df_musteri = pd.DataFrame({
    'Musteri_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Yasi': ['25', '45', '35', '50', '23', '40', '60', '20', '30', '55'],  # str tipinde
    'Sehir': ['Istanbul', 'Ankara', 'Istanbul', 'Izmir', 'Ankara', 'Istanbul', 'Izmir', 'Ankara', 'Istanbul', 'Izmir']
})

# Tablo 2: Finansal Durum
df_finans = pd.DataFrame({
    'Musteri_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Gelir': [25000.0, np.nan, 45000.0, 18000.0, np.nan, 55000.0, 12000.0, 22000.0, 60000.0, 15000.0],
    'Kredi_Skoru': [550, 720, 680, 500, 580, 790, 480, 610, 810, 520],
    'Borclu_Mu': [1, 0, 0, 1, 1, 0, 1, 0, 0, 1]  # Target (1: Kredisini Ödemedi/Riskli, 0: Ödedi/Temiz)
})

df=pd.merge(df_musteri,df_finans,on="Musteri_ID",how='outer')
df["Yasi"]=df["Yasi"].astype(int)
gelir_ort=df.groupby("Sehir")["Gelir"].transform("mean")
df["Gelir"]=df["Gelir"].fillna(gelir_ort)
df["Yuksek_Risk_Sinyali"]=np.where((df['Gelir']<25000) &(df["Kredi_Skoru"]<600),1,0)
x=df[["Yasi","Gelir","Kredi_Skoru","Yuksek_Risk_Sinyali"]]
y=df["Borclu_Mu"]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=42)
lm=LinearRegression()
model=lm.fit(x_train,y_train)
print(model.score(x_test,y_test))
print(model.predict([[24,20000,700,0]]))
