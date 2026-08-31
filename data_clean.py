import pandas as pd
import numpy as np

data_test = {
    'Musteri_ID': [101, 102, 103, 104, 105, 106, 107],
    'Sehir': ['Istanbul', 'Ankara', 'Istanbul', 'Izmir', 'Ankara', 'Istanbul', 'Izmir'],
    'Harcama': [4500.0, np.nan, 12000.0, 3200.0, np.nan, 8500.0, 1500.0],
    'Siparis_Sayisi': ['12', '3', '25', '8', '5', '18', '2'],  # Metin (str) tipinde
    'Segment': ['Bireysel', 'Kurumsal', 'Kurumsal', 'Bireysel', 'Bireysel', 'Kurumsal', 'Bireysel']
}

df = pd.DataFrame(data_test)
df["Siparis_Sayisi"]=df["Siparis_Sayisi"].astype(int)
sehir_ortalaması=df.groupby("Sehir")["Harcama"].transform("mean")

df["Harcama"]=df["Harcama"].fillna(sehir_ortalaması)
df["Müsteri_Statusu"]=np.where((df['Harcama']>5000) & (df["Siparis_Sayisi"]>=10),"VIP","Standart")
df.loc[(df["Sehir"]=="Istanbul") &(df["Müsteri_Statusu"]=="VIP"),["Musteri_ID","Harcama"]]
def segment_ozeti_getir(df:pd.DataFrame)->dict[str,float]:
    toplam_harcama=df.groupby("Segment")["Harcama"].sum().to_dict()
    return toplam_harcama
ozet=segment_ozeti_getir(df)
print(ozet)