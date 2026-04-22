# UTS
![Visualisasi](asset/uts/uts1.png)
## proses pengerjaan
### Column Filter: 
Melakukan seleksi fitur (feature selection). Tahap ini bertujuan membuang atribut yang tidak memiliki nilai prediktif atau relevansi terhadap hasil akhir, seperti nomor ID, guna mengurangi dimensi data (dimensionality reduction).

### Missing Value: 
Bertugas melakukan imputasi data. Jika terdapat sel atau baris yang kosong (null/NaN), sistem akan menambalnya menggunakan pendekatan statistik (misalnya mengisi dengan rata-rata untuk data numerik atau modus untuk data kategorikal) sehingga integritas jumlah dataset tetap terjaga.

### One to Many: 
Mengaplikasikan teknik One-Hot Encoding. Karena metrik perhitungan jarak pada KNN murni menggunakan operasi matematis, seluruh variabel yang bertipe kategori atau teks dikonversi menjadi representasi variabel biner (angka 0 dan 1) dalam kasus ini adalah tekstur tanah.

### Table Partitioner: 
Membagi dataset ke dalam dua sub-populasi secara acak menggunakan metode holdout. Proporsi pertama 70% dialokasikan sebagai training set untuk melatih algoritma. Proporsi sisanya dialokasikan sebagai testing set untuk menguji objektivitas dan performa model pada observasi yang belum pernah dipelajari.

### Normalizer & Normalizer (Apply): 
Melakukan penskalaan fitur (feature scaling) seperti Min-Max Normalization. Skala seluruh variabel numerik diseragamkan dalam rentang 0 sampai 1 agar variabel dengan angka bernilai besar tidak mendominasi perhitungan jarak. Node Apply di jalur tes memastikan bahwa data uji diskalakan murni mengikuti parameter referensi dari data latih, hal ini sangat krusial untuk mencegah kebocoran informasi (data leakage).

### K Nearest Neighbor: 
Node komputasi utama tempat berjalannya algoritma klasifikasi. Model mengkalkulasi matriks jarak euclidian distance antara setiap baris observasi di data uji dengan observasi di data latih untuk menentukan kelas atau label klasifikasinya.

### Scorer: 
Berfungsi sebagai instrumen evaluasi performa model. Proses ini melakukan komparasi matematis antara label prediksi yang dihasilkan oleh algoritma dengan label aktual (kunci jawaban aslinya), yang kemudian dirangkum dalam bentuk Confusion Matrix serta metrik validasi seperti rasio akurasi (Accuracy).
![Visualisasi](asset/uts/uts2.png)
Berdasarkan data pada tabel tersebut, berikut adalah penjelasan aktual dari performa model yang dievaluasi:
1. Accuracy (Akurasi): Pada tabel, baris Accuracy menunjukkan nilai rata-rata (Mean) sebesar 1. Dalam perhitungan evaluasi machine learning, angka 1 dikonversi menjadi 100%. Ini berarti persentase prediksi model yang benar dari total keseluruhan data uji adalah sempurna (100%).

2. Precision (Presisi): Baris Precision pada tabel juga menunjukkan nilai rata-rata (Mean) sebesar 1. Artinya, ketepatan prediksi kelas positif model ini adalah 100%. Saat model memprediksi suatu data masuk ke dalam kelas tertentu, tebakan tersebut mutlak benar dan sistem sama sekali tidak menghasilkan alarm palsu atau False Positives (terbukti dari nilai Mean pada baris FalsePositives yang berada di angka 0).

3. Recall (Sensitivitas): Baris Recall pun menunjukkan angka rata-rata (Mean) sebesar 1. Ini membuktikan bahwa kemampuan model mendeteksi seluruh kelas aktual adalah 100%. Model berhasil mengenali dan menangkap seluruh data target tanpa ada satu pun yang terlewat (terbukti dari nilai Mean pada baris FalseNegatives yang berada di angka 0).

4. F1-Score (F-measure): Pada KNIME, F1-Score dicantumkan sebagai F-measure. Tabel menunjukkan nilai rata-rata (Mean) metrik ini adalah 1. Karena F1-Score merupakan perhitungan penyeimbang (harmonic mean) antara Precision dan Recall, dan kebetulan kedua nilai tersebut di model ini adalah maksimal (1), maka nilai akhir F1-Score juga mutlak bernilai 1.
![Visualisasi](asset/uts/uts3.png)
1. (Kelas "Tidak Subur" aktual): Terdapat 304 observasi yang pada kenyataannya adalah tanah "Tidak Subur". Model berhasil memprediksi ke-304 data tersebut secara akurat ke dalam kolom "Tidak Subur". Angka 0 pada kolom sebelahnya menunjukkan tidak ada prediksi yang salah sasaran menjadi "Subur" (False Positive).

2. (Kelas "Subur" aktual): Terdapat 296 observasi yang pada kenyataannya adalah tanah "Subur". Model juga berhasil memprediksi ke-296 data tersebut secara akurat ke dalam kolom "Subur", tanpa ada satupun yang meleset ke kolom "Tidak Subur" (terlihat dari angka 0).