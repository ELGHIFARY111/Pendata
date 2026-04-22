import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# ==========================================
# TAHAP 1: LOAD DATA 20 SHEET
# ==========================================
print("Memuat data dari 20 Sheet Excel...")
all_sheets = pd.read_excel('Simulasi_ECommerce_20Sheet.xlsx', sheet_name=None)
df_all = pd.concat(all_sheets.values(), ignore_index=True)

# ==========================================
# TAHAP 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================
print("\nMelakukan EDA...")
# (Kode plot grafik sengaja di-comment agar skrip bisa jalan langsung ke ML, 
# Anda sudah berhasil menampilkan grafiknya dari kode sebelumnya)
# sns.countplot(x='Kelarisan', data=df_all) 
# sns.heatmap(df_all.corr(), annot=True)

# ==========================================
# TAHAP 3: PREPROCESSING BY EDA
# ==========================================
print("\nMelakukan Preprocessing berdasarkan temuan EDA...")

# Temuan EDA: Harga dan Biaya_Iklan memiliki korelasi ~0.00 dengan target.
# Aksi Preprocessing: Feature Selection (Drop fitur yang tidak relevan)
df_bersih = df_all.drop(columns=['ID_Produk', 'Harga', 'Biaya_Iklan'])
print("Fitur 'Harga' dan 'Biaya_Iklan' dibuang karena korelasi sangat rendah pada Heatmap.")

# Aksi Preprocessing: Standardisasi skala numerik pada fitur yang tersisa
fitur_relevan = ['Diskon_Persen', 'Rating', 'Jumlah_Ulasan']
scaler = StandardScaler()
df_bersih[fitur_relevan] = scaler.fit_transform(df_bersih[fitur_relevan])
print("Standardisasi selesai pada fitur:", fitur_relevan)

# ==========================================
# TAHAP 4: MACHINE LEARNING
# ==========================================
print("\nMelatih model Machine Learning...")
X = df_bersih[fitur_relevan]
y = df_bersih['Kelarisan']

# Split 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Random Forest
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)
y_pred = model_rf.predict(X_test)

# Evaluasi
print("\n=== HASIL AKHIR ===")
print(f"Akurasi: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nLaporan Klasifikasi:\n", classification_report(y_test, y_pred))

# Cek Feature Importance untuk membuktikan temuan EDA
print("\nTingkat Kepentingan Fitur (Machine Learning):")
importance = model_rf.feature_importances_
for i, v in enumerate(importance):
    print(f"- {X.columns[i]:<15} : {v:.4f}")