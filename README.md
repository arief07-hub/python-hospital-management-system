# Sistem Data Pasien Rumah Sakit

> **Capstone Project Module 2 — Python Fundamentals**
> Aplikasi CLI (Command Line Interface) untuk mengelola data pasien rumah sakit menggunakan Python dasar.

---

## Deskripsi

**Sistem Data Pasien Rumah Sakit** adalah aplikasi berbasis terminal yang dibuat untuk mengelola data pasien di sebuah rumah sakit. Aplikasi ini mengimplementasikan operasi **CRUD** (Create, Read, Update, Delete) sebagai fitur utama, dilengkapi dengan fitur tambahan seperti sistem pembayaran, pencarian, pengurutan, dan statistik.

Seluruh menu utama dibangun menggunakan **regular function** dan data disimpan dalam **list of dictionary**, sesuai dengan materi yang dipelajari pada Module 2.

---

## Fitur

### Fitur Utama (CRUD)
- **Create** — Menambah data pasien baru dengan ID otomatis dan sistem pembayaran.
- **Read** — Menampilkan seluruh data, mencari berdasarkan ID, atau berdasarkan nama.
- **Update** — Mengubah data pasien pada kolom tertentu dengan konfirmasi.
- **Delete** — Menghapus data pasien dengan konfirmasi terlebih dahulu.

### Fitur Tambahan
- **Sistem Pembayaran** — Uang yang dibayarkan diakumulasi sampai cukup; jika lebih, kembalian dihitung otomatis.
- **Pencarian** — Cari pasien berdasarkan ID atau sebagian nama.
- **Statistik** — Total pasien, total pemasukan, rata-rata umur, pasien termahal, dan jumlah pasien per status rawat.
- **Pengurutan (Sorting)** — Urutkan data berdasarkan biaya atau umur.
- **ID Otomatis** — Sistem membuat ID pasien berurutan secara otomatis (P001, P002, ...).
- **Validasi Input** — Mencegah input tidak valid (misalnya huruf pada kolom angka).
- **Konfirmasi Aksi** — Konfirmasi sebelum menyimpan, mengubah, atau menghapus data.

---

## Struktur Data

Setiap pasien memiliki **9 field**, dengan `id` sebagai kolom unik:

| Field      | Tipe    | Keterangan                          |
|------------|---------|-------------------------------------|
| `id`       | string  | ID unik pasien (contoh: P001)       |
| `nama`     | string  | Nama pasien                         |
| `umur`     | integer | Umur pasien                         |
| `penyakit` | string  | Diagnosa/penyakit                   |
| `ruangan`  | string  | Ruangan tempat pasien dirawat       |
| `dokter`   | string  | Dokter penanggung jawab             |
| `status`   | string  | Status rawat (Inap/Jalan/Pulang)    |
| `biaya`    | integer | Total biaya perawatan               |
| `bayar`    | integer | Total uang yang sudah dibayarkan    |

---
## Instalasi

### Prasyarat
- Python 3.x
- Library `tabulate`

### Langkah-langkah

1. Clone repository ini:
   ```bash
   git clone https://github.com/USERNAME/nama-repo.git
   cd nama-repo
   ```

2. Install library yang dibutuhkan:
   ```bash
   pip install tabulate
   ```

3. Jalankan program:
   ```bash
   python M_Arief_S_-_capstone-python-rumah_sakit.py
   ```
---
## Cara Penggunaan

Setelah program dijalankan, akan muncul menu utama:

```
============================================
     SISTEM DATA PASIEN RUMAH SAKIT
============================================
1. Lihat Data
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Urutkan Data
6. Statistik
7. Keluar
Pilih menu (1-7):
```

Pilih menu dengan mengetik angka **1–7**, lalu ikuti petunjuk pada layar.
Pada beberapa menu, ketik **0** untuk membatalkan atau kembali.

### Contoh: Sistem Pembayaran

Saat menambah pasien dengan biaya Rp2.000.000:
- Jika Anda membayar Rp1.000.000 → sistem meminta kekurangan Rp1.000.000.
- Anda tambah Rp1.500.000 → total menjadi Rp2.500.000 → **LUNAS**, kembalian Rp500.000.

---

## Struktur Kode

Program terbagi menjadi 9 bagian:

1. **Import Library** — memanggil `tabulate`.
2. **Data (Collection)** — list of dictionary berisi data pasien.
3. **Fungsi Bantu** — fungsi yang dipakai berulang (`cari_pasien`, `input_angka`, `konfirmasi`, dll).
4. **Fitur Create** — menambah data.
5. **Fitur Read** — menampilkan & mencari data.
6. **Fitur Update** — mengubah data.
7. **Fitur Delete** — menghapus data.
8. **Fitur Sorting & Statistik** — mengurutkan dan meringkas data.
9. **Menu Utama** — pusat kendali program (looping).

---

## Teknologi

- **Python 3** — bahasa pemrograman utama.
- **tabulate** — library untuk menampilkan data dalam bentuk tabel.

---

## Konsep yang Diterapkan

- Data collection (list & dictionary)
- Conditional statement (if / elif / else)
- Looping (for & while)
- Regular function & return value
- Input validation
- String formatting

---

## Penulis

**M. Arief S.**
Capstone Project Module 2 — Business Intelligence Analyst
