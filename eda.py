import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 1. Load Data dari 20 Sheet
all_sheets = pd.read_excel('Simulasi_ECommerce_20Sheet.xlsx', sheet_name=None)
df_all = pd.concat(all_sheets.values(), ignore_index=True)

print("Total Data:", df_all.shape)

# 2. Preprocessing: Pengecekan Missing Values
print("\nMissing Values:\n", df_all.isnull().sum())
# (Karena ini data dummy, tidak akan ada missing values. Jika ada, gunakan df.fillna() atau df.dropna())

# 3. EDA: Distribusi Target Kelarisan
plt.figure(figsize=(6,4))
sns.countplot(x='Kelarisan', data=df_all)
plt.title('Distribusi Kelarisan Produk (0 = Tidak, 1 = Laris)')
plt.show()

# 4. EDA: Korelasi Antar Variabel Numerik
plt.figure(figsize=(8,6))
kolom_numerik = ['Harga', 'Diskon_Persen', 'Rating', 'Jumlah_Ulasan', 'Biaya_Iklan', 'Kelarisan']
sns.heatmap(df_all[kolom_numerik].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriks Korelasi Fitur Numerik')
plt.show()

# 5. Preprocessing: Standarisasi Fitur
fitur = ['Harga', 'Diskon_Persen', 'Rating', 'Jumlah_Ulasan', 'Biaya_Iklan']
scaler = StandardScaler()
df_all[fitur] = scaler.fit_transform(df_all[fitur])

print("\nData setelah Preprocessing (Standard Scaling):\n", df_all.head())