-- 1. TABEL MASTER WILAYAH (Sesuai dengan data indonesia.sql)
CREATE TABLE `master_provinsi` (
  `id` char(2) PRIMARY KEY,
  `nama_provinsi` varchar(255)
);

CREATE TABLE `master_kota` (
  `id` char(4) PRIMARY KEY,
  `id_provinsi` char(2),
  `nama_kota` varchar(255)
);

CREATE TABLE `master_kecamatan` (
  `id` char(7) PRIMARY KEY,
  `id_kota` char(4),
  `nama_kecamatan` varchar(255)
);

CREATE TABLE `master_kelurahan` (
  `id` char(10) PRIMARY KEY,
  `id_kecamatan` char(7),
  `nama_kelurahan` varchar(255)
);

-- 2. TABEL PENGGUNA & TOKO
CREATE TABLE `pengguna` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50) UNIQUE NOT NULL,
  `email` varchar(100) UNIQUE NOT NULL,
  `password_hash` varchar(255),
  `nama_lengkap` varchar(100),
  `no_telepon` varchar(20),
  `role_akses` varchar(20) DEFAULT 'USER',
  `saldo_dompet` decimal(15,2) DEFAULT 0,
  `dibuat_pada` timestamp DEFAULT (now())
);

CREATE TABLE `toko` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_pemilik` integer,
  `nama_toko` varchar(100),
  `domain_toko` varchar(50) UNIQUE,
  `id_provinsi` char(2),
  `id_kota` char(4),
  `id_kecamatan` char(7),
  `id_kelurahan` char(10),
  `status_toko` varchar(20),
  `rating_toko` decimal(2,1)
);

CREATE TABLE `alamat` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_pengguna` integer,
  `nama_penerima` varchar(100),
  `no_telepon_penerima` varchar(20),
  `alamat_lengkap` text,
  `id_provinsi` char(2),
  `id_kota` char(4),
  `id_kecamatan` char(7),
  `id_kelurahan` char(10),
  `kode_pos` varchar(10),
  `koordinat_latlong` varchar(50),
  `apakah_utama` boolean
);

-- 3. TABEL MASTER LAINNYA
CREATE TABLE `master_brand_kurir` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nama_brand` varchar(50),
  `logo_url` varchar(255),
  `is_aktif` boolean
);

CREATE TABLE `master_layanan_kurir` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_brand` integer,
  `kode_layanan` varchar(20),
  `nama_tampilan` varchar(50),
  `tipe_layanan` varchar(20),
  `deskripsi` varchar(100)
);

CREATE TABLE `master_group_pembayaran` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nama_group` varchar(50),
  `is_aktif` boolean
);

CREATE TABLE `master_opsi_pembayaran` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_group` integer,
  `nama_opsi` varchar(50),
  `kode_bank` varchar(20),
  `biaya_admin_flat` decimal(10,2),
  `biaya_admin_persen` decimal(5,2),
  `logo_url` varchar(255),
  `is_aktif` boolean
);

-- 4. TABEL TRANSAKSI & PESANAN
CREATE TABLE `produk` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_toko` integer,
  `nama_produk` varchar(255),
  `harga` decimal(12,2),
  `stok` integer,
  `berat_gram` integer,
  `status_aktif` boolean
);

CREATE TABLE `keranjang` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_pengguna` integer,
  `id_produk` integer,
  `jumlah` integer
);

CREATE TABLE `transaksi_pembayaran` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `kode_bayar` varchar(50) UNIQUE,
  `id_pengguna` integer,
  `id_opsi_pembayaran` integer,
  `total_belanja_semua_toko` decimal(15,2),
  `total_ongkir_semua_toko` decimal(15,2),
  `biaya_admin_aplikasi` decimal(10,2),
  `biaya_penanganan_pembayaran` decimal(10,2),
  `total_tagihan_akhir` decimal(15,2),
  `status_bayar` varchar(20),
  `nomor_va_tujuan` varchar(50),
  `batas_waktu_bayar` timestamp
);

CREATE TABLE `pesanan` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `no_pesanan` varchar(50) UNIQUE,
  `id_transaksi_pembayaran` integer,
  `id_toko` integer,
  `id_pembeli` integer,
  `id_alamat_tujuan` integer,
  `id_layanan_kurir` integer,
  `nomor_resi` varchar(50),
  `biaya_ongkir_real` decimal(10,2),
  `tanggal_pesanan` timestamp DEFAULT (now()),
  `estimasi_sampai` date,
  `status_pesanan` varchar(30),
  `total_harga_produk` decimal(12,2),
  `total_akhir_pesanan` decimal(12,2)
);

CREATE TABLE `pesanan_detail` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_pesanan` integer,
  `id_produk` integer,
  `jumlah` integer,
  `harga_saat_beli` decimal(12,2),
  `subtotal` decimal(15,2)
);

CREATE TABLE `admin_activity_log` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_admin` integer,
  `tipe_aksi` varchar(50),
  `deskripsi` text,
  `waktu_aksi` timestamp
);


-- Relasi Wilayah
ALTER TABLE `master_kota` ADD FOREIGN KEY (`id_provinsi`) REFERENCES `master_provinsi` (`id`);
ALTER TABLE `master_kecamatan` ADD FOREIGN KEY (`id_kota`) REFERENCES `master_kota` (`id`);
ALTER TABLE `master_kelurahan` ADD FOREIGN KEY (`id_kecamatan`) REFERENCES `master_kecamatan` (`id`);

-- Relasi Alamat
ALTER TABLE `alamat` ADD FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id`);
ALTER TABLE `alamat` ADD FOREIGN KEY (`id_provinsi`) REFERENCES `master_provinsi` (`id`);
ALTER TABLE `alamat` ADD FOREIGN KEY (`id_kota`) REFERENCES `master_kota` (`id`);
ALTER TABLE `alamat` ADD FOREIGN KEY (`id_kecamatan`) REFERENCES `master_kecamatan` (`id`);
ALTER TABLE `alamat` ADD FOREIGN KEY (`id_kelurahan`) REFERENCES `master_kelurahan` (`id`);

-- Relasi Toko
ALTER TABLE `toko` ADD FOREIGN KEY (`id_pemilik`) REFERENCES `pengguna` (`id`);
ALTER TABLE `toko` ADD FOREIGN KEY (`id_provinsi`) REFERENCES `master_provinsi` (`id`);
ALTER TABLE `toko` ADD FOREIGN KEY (`id_kota`) REFERENCES `master_kota` (`id`);
ALTER TABLE `toko` ADD FOREIGN KEY (`id_kecamatan`) REFERENCES `master_kecamatan` (`id`);
ALTER TABLE `toko` ADD FOREIGN KEY (`id_kelurahan`) REFERENCES `master_kelurahan` (`id`);


ALTER TABLE `keranjang` ADD FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id`);
ALTER TABLE `admin_activity_log` ADD FOREIGN KEY (`id_admin`) REFERENCES `pengguna` (`id`);
ALTER TABLE `produk` ADD FOREIGN KEY (`id_toko`) REFERENCES `toko` (`id`);
ALTER TABLE `keranjang` ADD FOREIGN KEY (`id_produk`) REFERENCES `produk` (`id`);
ALTER TABLE `master_layanan_kurir` ADD FOREIGN KEY (`id_brand`) REFERENCES `master_brand_kurir` (`id`);
ALTER TABLE `master_opsi_pembayaran` ADD FOREIGN KEY (`id_group`) REFERENCES `master_group_pembayaran` (`id`);
ALTER TABLE `transaksi_pembayaran` ADD FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id`);
ALTER TABLE `transaksi_pembayaran` ADD FOREIGN KEY (`id_opsi_pembayaran`) REFERENCES `master_opsi_pembayaran` (`id`);
ALTER TABLE `pesanan` ADD FOREIGN KEY (`id_transaksi_pembayaran`) REFERENCES `transaksi_pembayaran` (`id`);
ALTER TABLE `pesanan` ADD FOREIGN KEY (`id_toko`) REFERENCES `toko` (`id`);
ALTER TABLE `pesanan` ADD FOREIGN KEY (`id_pembeli`) REFERENCES `pengguna` (`id`);
ALTER TABLE `pesanan` ADD FOREIGN KEY (`id_alamat_tujuan`) REFERENCES `alamat` (`id`);
ALTER TABLE `pesanan` ADD FOREIGN KEY (`id_layanan_kurir`) REFERENCES `master_layanan_kurir` (`id`);
ALTER TABLE `pesanan_detail` ADD FOREIGN KEY (`id_pesanan`) REFERENCES `pesanan` (`id`);
ALTER TABLE `pesanan_detail` ADD FOREIGN KEY (`id_produk`) REFERENCES `produk` (`id`);