import pandas as pd
import numpy as np

np.random.seed(42)
file_name = 'Simulasi_ECommerce_20Sheet.xlsx'

with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
    for i in range(1, 21):
        n_rows = 500
        
        harga = np.random.randint(10000, 500000, n_rows)
        diskon = np.random.uniform(0, 70, n_rows)
        rating = np.random.uniform(1.0, 5.0, n_rows)
        ulasan = np.random.randint(0, 2000, n_rows)
        biaya_iklan = np.random.randint(0, 100000, n_rows)
        
        df = pd.DataFrame({
            'ID_Produk': [f'PRD_{i}_{j}' for j in range(1, n_rows + 1)],
            'Harga': harga,
            'Diskon_Persen': diskon,
            'Rating': rating,
            'Jumlah_Ulasan': ulasan,
            'Biaya_Iklan': biaya_iklan
        })
        
        # PERBAIKAN LOGIKA: Ambang batas diturunkan ke 1.5 agar data lebih balance
        skor_laris = (rating * 0.4) + (ulasan / 2000 * 0.3) + (diskon / 70 * 0.3)
        df['Kelarisan'] = np.where(skor_laris > 1.5, 1, 0) # threshold baru
        
        sheet_name = f'Kategori_{i}'
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"File {file_name} BERHASIL DIPERBAIKI dengan data yang lebih seimbang!")