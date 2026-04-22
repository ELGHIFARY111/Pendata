import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 2. LOAD DATA
print("\nMemuat data...")
all_sheets = pd.read_excel('Simulasi_ECommerce_20Sheet.xlsx', sheet_name=None)
df_all = pd.concat(all_sheets.values(), ignore_index=True)

print(df_all.info())


# 4. PREPROCESSING
print("\nPreprocessing...")

df_bersih = df_all.drop(columns=['ID_Produk', 'Harga', 'Biaya_Iklan'])

fitur = ['Diskon_Persen', 'Rating', 'Jumlah_Ulasan']

scaler = StandardScaler()
df_bersih[fitur] = scaler.fit_transform(df_bersih[fitur])

# 5. SPLIT DATA
X = df_bersih[fitur]
y = df_bersih['Kelarisan']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. MACHINE LEARNING
print("\nTraining model...")

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 7. EVALUASI
print("\n=== HASIL ===")
print("Akurasi:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8. FEATURE IMPORTANCE
print("\nFeature Importance:")
importance = model.feature_importances_

for i, v in enumerate(importance):
    print(f"{fitur[i]} : {v:.4f}")