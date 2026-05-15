# Sistem pemutaran lagu berulang dalam playlist musik
# Deskripsi Singkat
Pengelolaan antrean lagu pada  aplikasi pemutar musik merupakan conntoh nyata dimana urutan media audio harus disusun secara terstruktur agar dapat diputar terus-menerus. Ketik pengguna menambahkan berbagai lagu ke dalam sebuah playlist, data berupa deretan audio tersebut membentuk daftar antrean yang mempresentasikan urutan hiburan berupa audio yang siap untuk didengarkan. Pengguna sering kali perlu mendengarkan musik secara terus-menerus tanpa jeda, seperti menginginkan pemutaran kembali secara otomatis setelah daftar urutan putarf mencapai batas akhirnya. Sistem harus mampu memutar lagu pertama kembali secara instan tanpa harus menghentikan aplikasi atau meminta pengguna menekan tombol putar secara manual satu per satu.

Untuk mengatasi masalah tersebut, struktur data dan algoritma yanng sangat tepat untuk diterapkan pada skala pemutaran ini adalah circular queue. ALgoritma ini dipilih karena  memiliki cara kerja  yang sangat efisien dan cerdas dalam menghubungkan ujung akhir daftar putar kembali ke titik awal secara presisi menggunakan operasi matematika sisa bagi. Circular queueu juga beroperasidengan mendaur ulang ruang memori dari lagu yang sudah selesai diputar untuk  diantrekan kembali,sehingga komputasinya sangat cepat,optimal dan fleksibel untuk memproses putaran siklus lagu  tanpa membebani kinerja memori perangkat keras pengguna.
# Source Code
<img width="845" height="393" alt="Screenshot 2026-05-15 161405" src="https://github.com/user-attachments/assets/d714efb7-81f5-447f-9cf3-401096095e01" />
Baris 1: Mendefinisikan sebuah blue print bernama looping playlist

Baris 2:  Mendefinisikan konstrukor yang otommatis berjalan saat objek dibuat, dengan kapasitas playlist maksimal 3 lagu.

Baris 3: Menimpan nilai batas playlist ke  dalam variabel  MAXN

Baris 4: Membuat struktur memori berupa lis yang diisi elemen kosong (None) sebanyak nilai kapasitas maksimal.

Baris 5: Menetapkan posisi penunjuk antrean paling depan di indeks -1 (menandakan antrean masih benar-benar kosong).

Baris 6: Menetapkan posisi penunjuk antrean paling belakang di indeks -1.

Baris 8: Mendefinisikan fungsi untuk mengecek apakah playlist sedang tidak memiliki lagu sama sekali.

Baris 9: Mengembalikan nilai True jika penunjuk depan masih di angka -1 (kosong).

Baris 11: Mendefinisikan fungsi untuk mengecek apakah kapasitas memori playlist sudah habis/penuh.

Baris 12: Ini adalah logika utama antrean melingkar (Circular Queue). Fungsi ini mengecek dengan operator sisa bagi (modulo) apakah posisi setelah elemen paling belakang akan menabrak posisi elemen paling depan.

Baris 14: Mendefinisikan fungsi untuk memasukkan lagu baru, dengan menerima parameter judul lagu.

Baris 15: Melakukan pengecekan, jika memori list penuh.

Baris 16: Jika penuh, maka cetak pesan peringatan bahwa playlist penuh.

Baris 17: Membatalkan dan keluar dari fungsi eksekusi penambahan lagu (karena tidak ada tempat lagi).

Baris 18: Pengecekan kondisi sebaliknya, jika playlist saat ini kosong (ini akan menjadi lagu pertama yang masuk).

Baris 19: Mengatur papan penunjuk depan untuk pindah dari -1 ke indeks 0.

Baris 20: Mengatur papan penunjuk belakang juga di posisi indeks 0.

Baris 21: Kondisi alternatif, jika playlist tidak penuh namun juga tidak kosong (berarti sudah ada lagu lain sebelumnya).

Baris 22: Menggeser posisi penunjuk belakang satu indeks ke depan. Karena melingkar, sisa bagi (modulo) akan membuatnya kembali ke 0 jika indeksnya mencapai batas ujung list.

Baris 23: Memasukkan teks judul lagu ke dalam array playlist tepat di kursi yang ditunjuk oleh indeks belakang terbaru.

Baris 24: Mencetak pesan konfirmasi ke layar bahwa lagu tersebut sukses dimasukkan ke antrean.
<img width="813" height="378" alt="Screenshot 2026-05-15 161428" src="https://github.com/user-attachments/assets/61a0061c-5021-4a42-9370-a9285dbd4034" />
Baris 26: Mendefinisikan fungsi (metode) untuk memanggil dan memutar lagu yang berada di urutan terdepan.

Baris 27: mengecek apakah kondisi penunjuk depan bernilai -1 (antrean kosong)

Baris 28: Mencetak pesan peringatan ke layar bahwa playlist sedang kosong sehingga sistem tidak bisa memutar apa pun.

Baris 29: Menghentikan paksa dan keluar dari fungsi tersebut agar program tidak mengalami eror saat mencoba mengambil lagu yang tidak ada.

Baris 30: Mengambil data judul lagu dari kursi antrean paling depan (yang ditunjuk oleh indeks depan) dan menyimpannya ke dalam variabel sementara bernama lagusekarang.

Baris 31: Menampilkan pesan ke layar bahwa lagu yang tersimpan di variabel tersebut sedang diputar saat ini.

Baris 32: Mengecek apakah posisi penunjuk depan dan belakang menunjuk ke indeks yang persis sama. Jika ya, berarti lagu yang baru saja diputar adalah satu-satunya lagu di dalam playlist.

Baris 33: Mereset/mengembalikan papan penunjuk depan ke angka -1 (kosong).

Baris 34: Mereset/mengembalikan papan penunjuk belakang juga ke angka -1.

Baris 35: Kondisi alternatif yang dijalankan jika antrean memiliki lebih dari satu lagu.

Baris 36: Menggeser papan penunjuk depan ke kursi sebelahnya secara melingkar menggunakan sisa bagi (modulo). Ini secara logis mengeluarkan lagu yang sudah diputar tadi dari antrean depan (Dequeue).

Baris 37: Menggunakan fungsi penambahan lagu yang ada di dalam kelas ini (self.TambahLagu) untuk memasukkan kembali lagu yang baru diputar tadi ke posisi antrean paling belakang. Di sinilah efek looping playlist terjadi!

Baris 41: Mendefinisikan blok fungsi utama (main) yang bertugas sebagai antarmuka program untuk pengguna.

Baris 42: Mencetak objek/sistem antrean baru ke dalam memori komputer berdasarkan cetak biru kelas LoopingPlaylist yang sudah kita rancang sebelumnya.

Baris 43: Menyiapkan variabel bantu dengan nilai awal 0 untuk menyimpan input angka yang akan diketik oleh pengguna.

Baris 44: Memulai sebuah siklus perulangan yang akan terus-menerus menampilkan menu utama selama pengguna belum menginput angka 3.

Baris 45: Mencetak garis pemisah dan judul menu ke layar.

Baris 46: Menampilkan teks pilihan opsi nomor 1 (Tambah Lagu).

Baris 47: Menampilkan teks pilihan opsi nomor 2 (Putar Lagu berikutnya).

Baris 48: Menampilkan teks pilihan opsi nomor 3 (Keluar).
<img width="794" height="423" alt="Screenshot 2026-05-15 161523" src="https://github.com/user-attachments/assets/0702c622-db87-4b39-9558-134fab7798d6" />
Baris 49: Memulai blok pengujian eksekusi (try) untuk mendeteksi dan mencegah program berhenti mendadak jika terjadi eror akibat input pengguna yang salah.

Baris 50: Meminta pengguna mengetikkan angka pilihan menu, mengubah format ketikannya menjadi bilangan bulat (integer), dan menyimpannya ke dalam variabel pilih.

Baris 51: Menangkap eror spesifik (ValueError) yang terjadi jika pengguna memasukkan karakter selain angka (misalnya huruf atau tanda baca).

Baris 52: Mencetak pesan peringatan ke layar bahwa input yang dimasukkan salah.

Baris 53: Memberi instruksi untuk melewati semua sisa kode di bawahnya dan langsung melompat kembali ke putaran awal looping while (sehingga menu ditampilkan ulang).

Baris 54: Mengecek kondisi apakah angka yang berhasil dimasukkan pengguna adalah angka 1.

Baris 55: Meminta pengguna mengetikkan teks judul lagu, kemudian menyimpan teks tersebut ke dalam variabel val.

Baris 56: Memanggil fungsi penambahan lagu pada sistem playlist dengan membawa data judul lagu yang baru saja diketik.

Baris 57: Mengecek kondisi alternatif, apakah pengguna mengetikkan angka 2.

Baris 58: Memanggil fungsi untuk memutar lagu terdepan dan otomatis memasukkannya kembali ke antrean paling belakang.

Baris 59: Mengecek kondisi alternatif terakhir, apakah pengguna mengetikkan angka 3.

Baris 60: Mencetak pesan perpisahan bahwa program selesai. (Siklus while akan otomatis berhenti setelah ini karena nilai variabel pilih sudah menjadi 3).

Baris 61: Menangkap semua kemungkinan input angka lainnya yang tidak relevan (misalnya pengguna mengetik angka 4, 5, atau 0).

Baris 62: Mencetak pesan peringatan bahwa pilihan menu tersebut tidak tersedia.

Baris 65: Ini adalah baris standar bawaan Python untuk mengecek apakah file script ini sedang dijalankan secara langsung oleh pengguna (bukan sedang diimpor ke dalam file Python yang lain).

Baris 66: Memicu atau menyalakan fungsi main() untuk pertama kalinya agar seluruh program antarmuka antrean lagu ini mulai bekerja.

# Output Code
<img width="782" height="362" alt="Screenshot 2026-05-15 162116" src="https://github.com/user-attachments/assets/34c7d940-4354-4267-887a-56f24225e239" />

## Putaran Pertama (Memasukkan Lagu Pertama)
=== Playlist Lagu === : Menampilkan judul header menu utama program.

1. Tambah Lagu : Menampilkan pilihan opsi nomor 1.

2. Putar Lagu berikutnya : Menampilkan pilihan opsi nomor 2.

3. Keluar : Menampilkan pilihan opsi nomor 3.

Pilih: 1 : Pengguna mengetik angka 1 untuk memilih menu penambahan lagu.

Nama lagu: Shape Of My Heart : Sistem meminta teks, dan pengguna mengetikkan judul lagu pertama.

Lagu Shape Of My Heart berhasil ditambahkan : Sistem mengonfirmasi bahwa lagu tersebut sukses dimasukkan ke dalam ruang antrean (indeks 0).
## Putaran Kedua (Memasukkan Lagu Kedua)
=== Playlist Lagu === : Menampilkan kembali judul menu karena program berada di dalam perulangan (while).

1. Tambah Lagu : Menampilkan kembali opsi menu 1.

2. Putar Lagu berikutnya : Menampilkan kembali opsi menu 2.

3. Keluar : Menampilkan kembali opsi menu 3.

Pilih: 1 : Pengguna mengetik angka 1 lagi untuk menambah lagu baru.

Nama lagu: About You : Pengguna mengetikkan judul lagu kedua.

Lagu About You berhasil ditambahkan : Sistem mengonfirmasi bahwa lagu kedua sukses menempati kursi antrean selanjutnya (indeks 1).

## Putaran Ketiga (Memasukkan Lagu Ketiga)
=== Playlist Lagu === : Menampilkan ulang header menu utama.

1. Tambah Lagu : Menampilkan opsi menu 1.

2. Putar Lagu berikutnya : Menampilkan opsi menu 2.

3. Keluar : Menampilkan opsi menu 3.

Pilih: 1 : Pengguna mengetik angka 1 untuk menambah lagu ketiga.

Nama lagu: Blue : Pengguna mengetikkan judul lagu ketiga.

Lagu Blue berhasil ditambahkan : Sistem mengonfirmasi bahwa lagu ketiga telah dimasukkan (indeks 2).
<img width="823" height="377" alt="Screenshot 2026-05-15 162129" src="https://github.com/user-attachments/assets/efe86cd4-30d4-4e04-b731-df878344cd62" />
## Putaran Keempat (Memutar Lagu Pertama)
=== Playlist Lagu === : Menampilkan ulang judul header menu utama.

1. Tambah Lagu : Menampilkan pilihan opsi nomor 1.

2. Putar Lagu berikutnya : Menampilkan pilihan opsi nomor 2.

3. Keluar : Menampilkan pilihan opsi nomor 3.

Pilih: 2 : Pengguna mengetik angka 2 untuk mengeksekusi pemutaran lagu.

sedang memutar: Shape Of My Heart : Sistem mengambil (melakukan Dequeue) lagu yang berada di antrean paling depan (indeks 0).

Lagu Shape Of My Heart berhasil ditambahkan : Sesuai dengan algoritma looping yang sudah kita buat, lagu yang baru saja diputar tersebut otomatis langsung dimasukkan kembali (di-Enqueue) ke posisi antrean paling belakang!

## Putaran Kelima (Memutar Lagu Kedua)
=== Playlist Lagu === : Menampilkan kembali judul menu.

1. Tambah Lagu : Menampilkan opsi menu 1.

2. Putar Lagu berikutnya : Menampilkan opsi menu 2.

3. Keluar : Menampilkan opsi menu 3.

Pilih: 2 : Pengguna mengetik angka 2 lagi untuk memutar lagu selanjutnya.

sedang memutar: About You : Sistem memanggil lagu kedua yang kini telah bergeser menjadi urutan terdepan di antrean.

Lagu About You berhasil ditambahkan : Lagu tersebut juga otomatis dimasukkan kembali ke antrean bagian belakang setelah dipanggil.

## Putaran Keenam (Memutar Lagu Ketiga)
=== Playlist Lagu === : Menampilkan ulang header menu utama.

1. Tambah Lagu : Menampilkan opsi menu 1.

2. Putar Lagu berikutnya : Menampilkan opsi menu 2.

3. Keluar : Menampilkan opsi menu 3.

Pilih: 2 : Pengguna kembali mengetik angka 2.

sedang memutar: Blue : Sistem memanggil lagu ketiga ("Blue") yang kini mendapat giliran berada di urutan terdepan.

Lagu Blue berhasil ditambahkan : Lagu "Blue" kembali dipindahkan ke akhir antrean.
### catatan:
Berkat algoritma ini, meskipun kapasitas antrean hanya 3 dan kita sudah memutar 3 lagu, antreannya tidak menjadi kosong. Pada putaran berikutnya, lagu "Shape Of My Heart" sudah kembali berada di antrean terdepan dan siap untuk diputar ulang dari awal 
<img width="775" height="228" alt="Screenshot 2026-05-15 162153" src="https://github.com/user-attachments/assets/f0436cf4-942c-47ad-ae38-c6a0b90796ae" />
## Putaran Ketujuh (Membuktikan Looping Playlist)
=== Playlist Lagu === : Menampilkan ulang judul header menu utama.

1. Tambah Lagu : Menampilkan pilihan opsi nomor 1.

2. Putar Lagu berikutnya : Menampilkan pilihan opsi nomor 2.

3. Keluar : Menampilkan pilihan opsi nomor 3.

Pilih: 2 : Pengguna kembali mengetik angka 2 untuk memutar lagu.

sedang memutar: Shape Of My Heart : Setelah lagu ketiga ("Blue") diputar sebelumnya, sistem sekarang memutar kembali lagu pertama ("Shape Of My Heart"). Ini membuktikan bahwa penunjuk antrean berhasil berputar (looping) kembali ke awal menggunakan rumus modulo.

Lagu Shape Of My Heart berhasil ditambahkan : Lagu pertama tersebut kembali dipindahkan ke akhir antrean untuk menjaga siklus tetap berjalan tanpa batas.

## Putaran Kedelapan (Mengakhiri Program)
=== Playlist Lagu === : Menampilkan kembali judul menu untuk kesekian kalinya.

1. Tambah Lagu : Menampilkan opsi menu 1.

2. Putar Lagu berikutnya : Menampilkan opsi menu 2.

3. Keluar : Menampilkan opsi menu 3.

Pilih: 3 : Pengguna mengetik angka 3, yang merupakan instruksi untuk menghentikan perulangan (sesuai dengan kondisi while pilih != 3: pada kode Anda).

Program selesai. : Sistem mencetak pesan penutup. Siklus while resmi berhenti, memori dibebaskan, dan eksekusi program Python berakhir sepenuhnya di titik ini.

# Link Youtube
