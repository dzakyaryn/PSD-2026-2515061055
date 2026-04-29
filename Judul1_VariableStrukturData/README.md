# Pengelolaan antrean lagu pada Platform Streaming Musik

# Deskripsi Singkat
Pengelolaan antrean lagu pada platform streaming musik merupakan contoh nyata dimana data harus disimpan secara berurutan namun fleksibel. ketika pengguna memutar lagu, mereka dapat menambahkan lagu ke daftar antrean seperti "tambahkan ke antrean", menghapus lagu dari daftar antrean, atau hanya ingin berpindah maju atau mundur ke lagu tertentu secara instan. sistem harus mampu menampung antrean yang selalu berubah-ubah tanpa menghentikan proses pemutaran lagu yang sedang berjalan.

Untuk mengatasi masalah tersebut, struktur data yang paling tepat adalah vektor (array dinamis). Vektor dipilih karena memiliki  kemampuan  untuk  mengakses data  secara instan saat sistem harus melompat ke lagu tertentu. Vektor juga dapat memperbesar atau memperkecil kapasitas ruang saat antrean sudah penuh oleh lagu-lagu sehingga manajemen memori menjadi lebih dinamis dan fleksibel.

# Source Code
baris 1 sampai 44 adalah source code deklarasi dari class vektor yang sama dengan source code modul praktikum struktur data. Baris 45 sampai selanjutnya akan dijelaskan perbaris source code dari sistem pengelolaan antrean lagu pada platform streaming musik.

<img width="850" height="262" alt="Screenshot 2026-04-29 184556" src="https://github.com/user-attachments/assets/a51cd30e-cc4b-42f6-a1bd-f5be250669d8" />
Baris 45: Membuat sebuah cetakan utama (class) bernama Antrean_Manager.

Baris 46: Membuat fungsi pengaturan awal (__init__) yang otomatis berjalan saat sistem antrean dibuat.

Baris 47: Menyiapkan variabel self.antrean menggunakan ruang memori Vector() untuk menampung daftar lagu.

Baris 48: Membuat penunjuk memori self.indeks_now mulai dari angka 0 untuk mengingat lagu mana yang sedang diputar.

Baris 50: Membuat fungsi tambah_lagu yang bertugas menerima input data berupa judul_lagu.

Baris 51: Menyisipkan judul_lagu tersebut ke urutan paling belakang di dalam self.antrean.

Baris 52: Mencetak teks pemberitahuan ke layar bahwa lagu berhasil dimasukkan.
<img width="895" height="207" alt="Screenshot 2026-04-29 184714" src="https://github.com/user-attachments/assets/dc597783-a112-44e2-aea7-2a4b40de4f50" />
Baris 54: Membuat fungsi putar_sekarang yang bertugas untuk mengambil dan memainkan lagu dari dalam antrean.

Baris 55: Memeriksa apakah jumlah lagu di dalam memori self.antrean kosong (bernilai 0).

Baris 56: Jika antrean ternyata benar-benar kosong, sistem akan mencetak teks peringatan ke layar.

Baris 57: Perintah return digunakan untuk menghentikan fungsi ini secara paksa dan keluar. Ini sangat penting agar komputer tidak memaksa membaca baris selanjutnya.

Baris 58: Mengambil judul lagu dari self.antrean secara spesifik pada posisi yang ditunjuk oleh self.indeks_now, lalu menyimpan judul tersebut ke dalam variabel sementara bernama lagu.

Baris 59: Mencetak teks ke layar untuk menampilkan judul lagu yang baru saja diambil dan sedang diputar.
<img width="825" height="250" alt="Screenshot 2026-04-29 184753" src="https://github.com/user-attachments/assets/c11a9d31-dd1d-4b7d-a9fb-6e6dcdd1fd59" />
Baris 61: Mendefinisikan fungsi next_lagu yang bertugas untuk melompat dan memutar lagu selanjutnya di dalam antrean.
Baris 62: Mengecek apakah isi antrean sedang kosong.

Baris 63: Mencetak teks peringatan ke layar jika antreannya memang benar-benar kosong.

Baris 64: Mengecek apakah lagu yang sedang diputar saat ini bukan lagu terakhir. Caranya dengan memastikan nilai indeks_now masih lebih kecil dari indeks paling ujung (yaitu total size() - 1).

Baris 65: Jika masih ada lagu selanjutnya, geser posisi penunjuk (indeks_now) maju 1 langkah dengan cara menambahkannya dengan angka 1.

Baris 66: Memanggil fungsi putar_sekarang() yang sudah di buat sebelumnya agar sistem langsung memutar lagu di posisi indeks yang baru tersebut.

Baris 67: Kondisi else (jika sebaliknya), yang akan otomatis berjalan apabila pengecekan di baris 64 tidak terpenuhi (artinya indeks_now sudah berada di ujung akhir antrean).

Baris 68: Mencetak pesan pemberitahuan ke layar bahwa pengguna sudah berada di penghujung playlist dan tidak bisa melakukan next lagi.
<img width="797" height="244" alt="Screenshot 2026-04-29 184820" src="https://github.com/user-attachments/assets/bb4e16c0-b839-41d9-b185-9a46f60b96c3" />
Baris 69: Mendefinisikan fungsi prev_lagu yang bertugas untuk mundur dan memutar lagu sebelumnya di dalam antrean.

Baris 70: Mengecek apakah isi antrean sedang kosong.

Baris 71: Mencetak teks peringatan ke layar jika antreannya memang kosong.

Baris 72: Mengecek apakah lagu yang diputar saat ini bukan lagu paling pertama. Caranya dengan memastikan nilai indeks_now lebih besar dari 0.

Baris 73: Jika ya, geser posisi penunjuk (indeks_now) mundur 1 langkah dengan cara menguranginya dengan angka 1.

Baris 74: Memanggil fungsi putar_sekarang() agar sistem langsung memutar lagu di posisi indeks yang baru (mundur) tersebut.

Baris 75: Kondisi else, yang akan otomatis berjalan apabila pengguna mencoba menekan tombol previous padahal mereka sudah berada di indeks 0 (lagu urutan paling awal).

Baris 76: Mencetak pesan peringatan ke layar bahwa pengguna tidak bisa mundur lagi.
<img width="853" height="266" alt="Screenshot 2026-04-29 184835" src="https://github.com/user-attachments/assets/06986000-573c-49da-aef4-09499d1367f7" />
Baris 77: Mendefinisikan fungsi hapus_lagu yang bertugas untuk membuang lagu urutan paling akhir dari dalam antrean.

Baris 78: Mengecek apakah antrean memiliki isi (jumlah lagu lebih besar dari 0).

Baris 79: Melakukan pengecekan kondisi khusus: Apakah lagu yang sedang diputar saat ini kebetulan adalah lagu di urutan paling belakang (size() - 1) DAN antrean tersebut memiliki lebih dari satu lagu (indeks_now > 0)?

Baris 80: Jika kondisi di baris 79 benar, maka sistem akan menggeser penunjuk (indeks_now) mundur 1 langkah (-= 1).

Baris 81: Memanggil fungsi pop_back() pada self.antrean (Vector) untuk mengeksekusi penghapusan lagu di slot paling belakang.

Baris 82: Mencetak pesan konfirmasi ke layar bahwa penghapusan berhasil dilakukan.

Baris 83: Kondisi else, yang akan otomatis tereksekusi jika syarat di baris 78 tidak terpenuhi (artinya ukuran antrean adalah 0 alias kosong).

Baris 84: Mencetak pesan peringatan ke layar bahwa tidak ada tindakan penghapusan yang dilakukan karena antrean sudah tidak memiliki lagu.
<img width="828" height="230" alt="image" src="https://github.com/user-attachments/assets/aabeec75-151a-44d2-8e32-0a8f5e78328c" />
Baris 87: Mendefinisikan fungsi main(), yang berfungsi sebagai ruang utama untuk menjalankan perintah-perintah aplikasi Anda.

Baris 88: Membuat sebuah "sistem pengelola antrean" baru dari cetakan Antrean_Manager(), lalu memberinya nama yd_music.

Baris 90: Menyuruh sistem yd_music untuk menambahkan lagu "Love me not" ke dalam antrean.

Baris 91: Menyuruh sistem menambahkan lagu "Somebody pleasure" ke urutan selanjutnya.

Baris 92: Menyuruh sistem menambahkan lagu "Happiness" ke urutan selanjutnya lagi.

Baris 93: Perintah ini mengakses langsung memori antrean (yaitu si Vector) milik yd_music, lalu memicu fungsi display() bawaan Vector tersebut. Tujuannya adalah untuk mencetak seluruh isi antrean lagu ke layar terminal sekaligus.
<img width="823" height="251" alt="image" src="https://github.com/user-attachments/assets/afa8097b-e53f-4966-9a88-c83ede537ca7" />
Baris 86: Menyuruh sistem yd_music untuk menjalankan fungsi putar_sekarang(), yang akan menampilkan/memainkan lagu pada urutan saat ini (karena baru mulai, ini akan memutar lagu pertama).

Baris 87: Menyuruh sistem menjalankan fungsi next_lagu() untuk melompat dan memutar lagu urutan kedua.

Baris 89: Menyuruh mesin menjalankan fungsi hapus_lagu() untuk membuang lagu yang berada di posisi paling akhir dalam antrean.

Baris 90: Memanggil kembali fungsi putar_sekarang() untuk memastikan dan menampilkan lagu apa yang saat ini sedang aktif setelah ada proses penghapusan.

Baris 92: Ini adalah "penjaga pintu" (entry point) standar di Python. Baris ini mengecek apakah file kode sedang dieksekusi secara langsung sebagai program utama (bukan sekadar diimpor ke file Python lain).

Baris 93: Jika pengecekan di baris 92 benar, maka baris ini akan memanggil fungsi main() (yang berisi semua perintah tambah/putar/hapus di atas) agar program benar-benar mulai bekerja

#Output Program
<img width="858" height="173" alt="image" src="https://github.com/user-attachments/assets/d4107712-aeba-45de-8c7a-04af3683f26f" />
Baris 1-3 (Berhasil menambahkan...): Ini adalah bukti nyata bahwa perintah yd_music.tambah_lagu(...) yang di tulis berulang kali telah berhasil dieksekusi. Tiga lagu telah masuk ke dalam memori Vector.

Baris 4 ([Love me not, Somebody pleasure, Happiness]): Ini adalah hasil dari perintah yd_music.antrean.display(). 

Baris 5 (sedang memutar: Love me not): Ini adalah respon dari pemanggilan yd_music.putar_sekarang() yang pertama. Karena indeks masih 0, lagu pertama pun diputar.

Baris 6 (sedang memutar: Somebody pleasure): Ini adalah efek dari perintah yd_music.next_lagu(). Penunjuk indeks bergeser ke angka 1, sehingga lagu kedua yang diputar.

Baris 7 (lagu terakhir berhasil dihapus): Ini dari fungsi yd_music.hapus_lagu(). Lagu "Happiness" yang tadinya ada di urutan belakang, kini sudah dibuang dari memori.

Baris 8 (sedang memutar: Somebody pleasure): kembali memanggil yd_music.putar_sekarang(). Karena indeks saat ini menunjuk ke lagu "Somebody pleasure", maka sistem menampilkan lagu tersebut.
