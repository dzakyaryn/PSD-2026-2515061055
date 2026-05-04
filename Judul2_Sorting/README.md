# Pengurutan Pengeluaran Jajan Harian
# Deskripsi Singkat
Pencatatan pengeluaran jajan harian merupakan contoh nyata di mana riwayat transaksi keuangan harus disusun secara terstruktur agar mudah dievaluasi. Ketika pengguna mencatat pengeluaran setiap hari, data seperti jenis makanan dan harga masuk secara acak seiring berjalannya waktu. Pengguna sering kali perlu mengevaluasi kebiasaan konsumsi mereka, seperti mencari tahu jajan apa yang paling menguras dompet dari yang termahal hingga yang termurah. Sistem harus mampu mengubah kumpulan data pengeluaran yang berantakan tersebut menjadi terurut tanpa mengubah detail informasi di dalamnya.

Untuk mengatasi masalah tersebut, algoritma yang paling tepat untuk diterapkan adalah Selection Sort. Algoritma ini dipilih karena memiliki cara kerja yang sangat efisien untuk mencari nilai maksimum atau minimum dari kumpulan data dan langsung memindahkannya ke urutan teratas atau terbawah. Selection Sort juga tidak membutuhkan memori tambahan sehingga sangat ringan, optimal, dan fleksibel untuk memproses jumlah data harian atau mingguan pada perangkat dengan spesifikasi terbatas.
# Source Code 
<img width="854" height="342" alt="Screenshot 2026-05-03 212942" src="https://github.com/user-attachments/assets/528dae23-d0b8-4298-bdb8-859007e5dc7d" />
Baris 1: Mendefinisikan fungsi bernama tukar yang menerima parameter array, dan dua posisi indeks i dan j

Baris 2: Menyimpan data array indeks i ke dalam variabel sementara bernama temp

Baris 3: Menukar data array indeks i dengan data array indeks j

Baris 4: Menukar data array indeks j dengan data array indeks i yang asli

Baris 7: Mendefinisikan fungsi bernama selection_sort_pengeluaran yang menerima parameter data array dan n yaitu jumlah data

Baris 8: Melakukan Perulangan sebagai penanda batas yang belum terurut

Baris 9: Menyimpan posisi i ke dalam variabel bernama pos, ini sebagai asumsi bahwa posisi i memiliki harga termahal

Baris 10: melakukan perulangan untuk mengecek sisa data di sebelah kanan

Baris 11: Melakukan perbandingan khusus pada kunci harga apakah array j lebih besar dari array pos  

Baris 12: jika lebih mahal, rubah nilai pos dengan posisi j

Baris 13: jika pos tidak sama dengan i, artinya memeriksa apakah ada harga yang lebih besar

Baris 14: Melakukan pertukaran posisi i dan pos menggunakan fungsi tukar

Baris 1: Mendefinisikan fungsi tukar untuk menukar posisi dua elemen dalam array.  

Baris 2: Menyimpan nilai array indeks ke-i ke dalam variabel sementara temp.  

Baris 3: Mengganti nilai array indeks ke-i dengan nilai dari indeks ke-j.  

Baris 4: Memasukkan nilai dari variabel temp ke array indeks ke-j.  

Baris 5: Baris kosong.  

Baris 6: Baris kosong.  

Baris 7: Mendefinisikan fungsi selection_sort_pengeluaran untuk mengurutkan data.  

Baris 8: Memulai perulangan luar sebagai batas area data yang belum terurut.  

Baris 9: Menetapkan indeks i sebagai posisi harga termurah sementara.  

Baris 10: Memulai perulangan dalam untuk memindai sisa data di sebelah kanan.  

Baris 11: Memeriksa apakah harga di indeks j lebih murah dari harga di posisi termurah saat ini.  

Baris 12: Jika ya, perbarui posisi termurah menjadi indeks j.  

Baris 13: Memeriksa apakah posisi termurah berubah dari asumsi awal di indeks i.  
Baris 14: Jika berubah, panggil fungsi tukar untuk memindahkan data tersebut ke depan.  


<img width="832" height="421" alt="Screenshot 2026-05-03 213007" src="https://github.com/user-attachments/assets/0034ba6c-0307-4945-8b44-0d7bbcc30cde" />

Baris 17: Mendefinisikan fungsi main sebagai program utama.  

Baris 18: Memulai blok penanganan error untuk input pengguna awal.  

Baris 19: Meminta input jumlah data jajan dan mengubahnya menjadi format angka.  

Baris 20: Menangkap error jika pengguna tidak memasukkan angka.  

Baris 21: Menampilkan pesan peringatan input tidak valid.  

Baris 22: Menghentikan eksekusi fungsi karena input jumlah data salah.  

Baris 23: Membuat daftar kosong bernama pengeluaran untuk menyimpan data.  

Baris 24: Mencetak instruksi untuk memasukkan data.  

Baris 25: Memulai perulangan untuk menanyakan input sebanyak jumlah data.  

Baris 26: Mencetak teks penanda urutan data yang sedang diinput.  

Baris 27: Meminta pengguna mengetik nama hari.  

Baris 28: Meminta pengguna mengetik nama jajanan.  

Baris 29: Memulai perulangan khusus untuk memvalidasi input harga.  

Baris 30: Membuka blok penanganan error khusus input harga.  

Baris 31: Meminta input nominal harga dan memaksanya menjadi angka.  

Baris 32: Menghentikan perulangan validasi harga jika input angka berhasil.  

Baris 33: Menangkap error jika input harga bukan angka.  

Baris 34: Menampilkan peringatan untuk memasukkan angka.  

<img width="843" height="331" alt="Screenshot 2026-05-03 213054" src="https://github.com/user-attachments/assets/8ab78e8f-0b6f-42ae-8ee1-3c837eeaf92d" />


Baris 35: Menggabungkan hari, jajan, dan harga ke dalam satu objek Dictionary.  

Baris 36: Menambahkan Dictionary tersebut ke dalam daftar pengeluaran.  

Baris 37: Mencetak teks pembuka sebelum menampilkan daftar acak.  

Baris 38: Melakukan perulangan untuk membaca daftar yang belum diurutkan.  

Baris 39: Mencetak detail hari, jajan, dan harga sesuai urutan masuk.  

Baris 40: Memanggil fungsi untuk mengurutkan daftar pengeluaran.  

Baris 41: Mencetak teks pembuka sebelum menampilkan hasil urutan.  

Baris 42: Melakukan perulangan untuk membaca daftar yang sudah diurutkan.  

Baris 43: Mencetak detail pengeluaran dari harga termurah ke termahal.

Baris 47: Memeriksa apakah file ini dijalankan secara langsung

Baris 48: Menjalankan fungsi main() untuk memulai eksekusi program

# Output Code
<img width="784" height="307" alt="Screenshot 2026-05-04 223152" src="https://github.com/user-attachments/assets/c7c66528-e4e0-4a4b-bc00-411d35aa0cd9" />
Baris 2: Pengguna menginput angka 5 untuk menentukan jumlah data jajan yang akan dicatat.

Baris 3: Mencetak instruksi bahwa pengisian elemen array dimulai.

Baris 4: Menampilkan teks penanda untuk pengisian data ke-1.

Baris 5: Pengguna menginput nama hari untuk data ke-1 (senin).

Baris 6: Pengguna menginput nama jajan untuk data ke-1 (mie ayam).

Baris 7: Pengguna menginput harga untuk data ke-1 (13000).

Baris 8: Menampilkan teks penanda untuk pengisian data ke-2.

Baris 9: Pengguna menginput nama hari untuk data ke-2 (selasa).

Baris 10: Pengguna menginput nama jajan untuk data ke-2 (bakso).

Baris 11: Pengguna menginput harga untuk data ke-2 (10000).

Baris 12: Menampilkan teks penanda untuk pengisian data ke-3.

Baris 13: Pengguna menginput nama hari untuk data ke-3 (selasa).

Baris 14: Pengguna menginput nama jajan untuk data ke-3 (sate ayam).

Baris 15: Pengguna menginput harga untuk data ke-3 (16000).

Baris 16: Menampilkan teks penanda untuk pengisian data ke-4.

Baris 17: Pengguna menginput nama hari untuk data ke-4 (rabu).

Baris 18: Pengguna menginput nama jajan untuk data ke-4 (kopi).

Baris 19: Pengguna menginput harga untuk data ke-4 (19000).


<img width="785" height="280" alt="Screenshot 2026-05-04 223210" src="https://github.com/user-attachments/assets/be5aa0d1-6e81-4491-9c75-b7b2f9b9ec86" />

Baris 20: Menampilkan teks penanda untuk pengisian data ke-5 (terakhir).

Baris 21: Pengguna menginput nama hari untuk data ke-5 (kamis).

Baris 22: Pengguna menginput nama jajan untuk data ke-5 (mie gacoan).

Baris 23: Pengguna menginput harga untuk data ke-5 (13000).

Baris 24: Mencetak teks pembuka untuk menampilkan daftar jajan awal.

Baris 25: Menampilkan rekap data ke-1 sesuai urutan input (senin | mie ayam | Rp13000).

Baris 26: Menampilkan rekap data ke-2 sesuai urutan input (selasa | bakso | Rp10000).

Baris 27: Menampilkan rekap data ke-3 sesuai urutan input (selasa | sate ayam | Rp16000).

Baris 28: Menampilkan rekap data ke-4 sesuai urutan input (rabu | kopi | Rp19000).

Baris 29: Menampilkan rekap data ke-5 sesuai urutan input (kamis | mie gacoan | Rp13000).

Baris 30: Mencetak teks pembuka untuk hasil akhir pengurutan (Selection Sort).

Baris 31: Menampilkan urutan pertama (termahal) hasil algoritma (rabu | kopi | Rp19000).

Baris 32: Menampilkan urutan kedua termahal (selasa | sate ayam | Rp16000).

Baris 33: Menampilkan urutan ketiga termahal (senin | mie ayam | Rp13000).

Baris 34: Menampilkan urutan keempat termahal (kamis | mie gacoan | Rp13000).

Baris 35: Menampilkan urutan kelima atau termurah (selasa | bakso | Rp10000).

