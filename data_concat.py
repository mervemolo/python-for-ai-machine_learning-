# import pandas as pd
# import numpy as np

# # 1. Müşteri Tablosu
# df_musteriler = pd.DataFrame({
#     'Musteri_ID': [101, 102, 103, 104],
#     'Ad': ['Caner', 'Selin', 'Burak', 'Derya'],
#     'Sehir': ['Istanbul', 'Ankara', 'Izmir', 'Bursa']
# })

# # 2. Ocak Ayı İşlemleri
# df_ocak = pd.DataFrame({
#     'Islem_ID': [1, 2],
#     'Musteri_ID': [101, 102],
#     'Tutar': [1500.0, 2300.0]
# })

# # 3. Şubat Ayı İşlemleri
# df_subat = pd.DataFrame({
#     'Islem_ID': [3, 4],
#     'Musteri_ID': [101, 103],
#     'Tutar': [850.0, 4100.0]
# })
# df_toplam=pd.concat([df_ocak,df_subat],ignore_index=True)
# print(df_toplam)
# df_left=pd.merge(df_musteriler,df_toplam,on="Musteri_ID",how="left")
# print(df_left)
# df_right=pd.merge(df_musteriler,df_toplam,on="Musteri_ID",how="right")
# print(df_right)
# no_siparis=df_left.loc[df_left["Tutar"].isnull()]
# print(no_siparis)















import pandas as pd

# 1. Şirket Çalışanları Tablosu
df_calisanlar = pd.DataFrame({
    'Calisan_ID': [1, 2, 3, 4],
    'Ad': ['Ali', 'Veli', 'Ayşe', 'Fatma']
})

# 2. Aktif Projeler Tablosu
df_projeler = pd.DataFrame({
    'Proje_Kodu': ['PRJ-A', 'PRJ-B', 'PRJ-C'],
    'Calisan_ID': [2, 3, 5]  # 5 numaralı id çalışanlar tablosunda yok!
})


df_inner=pd.merge(df_calisanlar,df_projeler,on="Calisan_ID",how="inner")
# print(df_inner)
print(len(df_inner))
print(len(df_inner.columns))
df_right=pd.merge(df_calisanlar,df_projeler,on="Calisan_ID", how="right")
print(df_right)
df_outer=pd.merge(df_calisanlar,df_projeler,on="Calisan_ID",how="outer")
print(df_outer)