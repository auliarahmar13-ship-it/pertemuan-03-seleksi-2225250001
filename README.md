
# Pertemuan 03 – Dasar Python (Percabangan)

## Identitas Mahasiswa

| Keterangan | Isi |
|---|---|
| Nama | Aulia Rahma Ramadhani |
| NIM | 2225250001 |
| Kelas | 3A |
| Mata Kuliah | Algoritma dan Pemrograman |

---

## Tujuan Repositori

Repositori ini berisi latihan dan tugas Pertemuan 03 mengenai percabangan (`if`, `elif`, `else`) menggunakan Python. Seluruh program dibuat sesuai modul dan telah diuji menggunakan test case yang diberikan dosen.

---

## Daftar Berkas

| Folder/File | Fungsi |
|---|---|
| `README.md` | Dokumentasi Pertemuan 03 |
| `latihan/01_genap_ganjil.py` | Menentukan bilangan genap atau ganjil |
| `latihan/02_bandingkan_dua_bilangan.py` | Membandingkan dua bilangan |
| `latihan/03_kelulusan_bersyarat.py` | Menentukan status kelulusan berdasarkan nilai dan kehadiran |
| `latihan/04_jenis_segitiga.py` | Menentukan jenis segitiga dari tiga sisi |
| `tugas/analisis_persamaan_kuadrat.py` | Menganalisis jenis akar persamaan kuadrat |

---

## Cara Menjalankan

Buka terminal pada folder **Pertemuan-03**, kemudian jalankan program dengan perintah berikut.

```bash
python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
python tugas/analisis_persamaan_kuadrat.py
```

---

# Hasil Test Case

## Latihan 1 – Genap atau Ganjil

| Input | Output |
|---|---|
| 8 | Genap |
| 13 | Ganjil |
| 0 | Genap |
| -7 | Ganjil |

**Penjelasan:** Program mengecek sisa hasil bagi 2. Jika sisa = 0 maka genap, selain itu ganjil.

---

## Latihan 2 – Membandingkan Dua Bilangan

| Bilangan 1 | Bilangan 2 | Output |
|---:|---:|---|
| 7 | 4 | Bilangan pertama lebih besar |
| 2 | 9 | Bilangan pertama lebih kecil |
| 5 | 5 | Kedua bilangan sama |
| -3 | -8 | Bilangan pertama lebih besar |

**Penjelasan:** Program menggunakan nested `if` untuk menentukan apakah bilangan pertama lebih besar, sama, atau lebih kecil.

---

## Latihan 3 – Kelulusan Bersyarat

| Nilai | Kehadiran | Hasil |
|---:|---:|---|
| 75 | 90 | Lulus |
| 59 | 90 | Belum lulus |
| 75 | 79 | Belum lulus |
| 60 | 80 | Lulus |

**Penjelasan:** Mahasiswa dinyatakan lulus apabila **nilai ≥ 60** dan **kehadiran ≥ 80%**.

---

## Latihan 4 – Jenis Segitiga

| Sisi (a,b,c) | Hasil |
|---|---|
| 3, 3, 3 | Sama sisi |
| 5, 5, 8 | Sama kaki |
| 3, 4, 5 | Sembarang |
| 1, 2, 3 | Tidak membentuk segitiga |

**Penjelasan:** Program memeriksa syarat terbentuknya segitiga terlebih dahulu, kemudian menentukan jenisnya menggunakan nested `if`.

---

## Tugas – Analisis Persamaan Kuadrat

| a | b | c | D | Hasil |
|---:|---:|---:|---:|---|
| 1 | -5 | 6 | 1 | Dua akar real: 3.00 dan 2.00 |
| 1 | 2 | 1 | 0 | Akar kembar: -1.00 |
| 1 | 0 | 1 | -4 | Tidak ada akar real |
| 0 | 2 | 3 | - | Bukan persamaan kuadrat |

**Penjelasan:** Program menghitung diskriminan (`D = b² - 4ac`) untuk menentukan apakah persamaan memiliki dua akar real, akar kembar, tidak memiliki akar real, atau bukan persamaan kuadrat.

---

## Refleksi

Pada Pertemuan 03 saya mempelajari penggunaan percabangan (`if`, `elif`, dan `else`) serta nested `if` untuk menyelesaikan berbagai kasus, seperti menentukan bilangan genap/ganjil, membandingkan dua bilangan, menentukan kelulusan, mengidentifikasi jenis segitiga, dan menganalisis akar persamaan kuadrat.

---

## Sumber

- Modul/Panduan Algoritma dan Pemrograman Pertemuan 03.