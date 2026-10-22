# Pertemuan 09 List dan Pengolahan Data Numerik

## Identitas

Nama: Ismaya Catur Dewi Azzahra  
NIM: 2225250018  
Kelas: 3A

## Tujuan

Tujuan dari tugas ini adalah mengolah kumpulan data numerik menggunakan list Python, mengakses dan memanipulasi elemen dengan indeks, slicing, `append`, `insert`, `remove`, dan `pop`, menggabungkan list dengan perulangan, seleksi, dan fungsi untuk menghitung statistik sederhana, serta mengunggah hasil pengerjaan ke GitHub.

## Struktur Program

| File                                  | Keterangan                                                                                    |
| ------------------------------------- | --------------------------------------------------------------------------------------------- |
| `latihan/01_buat_list.py`             | Membuat list lima nilai, menampilkan isi dan banyak data.                                     |
| `latihan/02_indeks_slicing.py`        | Menampilkan elemen pertama, terakhir, tiga elemen awal, dan indeks 1 sampai 3.                |
| `latihan/03_manipulasi_list.py`       | Mengubah, menambah, menyisipkan, dan menghapus elemen list.                                   |
| `latihan/04_agregasi_nilai.py`        | Menghitung total, rata-rata, minimum, dan maksimum.                                           |
| `latihan/05_filter_kelulusan.py`      | Menyaring nilai yang lulus (batas 60) dan menghitung jumlahnya.                               |
| `latihan/06_fungsi_statistik.py`      | Fungsi `rata_rata(data)` yang aman untuk list kosong.                                         |
| `praktik/analisis_nilai_mahasiswa.py` | Ringkasan statistik dan kelulusan dari 10 nilai memakai fungsi `rata_rata` dan `nilai_lulus`. |

## Cara Menjalankan Program

Program dijalankan melalui VS Code menggunakan Python.

Langkah-langkah:

1. Buka folder `pertemuan-09-list-2225250018` di VS Code.
2. Buka file `praktik/analisis_nilai_mahasiswa.py`.
3. Jalankan program melalui terminal dengan perintah `python3 praktik/analisis_nilai_mahasiswa.py` (di Windows gunakan `python`).
4. Periksa ringkasan statistik dan kelulusan yang ditampilkan.
5. Bandingkan hasilnya dengan test case pada bagian Hasil Pengujian.

## Hasil Pengujian

Batas kelulusan = 60.

| Operasi                    | Data                                     | Diharapkan                   | Aktual                       | Status |
| -------------------------- | ---------------------------------------- | ---------------------------- | ---------------------------- | ------ |
| Rata-rata                  | [60, 70, 80]                             | 70.00                        | 70.00                        | Lulus  |
| Minimum / maksimum         | [60, 70, 80]                             | 60 / 80                      | 60 / 80                      | Lulus  |
| Jumlah lulus               | [60, 70, 80]                             | 3                            | 3                            | Lulus  |
| Batas kelulusan            | [59, 60, 61]                             | 2 lulus                      | 2 lulus ([60, 61])           | Lulus  |
| List kosong (rata_rata)    | []                                       | Tidak error                  | 0, tanpa error               | Lulus  |
| Total, rata-rata, min, max | [78, 55, 90, 67, 60, 82, 45, 71, 88, 59] | 695; 69.50; 45; 90           | 695; 69.50; 45; 90           | Lulus  |
| Lulus / belum lulus        | [78, 55, 90, 67, 60, 82, 45, 71, 88, 59] | 7 / 3                        | 7 / 3                        | Lulus  |
| List nilai lulus           | [78, 55, 90, 67, 60, 82, 45, 71, 88, 59] | [78, 90, 67, 60, 82, 71, 88] | [78, 90, 67, 60, 82, 71, 88] | Lulus  |

## Refleksi

Hal yang saya pahami tentang indeks dan list adalah indeks dimulai dari 0, indeks `-1` mengakses elemen terakhir, dan batas akhir pada slicing tidak ikut diambil (`nilai[1:4]` hanya mengambil indeks 1, 2, dan 3).

Kesalahan yang berhasil diperbaiki: pembagi rata-rata harus `len(data)`, bukan angka tetap, dan list kosong perlu diperiksa lebih dulu agar tidak terjadi `ZeroDivisionError`. Selain itu, nilai tepat 60 harus dihitung lulus sehingga operator yang dipakai adalah `>=`, bukan `>`
