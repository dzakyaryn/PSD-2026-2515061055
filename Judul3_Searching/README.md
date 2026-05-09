# Sistem pencarian nilai ujian mahasiswa metode binary search interpolation
# Deskripsi singkat
Pengelolaan data nilai ujian mahasiswa merupakan contoh nyata di mana rekam jejak akademik harus disusun secara terstruktur agar mudah ditelusuri. Ketika dosen mengunggah nilai di akhir semester, data berupa deretan angka tersebut membentuk daftar panjang yang merepresentasikan capaian dari ratusan hingga ribuan mahasiswa. Pengguna sering kali perlu menelusuri capaian akademik secara spesifik, seperti mencari tahu secara cepat letak dan identitas mahasiswa yang mendapatkan nilai batas kelulusan tertentu (misalnya nilai 82) di dalam daftar urutan prestasi. Sistem harus mampu melacak dan menemukan target nilai tersebut di dalam tumpukan data skala besar secara instan tanpa harus memeriksa baris nama mahasiswa satu per satu.

Untuk mengatasi masalah tersebut, algoritma yang sangat tepat untuk diterapkan pada skala pencarian ini adalah Interpolation Search. Algoritma ini dipilih karena memiliki cara kerja yang sangat efisien dan cerdas dalam memprediksi letak nilai ujian secara proporsional berdasarkan rentang nilai terendah dan tertinggi di dalam daftar yang sudah diurutkan. Interpolation Search juga beroperasi dengan melompat langsung ke area data yang relevan, sehingga komputasinya sangat cepat, optimal, dan fleksibel untuk memproses ribuan pencarian secara bersamaan tanpa membebani kinerja memori server universitas
# Source code
<img width="840" height="404" alt="Screenshot 2026-05-08 232243" src="https://github.com/user-attachments/assets/3bcd568b-23a6-41be-8ac4-841601a4e2ba" />
Baris 1: Mendefinisikan fungsi pencarian dengan 3 parameter utama, yaitu array data, panjang array, dan nilai target yang ingin dicari.

Baris 2: Menetapkan batas bawah area pencarian pada indeks pertama atau indeks ke-0.

Baris 3: Menetapkan batas atas area pencarian pada indeks paling akhir dari array.

Baris 4: Memulai perulangan bersyarat, di mana pencarian hanya berjalan selama nilai target berada di dalam rentang batas bawah dan atas, serta indeks tidak saling silang.

Baris 5: Mengecek apakah nilai pada batas atas dan bawah sama persis, guna menghindari error pembagian dengan angka nol pada rumus selanjutnya.

Baris 6: Jika nilainya sama, dilakukan verifikasi apakah nilai tersebut adalah target yang sedang dicari.

Baris 7: Jika benar itu targetnya, program langsung mengembalikan posisi indeks tersebut.

Baris 8: Jika bukan targetnya, perulangan dihentikan secara paksa.

Baris 9: Menghitung estimasi letak indeks menggunakan rumus matematika interpolasi berdasarkan persentase nilai target.

Baris 10: Mencetak hasil tebakan letak indeks beserta nilai di dalamnya ke layar.

Baris 11: Mengevaluasi apakah nilai target ternyata lebih besar dari nilai hasil tebakan.

Baris 12: Jika lebih besar, batas bawah pencarian digeser ke sebelah kanan dari posisi tebakan.

Baris 13: Mengevaluasi apakah nilai target ternyata lebih kecil dari nilai hasil tebakan.

Baris 14: Jika lebih kecil, batas atas pencarian digeser ke sebelah kiri dari posisi tebakan.

Baris 15: Kondisi ketika nilai target sama persis dengan nilai hasil tebakan.

Baris 16: Mengembalikan posisi indeks tebakan tersebut karena data berhasil ditemukan.

Baris 17: Melakukan validasi keamanan terakhir di luar area perulangan untuk mengecek apakah sisa indeks di batas bawah adalah targetnya.

Baris 18: Jika benar, kembalikan indeks batas bawah tersebut.

Baris 19: Mengembalikan nilai -1 sebagai penanda bahwa seluruh proses pencarian gagal dan data tidak ditemukan.
<img width="832" height="407" alt="Screenshot 2026-05-08 232314" src="https://github.com/user-attachments/assets/f0401e36-79a3-41a5-bc67-7dc0cee0a1cb" />
Baris 21: Mendefinisikan fungsi utama untuk menjalankan alur program.

Baris 22: Menyediakan daftar nilai ujian mahasiswa yang sudah diurutkan dari nilai terkecil ke terbesar sebagai database pencarian.

Baris 23: Menghitung dan menyimpan total jumlah elemen dari daftar nilai tersebut.

Baris 24: Mencetak seluruh isi daftar nilai ujian ke layar pengguna.

Baris 25: Mencetak informasi total jumlah data mahasiswa.

Baris 26: Memulai perulangan tanpa henti untuk memastikan pengguna memasukkan data yang benar.

Baris 27: Membuka blok penanganan error untuk memantau proses input.

Baris 28: Meminta pengguna memasukkan angka nilai yang ingin dicari, lalu mengubah formatnya menjadi bilangan bulat.

Baris 29: Jika input berupa angka valid, program akan keluar dari perulangan input.

Baris 30: Menangkap error apabila pengguna memasukkan karakter selain angka (seperti huruf).

Baris 31: Menampilkan pesan teguran error agar pengguna memasukkan ulang dengan format yang benar.

Baris 32: Memanggil fungsi pencarian interpolasi dan menyimpan hasil lokasi indeksnya di sebuah variabel.

Baris 33: Mengevaluasi apakah hasil pencariannya BUKAN bernilai -1 (yang berarti sukses).

Baris 34: Menampilkan pesan keberhasilan beserta lokasi indeks nilai tersebut.

Baris 35: Mengevaluasi kondisi sebaliknya, yaitu jika hasilnya bernilai -1.

Baris 36: Menampilkan pesan bahwa nilai yang dicari tidak terdaftar.

Baris 38: Memastikan bahwa file ini dijalankan secara langsung sebagai program utama.

Baris 39: Mengeksekusi fungsi utama untuk memulai keseluruhan program.
# Output code
<img width="861" height="141" alt="Screenshot 2026-05-08 232404" src="https://github.com/user-attachments/assets/91372464-e44f-413b-9f6e-842736f88187" />
Baris 1: Daftar Nilai Ujian Tersedia: [45, 50, 52, 60, 65, 68, 70, 75, 82, 85, 88, 90, 95]
Program mencetak ke layar keseluruhan isi data nilai ujian yang ada di dalam memori (array). Data ini sudah dalam keadaan terurut dari yang terkecil hingga terbesar sebagai prasyarat pencarian.

Baris 2: Total data mahasiswa: 13
Program menghitung dan menampilkan jumlah total nilai (panjang array) yang akan diproses, yaitu sebanyak 13 elemen data.

Baris 3: Masukkan nilai ujian yang ingin dicari: 75
Sistem meminta pengguna untuk mengetikkan angka yang ingin dicari. Pada baris ini, pengguna memasukkan (input) nilai target yaitu 75 dan menekan Enter.

Baris 4: Posisi estimasi: 6, nilainya: 70
Ini adalah proses iterasi langkah pertama dari algoritma Interpolation Search. Rumus matematika memprediksi letak nilai 75 berada di indeks ke-6. Ketika sistem memeriksa indeks ke-6, ternyata nilainya adalah 70. Karena 75 lebih besar dari 70, program tahu ia harus menggeser pencarian ke sisa data di sebelah kanan.

Baris 5: Posisi estimasi: 7, nilainya: 75
Ini adalah iterasi langkah kedua. Setelah menyesuaikan area pencarian di sebelah kanan, rumus kembali menebak posisi dan kali ini memprediksi letaknya ada di indeks ke-7. Saat diperiksa, nilai pada indeks ke-7 adalah tepat 75.

Baris 6: Ketemu pada indeks ke-7
Karena nilai pada tebakan terakhir sudah cocok dengan nilai target yang dimasukkan pengguna (75 == 75), program menghentikan proses pencarian dan menampilkan kesimpulan akhir bahwa data tersebut berhasil ditemukan di posisi indeks ke-7.
# Link youtube
https://youtu.be/nhO3bkeTO-8
