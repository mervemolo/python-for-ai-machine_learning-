import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Veri Seti (Müşteri Davranışları)
data = {
    'Yas': [25, 45, 35, 50, 23, 40, 60, 20, 30, 55],
    'Aylik_Harcama': [150, 800, 300, 1200, 100, 650, 900, 80, 400, 1100],
    'Arama_Sayisi': [5, 1, 3, 0, 8, 2, 0, 6, 2, 1],
    'Terk_Etti': [1, 0, 0, 0, 1, 0, 0, 1, 0, 0]  # Target (0: Kaldı, 1: Terk Etti)
}

df = pd.DataFrame(data)

# 2. X (Features) ve y (Target) Ayrımı
X = df[['Yas', 'Aylik_Harcama', 'Arama_Sayisi']]
y = df['Terk_Etti']

# 3. Train/Test Split (%80 Eğitim, %20 Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Eğitimi (Random Forest)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Tahmin Yapma ve Değerlendirme
y_pred = model.predict(X_test)
basari = accuracy_score(y_test, y_pred)

print(f"Model Doğruluk Oranı (Accuracy): {basari * 100:.0f}%")

# Yeni bir müşteri için Churn tahmini yapalım:
yeni_musteri = [[22, 110, 7]]  # Genç, az harcama yapıyor, 7 kez müşteri hizmetlerini aramış
tahmin = model.predict(yeni_musteri)
print("Yeni Müşteri Tahmini:", "Terk Edebilir (1)" if tahmin[0] == 1 else "Kalıcı (0)")