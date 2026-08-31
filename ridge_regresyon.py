# Ridge regresyon overfitting (Aşırı öğrenme durumları için kullanılır)
# Ridge regresyon sayesinde bias ve varyans arasındaki dengeyi sağlayabiliriz
# Ridge regresyonda katsayılar üzerinde regülasyon yapılıyor 
# Ridge regresyonda katsayılar küçülür ama sıfır olmaz Features öz nitelik azalmaz.
# Rigde regresyonda cezalar karesi ile orantılı
# Ridge regresyon l2
# y=a1*x1+a2*x2+............+b+alfa*(katsayılar toplamı)**2

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge
import matplotlib.pyplot as plt

df=pd.read_csv("student_performance.csv")
print(df.head(3))
y=df["exam_score"]
x=df[["study_hours"]]
# plt.style.use("fivethirtyeight")
# plt.figure(figsize=(8,8))
# plt.scatter(x,y)
# plt.show()
lm=LinearRegression()
model=lm.fit(x,y)
print(model.score(x,y))
alphalar=[1,10,20,100,200]
for a in alphalar:
    r=Ridge(alpha=a)
    modelr=r.fit(x,y)
    skor=modelr.score(x,y)
    print("skor",skor)
    print(f"Katsayı {modelr.coef_}")

