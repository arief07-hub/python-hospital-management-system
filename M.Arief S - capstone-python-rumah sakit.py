# ============================================================
# CAPSTONE PROJECT MODULE 2
# Judul : Data Pasien Rumah Sakit
# Nama  : Arief
# ============================================================

# --- IMPORT LIBRARY ---
from tabulate import tabulate   # library eksternal untuk menampilkan tabel rapi
                                # (perlu install dulu: pip install tabulate)


# ============================================================
# SECTION 1: DATA (COLLECTION)
# ============================================================
# Data disimpan dalam bentuk LIST OF DICTIONARY.
# - list  -> menampung banyak pasien (bisa ditambah/dihapus)
# - dict  -> tiap pasien punya beberapa field (key : value)
# 'id' adalah kolom UNIK (tidak boleh sama antar pasien).
# 'bayar'  menyimpan uang yang sudah dibayarkan pasien.
# 'dokter' menyimpan nama dokter penanggung jawab.
# 'status' menyimpan status rawat pasien.

data_pasien = [
    {"id": "P001", "nama": "Budi Santoso",   "umur": 45, "penyakit": "Diabetes",   "ruangan": "Melati",  "dokter": "Dr. Hasan", "status": "Rawat Inap",   "biaya": 5000000, "bayar": 5000000},
    {"id": "P002", "nama": "Siti Aminah",    "umur": 30, "penyakit": "Demam",      "ruangan": "Mawar",   "dokter": "Dr. Rina",  "status": "Rawat Jalan",  "biaya": 1500000, "bayar": 1500000},
    {"id": "P003", "nama": "Andi Wijaya",    "umur": 60, "penyakit": "Hipertensi", "ruangan": "Anggrek", "dokter": "Dr. Bagas", "status": "Sudah Pulang", "biaya": 3200000, "bayar": 3200000},
    {"id": "P004", "nama": "Dewi Lestari",   "umur": 28, "penyakit": "Tipes",      "ruangan": "Mawar",   "dokter": "Dr. Rina",  "status": "Rawat Inap",   "biaya": 2800000, "bayar": 2000000},
    {"id": "P005", "nama": "Rudi Hartono",   "umur": 52, "penyakit": "Jantung",    "ruangan": "Melati",  "dokter": "Dr. Hasan", "status": "Rawat Inap",   "biaya": 8500000, "bayar": 8500000},
    {"id": "P006", "nama": "Maya Sari",      "umur": 22, "penyakit": "Demam",      "ruangan": "Anggrek", "dokter": "Dr. Bagas", "status": "Rawat Jalan",  "biaya": 900000,  "bayar": 900000},
    {"id": "P007", "nama": "Joko Prasetyo",  "umur": 67, "penyakit": "Stroke",     "ruangan": "Melati",  "dokter": "Dr. Sari",  "status": "Rawat Inap",   "biaya": 12000000,"bayar": 7000000},
    {"id": "P008", "nama": "Rina Wulandari", "umur": 35, "penyakit": "Diabetes",   "ruangan": "Mawar",   "dokter": "Dr. Sari",  "status": "Sudah Pulang", "biaya": 4100000, "bayar": 4100000},
    {"id": "P009", "nama": "Agus Salim",     "umur": 41, "penyakit": "Hipertensi", "ruangan": "Anggrek", "dokter": "Dr. Rina",  "status": "Rawat Jalan",  "biaya": 1750000, "bayar": 1750000},
    {"id": "P010", "nama": "Nia Ramadhani",  "umur": 19, "penyakit": "Tipes",      "ruangan": "Mawar",   "dokter": "Dr. Bagas", "status": "Rawat Inap",   "biaya": 2400000, "bayar": 2400000},
]

# Daftar pilihan status rawat (dipakai saat Create & Update)
pilihan_status = ["Rawat Inap", "Rawat Jalan", "Sudah Pulang"]


# ============================================================
# SECTION 2: FUNGSI BANTU (HELPER)
# ============================================================
# Fungsi kecil yang dipakai berulang-ulang oleh fitur CRUD.
# Tujuannya: kode efisien, tidak menulis ulang logika yang sama.

def cari_pasien(id_pasien):
    """Mencari 1 pasien berdasarkan ID.
    Mengembalikan dictionary pasien jika ketemu, atau None jika tidak ada."""
    for pasien in data_pasien:          # cek satu per satu isi list
        if pasien["id"] == id_pasien:   # jika ID cocok
            return pasien               # langsung kembalikan datanya
    return None                         # jika loop selesai & tidak ketemu


def id_sudah_ada(id_pasien):
    """Mengecek apakah sebuah ID sudah dipakai (untuk menjaga keunikan)."""
    return cari_pasien(id_pasien) is not None   # True jika ketemu, False jika tidak


def input_angka(pesan):
    """Meminta input yang WAJIB berupa angka.
    Ketik 0 untuk BATAL -> mengembalikan None.
    Selama user salah, pertanyaan diulang terus (looping)."""
    while True:
        nilai = input(pesan)
        if nilai == "0":             # 0 = sinyal batal
            return None              # None menandakan user membatalkan
        if nilai.isdigit():          # isdigit() = True kalau semua karakter angka
            return int(nilai)        # ubah teks menjadi angka lalu kembalikan
        print("  [!] Input harus berupa angka (atau 0 untuk batal).")


def input_teks(pesan):
    """Meminta input teks. Ketik 0 untuk BATAL -> mengembalikan None.
    Teks tidak boleh kosong."""
    while True:
        nilai = input(pesan)
        if nilai == "0":             # 0 = sinyal batal
            return None              # None menandakan user membatalkan
        if nilai.strip() != "":      # .strip() buang spasi; cek tidak kosong
            return nilai.title()     # rapikan Huruf Depan Kapital
        print("  [!] Tidak boleh kosong (atau ketik 0 untuk batal).")


def konfirmasi(pesan):
    """Meminta konfirmasi y/n dari user.
    Mengembalikan True jika setuju (y), False jika tidak (n)."""
    while True:
        jawaban = input(f"{pesan} (y/n): ").lower()   # .lower() -> Y jadi y
        if jawaban == "y":
            return True
        elif jawaban == "n":
            return False
        else:
            print("  [!] Ketik 'y' untuk ya atau 'n' untuk tidak.")


def kembali_ke_menu():
    """Menahan program agar tidak langsung balik ke menu utama.
    User harus menekan Enter dulu untuk kembali."""
    input("\nTekan Enter untuk kembali ke menu utama...")


def pilih_status_rawat():
    """Meminta user memilih status rawat dari daftar yang tersedia.
    Dibuat sebagai pilihan angka agar user tidak salah ketik."""
    print("\nPilih Status Rawat (0 untuk batal):")
    nomor = 1
    for status in pilihan_status:            # tampilkan daftar pilihan
        print(f"{nomor}. {status}")
        nomor += 1

    while True:
        pilihan = input("Pilih (1-3)      : ")
        if pilihan == "0":
            return None                      # batal
        elif pilihan == "1":
            return pilihan_status[0]         # "Rawat Inap"
        elif pilihan == "2":
            return pilihan_status[1]         # "Rawat Jalan"
        elif pilihan == "3":
            return pilihan_status[2]         # "Sudah Pulang"
        else:
            print("  [!] Pilihan tidak valid. Masukkan angka 1-3.")


def generate_id():
    """Membuat ID pasien otomatis, berurutan (P001, P002, ...)."""
    if len(data_pasien) == 0:        # jika data kosong
        return "P001"                # mulai dari P001
    angka_terbesar = 0
    for pasien in data_pasien:
        angka = int(pasien["id"][1:])          # [1:] = buang huruf 'P', sisakan angka
        if angka > angka_terbesar:
            angka_terbesar = angka
    return f"P{angka_terbesar + 1:03d}"        # :03d = angka jadi 3 digit -> 004


def proses_pembayaran(biaya):
    """Sistem pembayaran.
    - Uang yang dibayar diakumulasi (dijumlah) sampai cukup.
    - Jika kurang, user cukup menambah kekurangannya.
    - Jika lebih, kembalian dihitung dan ditampilkan.
    Mengembalikan total uang yang dibayarkan."""
    total_bayar = 0                              # akumulasi uang yang masuk
    print(f"\nTotal biaya yang harus dibayar: Rp{biaya:,}")

    while total_bayar < biaya:                   # selama uang belum cukup
        kurang = biaya - total_bayar             # sisa yang harus dibayar
        print(f"Kekurangan saat ini: Rp{kurang:,}")
        uang = input_angka("Masukkan uang       : ")
        total_bayar += uang                      # tambahkan ke akumulasi

        if total_bayar < biaya:                  # kalau masih kurang
            print(f"  [!] Uang masih kurang Rp{biaya - total_bayar:,}. Tambahkan lagi.")

    kembalian = total_bayar - biaya              # sisa uang = kembalian
    print(f"\nPembayaran LUNAS. Total dibayar: Rp{total_bayar:,}")
    if kembalian > 0:
        print(f"Kembalian: Rp{kembalian:,}")
    else:
        print("Uang pas, tidak ada kembalian.")

    return total_bayar


def tampilkan_tabel(list_pasien):
    """Menampilkan daftar pasien dalam bentuk tabel rapi (pakai tabulate)."""
    header = ["ID", "Nama", "Umur", "Penyakit", "Ruangan", "Dokter", "Status Rawat", "Biaya", "Bayar", "Lunas?"]
    keys   = ["id", "nama", "umur", "penyakit", "ruangan", "dokter", "status", "biaya", "bayar"]

    tabel = []
    for pasien in list_pasien:
        baris = []
        # zip() memasangkan tiap judul kolom dengan key-nya secara sejajar
        for judul, kunci in zip(header, keys):
            nilai = pasien[kunci]
            if kunci in ("biaya", "bayar"):
                nilai = f"Rp{nilai:,}"      # format ribuan -> Rp5,000,000
            baris.append(nilai)
        # kolom terakhir = Lunas jika bayar >= biaya, selain itu Belum Lunas
        if pasien["bayar"] >= pasien["biaya"]:
            baris.append("Lunas")
        else:
            baris.append("Belum Lunas")
        tabel.append(baris)

    print(tabulate(tabel, headers=header, tablefmt="fancy_grid"))


# ============================================================
# SECTION 3: FITUR CREATE (MENAMBAH DATA)
# ============================================================

def create_pasien():
    print("\n=== TAMBAH DATA PASIEN ===")
    print("(Ketik 0 kapan saja untuk membatalkan dan kembali ke menu)")

    id_pasien = generate_id()                 # ID dibuat otomatis oleh sistem
    print(f"ID otomatis untuk pasien ini: {id_pasien}")

    # Tiap input dicek: kalau None berarti user ketik 0 (batal) -> hentikan
    nama = input_teks("Masukkan Nama       : ")
    if nama is None:
        print("Penambahan data dibatalkan.")
        return

    umur = input_angka("Masukkan Umur       : ")
    if umur is None:
        print("Penambahan data dibatalkan.")
        return

    penyakit = input_teks("Masukkan Penyakit   : ")
    if penyakit is None:
        print("Penambahan data dibatalkan.")
        return

    ruangan = input_teks("Masukkan Ruangan    : ")
    if ruangan is None:
        print("Penambahan data dibatalkan.")
        return

    dokter = input_teks("Masukkan Dokter     : ")
    if dokter is None:
        print("Penambahan data dibatalkan.")
        return

    status = pilih_status_rawat()             # status dipilih dari daftar
    if status is None:
        print("Penambahan data dibatalkan.")
        return

    biaya = input_angka("Masukkan Biaya (Rp) : ")
    if biaya is None:
        print("Penambahan data dibatalkan.")
        return

    # Proses pembayaran: uang diakumulasi sampai cukup, lalu hitung kembalian
    bayar = proses_pembayaran(biaya)

    # Gabungkan key + value menjadi satu dictionary pakai zip()
    keys   = ["id", "nama", "umur", "penyakit", "ruangan", "dokter", "status", "biaya", "bayar"]
    values = [id_pasien, nama, umur, penyakit, ruangan, dokter, status, biaya, bayar]
    pasien_baru = dict(zip(keys, values))

    # tampilkan dulu data yang akan disimpan, lalu minta konfirmasi
    print("\nData yang akan disimpan:")
    tampilkan_tabel([pasien_baru])

    if konfirmasi("Simpan data ini?"):
        data_pasien.append(pasien_baru)       # tambahkan ke list
        print(f"\n[OK] Data pasien '{nama}' berhasil ditambahkan!")
    else:
        print("Penambahan data dibatalkan.")


# ============================================================
# SECTION 4: FITUR READ (MENAMPILKAN & MENCARI DATA)
# ============================================================

def read_pasien():
    print("\n=== LIHAT DATA PASIEN ===")

    if len(data_pasien) == 0:                 # jaga-jaga kalau data kosong
        print("Belum ada data pasien.")
        return

    # Sub-menu: user bisa pilih cara melihat data
    print("1. Tampilkan semua data")
    print("2. Cari berdasarkan ID")
    print("3. Cari berdasarkan Nama")
    print("0. Kembali ke menu utama")
    pilihan = input("Pilih (0/1/2/3): ")

    if pilihan == "0":
        return                                # kembali ke menu utama

    if pilihan == "1":
        tampilkan_tabel(data_pasien)
        print(f"Total pasien: {len(data_pasien)}")

    elif pilihan == "2":
        id_pasien = input("Masukkan ID Pasien: ").upper()
        pasien = cari_pasien(id_pasien)
        if pasien:
            tampilkan_tabel([pasien])         # dibungkus [ ] agar bisa ditabelkan
        else:
            print("  [!] Pasien tidak ditemukan.")

    elif pilihan == "3":
        kata = input("Masukkan Nama (sebagian juga bisa): ").title()
        # cari semua pasien yang namanya mengandung kata kunci
        hasil = []
        for pasien in data_pasien:
            if kata in pasien["nama"]:
                hasil.append(pasien)
        if hasil:
            tampilkan_tabel(hasil)
        else:
            print("  [!] Tidak ada nama yang cocok.")
    else:
        print("  [!] Pilihan tidak valid.")


# ============================================================
# SECTION 5: FITUR UPDATE (MENGUBAH DATA)
# ============================================================

def update_pasien():
    print("\n=== UPDATE DATA PASIEN ===")

    id_pasien = input("Masukkan ID Pasien yang akan diubah (0 untuk kembali): ").upper()
    if id_pasien == "0":
        return                                # kembali ke menu utama
    pasien = cari_pasien(id_pasien)

    if pasien is None:                        # kalau ID tidak ada, hentikan
        print("  [!] Pasien tidak ditemukan.")
        return

    print("\nData saat ini:")
    tampilkan_tabel([pasien])

    # User memilih kolom mana yang mau diubah
    print("\nKolom yang bisa diubah:")
    print("1. Nama     2. Umur     3. Penyakit")
    print("4. Ruangan  5. Dokter   6. Status Rawat")
    print("7. Biaya")
    kolom = input("Pilih kolom (1-7): ")

    # simpan dulu nilai barunya ke variabel sementara (belum langsung diubah)
    if kolom == "1":
        field, nilai_baru = "nama", input("Nama baru: ").title()
    elif kolom == "2":
        field, nilai_baru = "umur", input_angka("Umur baru: ")
    elif kolom == "3":
        field, nilai_baru = "penyakit", input("Penyakit baru: ").title()
    elif kolom == "4":
        field, nilai_baru = "ruangan", input("Ruangan baru: ").title()
    elif kolom == "5":
        field, nilai_baru = "dokter", input("Dokter baru: ").title()
    elif kolom == "6":
        field, nilai_baru = "status", pilih_status_rawat()
    elif kolom == "7":
        field, nilai_baru = "biaya", input_angka("Biaya baru: ")
    else:
        print("  [!] Pilihan tidak valid.")
        return

    # tampilan perubahan lama -> baru, minta konfirmasi
    print(f"\nPerubahan: {field} '{pasien[field]}' -> '{nilai_baru}'")
    if konfirmasi("Terapkan perubahan ini?"):
        pasien[field] = nilai_baru            # baru diubah di sini
        print(f"\n[OK] Data pasien '{pasien['nama']}' berhasil diperbarui!")
        tampilkan_tabel([pasien])
    else:
        print("Perubahan dibatalkan.")


# ============================================================
# SECTION 6: FITUR DELETE (MENGHAPUS DATA)
# ============================================================

def delete_pasien():
    print("\n=== HAPUS DATA PASIEN ===")

    id_pasien = input("Masukkan ID Pasien yang akan dihapus (0 untuk kembali): ").upper()
    if id_pasien == "0":
        return                                # kembali ke menu utama
    pasien = cari_pasien(id_pasien)

    if pasien is None:
        print("  [!] Pasien tidak ditemukan.")
        return

    print("\nData yang akan dihapus:")
    tampilkan_tabel([pasien])

    if konfirmasi("Yakin ingin menghapus?"):
        data_pasien.remove(pasien)            # hapus dictionary dari list
        print("[OK] Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


# ============================================================
# SECTION 7: FITUR SORTING (URUTKAN DATA)
# ============================================================

def ambil_biaya(pasien):    # fungsi bantu sebagai 'key' sorting (pengganti lambda)
    return pasien["biaya"]

def ambil_umur(pasien):
    return pasien["umur"]

def urutkan_pasien():
    print("\n=== URUTKAN DATA ===")
    print("1. Biaya (termahal dulu)")
    print("2. Umur (termuda dulu)")
    print("0. Kembali ke menu utama")
    pilihan = input("Pilih (0/1/2): ")

    if pilihan == "0":
        return                                # kembali ke menu utama

    if pilihan == "1":
        # sorted() mengurutkan; key menentukan dasar urutan; reverse=True = besar->kecil
        hasil = sorted(data_pasien, key=ambil_biaya, reverse=True)
    elif pilihan == "2":
        hasil = sorted(data_pasien, key=ambil_umur)
    else:
        print("  [!] Pilihan tidak valid.")
        return
    tampilkan_tabel(hasil)


# ============================================================
# SECTION 8: FITUR STATISTIK (RINGKASAN DATA)
# ============================================================

def statistik_pasien():
    print("\n=== STATISTIK DATA PASIEN ===")

    if len(data_pasien) == 0:
        print("Belum ada data.")
        return

    total_pasien = len(data_pasien)
    total_biaya  = 0
    total_umur   = 0
    pasien_termahal = data_pasien[0]          # anggap data pertama termahal dulu

    for pasien in data_pasien:                # jumlahkan semua sambil cari termahal
        total_biaya += pasien["biaya"]
        total_umur  += pasien["umur"]
        if pasien["biaya"] > pasien_termahal["biaya"]:
            pasien_termahal = pasien

    rata_umur = total_umur / total_pasien     # rata-rata = total / jumlah

    print(f"Total pasien    : {total_pasien}")
    print(f"Total pemasukan : Rp{total_biaya:,}")
    print(f"Rata-rata umur  : {rata_umur:.1f} tahun")   # .1f = 1 angka di belakang koma
    print(f"Pasien termahal : {pasien_termahal['nama']} (Rp{pasien_termahal['biaya']:,})")

    # hitung jumlah pasien per status rawat
    print("\nJumlah pasien per status rawat:")
    for status in pilihan_status:             # cek satu per satu status yang ada
        jumlah = 0
        for pasien in data_pasien:
            if pasien["status"] == status:
                jumlah += 1
        print(f"  {status:<14}: {jumlah} pasien")


# ============================================================
# SECTION 9: MENU UTAMA (PROGRAM BERJALAN DI SINI)
# ============================================================

def menu():
    while True:                               # looping supaya menu muncul terus
        print("\n" + "=" * 44)
        print("     SISTEM DATA PASIEN RUMAH SAKIT")
        print("=" * 44)
        print("1. Lihat Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Urutkan Data")
        print("6. Statistik")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")

                                                # fungsi sesuai pilihan user
        if pilihan == "1":
            read_pasien()
            kembali_ke_menu()
        elif pilihan == "2":
            create_pasien()
            kembali_ke_menu()
        elif pilihan == "3":
            update_pasien()
            kembali_ke_menu()
        elif pilihan == "4":
            delete_pasien()
            kembali_ke_menu()
        elif pilihan == "5":
            urutkan_pasien()
            kembali_ke_menu()
        elif pilihan == "6":
            statistik_pasien()
            kembali_ke_menu()
        elif pilihan == "7":
            print("\nTerima kasih telah menggunakan aplikasi. Sampai jumpa!")
            break                             # keluar dari looping = program berhenti
        else:
            print("  [!] Pilihan tidak valid. Masukkan angka 1-7.")
            kembali_ke_menu()

menu()   # panggil menu() agar aplikasi mulai berjalan