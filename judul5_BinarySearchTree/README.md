# Pengelolaan Jadwal Kelas Mata Kuliah
# Deskripsi Singkat
Pengelolaan jadwal kelas mata kuliah pada sistem akademik merupakan contoh nyata di mana rentang waktu harus disusun secara terstruktur agar dapat berjalan tanpa adanya tabrakan mata kuliah. Ketika pihak kampus menambahkan berbagai mata kuliah ke dalam sebuah ruangan, data berupa alokasi waktu tersebut membentuk daftar kalender yang merepresentasikan urutan agenda yang siap untuk dilaksanakan. Pengelola sering kali perlu memastikan rangkaian perkuliahan berjalan tertib, seperti menghindari dimulainya kelas baru sebelum kelas sebelumnya benar-benar selesai. Sistem harus mampu memvalidasi celah waktu dan mendeteksi potensi tabrakan secara instan, tanpa harus menghentikan aplikasi atau meminta pengguna menelusuri daftar jadwal secara manual satu per satu.

# Output Code
Untuk mengatasi masalah tersebut, struktur data dan algoritma yang sangat tepat untuk diterapkan pada skala penjadwalan ini adalah Binary Search Tree (BST) Lanjutan. Algoritma ini dipilih karena memiliki cara kerja yang sangat efisien dan cerdas dalam memvalidasi ketersediaan waktu menggunakan operasi pencarian batas rentang melalui fitur Predecessor (jadwal tepat sebelumnya) dan Successor (jadwal tepat setelahnya). BST Lanjutan juga beroperasi dengan mengurutkan titik waktu secara logis ke dalam cabang-cabang pohon pencarian, sehingga proses komputasinya sangat cepat, optimal, dan fleksibel untuk memproses penyisipan ribuan jadwal perkuliahan tanpa membebani kinerja sistem basis data kampus.
<img width="845" height="395" alt="Screenshot 2026-05-24 091259" src="https://github.com/user-attachments/assets/e2fdac84-a063-42cc-b394-c309a5e127d7" />
Baris 1 (Mendefinisikan class NodeKelas sebagai cetak biru untuk simpul dalam BST)

Baris 2 (Mendefinisikan konstruktor __init__ untuk inisialisasi parameter saat objek node dibuat)

Baris 3 (Menyimpan argumen mulai ke dalam atribut objek sebagai kunci/key pencarian node)

Baris 4 (Menyimpan argumen selesai ke dalam atribut objek)

Baris 5 (Menyimpan argumen kelas (nama mata kuliah) ke dalam atribut objek)

Baris 6 (Menginisialisasi pointer self.left (cabang anak kiri) dengan nilai kosong None)

Baris 7 (Menginisialisasi pointer self.right (cabang anak kanan) dengan nilai kosong None)

Baris 10 (Mendefinisikan class KalenderBST yang berisi logika utama struktur data pohon)

Baris 11 (Mendefinisikan konstruktor __init__ untuk inisialisasi struktur pohon)

Baris 12 (Menetapkan akar utama pohon (self.root) dengan nilai None sebagai tanda pohon masih kosong)

Baris 14 (Mendefinisikan fungsi insert_node untuk menyisipkan jadwal node baru secara rekursif)

Baris 15 (Mengecek kondisi apakah posisi node saat penelusuran saat ini kosong)

Baris 16 (Jika kosong, kembalikan objek NodeKelas baru sebagai node daun di titik tersebut)

Baris 17 (Mengecek apakah target waktu mulai lebih kecil dari waktu mulai node saat ini)

Baris 18 (Memanggil fungsi rekursif untuk masuk menelusuri ke cabang anak kiri)

Baris 19 (Mengecek apakah target waktu mulai lebih besar dari waktu mulai node saat ini)

Baris 20 (Memanggil fungsi rekursif untuk masuk menelusuri ke cabang anak kanan)

Baris 21 (Mengembalikan referensi node saat ini untuk merakit dan menjaga rantai silsilah pohon)

Baris 23 (Mendefinisikan fungsi delete_node untuk menghapus node berdasarkan waktu mulai)

Baris 24 (Mengecek jika penelusuran mentok pada node kosong/data jadwal tidak ditemukan di pohon)

Baris 25 (Mengembalikan root dan bendera status False jika jadwal gagal ditemukan)

<img width="833" height="375" alt="Screenshot 2026-05-24 091317" src="https://github.com/user-attachments/assets/c302d205-90d4-4e16-a494-a1b22103236e" />
Baris 27 (Menginisialisasi variabel found dengan nilai bawaan False untuk status pencarian)

Baris 28 (Mengecek jika kunci jadwal target lebih kecil dari nilai node saat ini)

Baris 29 (Memanggil rekursi untuk menelusuri cabang kiri dan memperbarui statusnya)

Baris 30 (Mengecek jika kunci jadwal target lebih besar dari nilai node saat ini)

Baris 31 (Memanggil rekursi untuk menelusuri cabang kanan dan memperbarui statusnya)

Baris 32 (Blok else yang artinya nilai jadwal yang dicari berhasil ditemukan pada node ini)

Baris 33 (Mengubah nilai status penanda pencarian found menjadi True)

Baris 34 (Mengecek Kasus 1: Node yang akan dihapus tidak memiliki cabang anak sama sekali (daun))

Baris 35 (Menghancurkan node daun dengan mengembalikan None ke asal induk pemanggilnya)

Baris 36 (Mengecek Kasus 2: Node yang akan dihapus tidak memiliki cabang kiri (hanya punya cabang kanan))

Baris 37 (Mengembalikan cabang kanannya untuk menggantikan posisinya beserta nilai kembalian status found)

Baris 38 (Mengecek Kasus 2 lainnya: Node yang dihapus tidak memiliki cabang kanan (hanya punya cabang kiri))

Baris 39 (Mengembalikan cabang kirinya untuk menggantikan posisinya beserta status found)

Baris 40 (Blok eksekusi Kasus 3: Terjadi saat node memiliki struktur utuh 2 anak)

Baris 41 (Mencari successor yaitu nilai terkecil di percabangan kanan dengan memanggil find_min_node)

Baris 42 (Menimpa nilai waktu mulai node yang akan dihapus dengan nilai waktu mulai successor)

Baris 43 (Menimpa nilai waktu selesai node dengan nilai waktu successor)

Baris 44 (Menimpa nilai data kelas node dengan nilai kelas dari successor)

Baris 45 (Menghapus node successor yang lama di cabang kanan menggunakan pemanggilan delete_node rekursif)

Baris 46 (Mengembalikan root saat ini yang sudah selesai dimodifikasi penghapusan ke node induknya)

Baris 48 (Mendefinisikan fungsi batalkan_jadwal sebagai wrapper atau jembatan untuk operasi penghapusan menu)

Baris 49 (Menjalankan fungsi eksekusi internal delete_node dari akar lalu menyalin hasil statusnya ke variabel found)

Baris 50 (Mengembalikan status eksekusi boolean found tersebut ke pemanggilnya/menu luar)

<img width="836" height="415" alt="Screenshot 2026-05-24 091333" src="https://github.com/user-attachments/assets/b7aa7c53-b6ec-4061-bf94-feb8a4d6632b" />
Baris 52 (Mendefinisikan fungsi internal find_min_node untuk mencari nilai terkecil dari pohon rujukan)

Baris 53 (Menetapkan variabel current mulai dari posisi node paramater target rujukan)

Baris 54 (Memulai perulangan jalan telusur selama posisi saat ini dan cabang kirinya berwujud/tidak kosong)

Baris 55 (Berpindah iterasi terus-menerus mengikuti node anak kiri)

Baris 56 (Jika perulangan selesai, mengembalikan posisi current paling ujung kiri yakni data terkecilnya)

Baris 58 (Mendefinisikan fungsi find_successor untuk mencari jadwal yang terletak langsung persis setelahnya)

Baris 59 (Menetapkan iterasi pencarian dari node paling akar kalender (self.root))

Baris 60 (Menginisialisasi variabel status dan nilai successor dengan kosong/None)

Baris 61 (Memulai loop penelusuran node selagi posisi node belum mentok)

Baris 62 (Jika batas parameter target waktu lebih kecil daripada posisi saat ini)

Baris 63 (Jadikan node ini sebagai kandidat cadangan jadwal setelahnya (successor))

Baris 64 (Bergerak ke sisi kiri demi mencari nilai yang letaknya lebih mendempet ke target waktu)

Baris 65 (Jika parameter waktu ternyata lebih besar sama dengan titik current)

Baris 66 (Bergerak mencari ke cabang sisi kanan)

Baris 67 (Mengembalikan titik node kandidat optimal successor ke sistem)

Baris 69 (Mendefinisikan fungsi find_predecessor untuk mencari jadwal yang terletak langsung persis sebelumnya)

Baris 70 (Menetapkan penelusuran berawal dari posisi pucuk pohon self.root)

Baris 71 (Menginisialisasi default predecessor menjadi objek None)

Baris 72 (Melakukan siklus while penyusuran selagi belum tiba di titik None)

Baris 73 (Jika input waktu dari pengguna lebih besar daripada nilai mulai node ini)

Baris 74 (Jadikan current sebagai kandidat pendahulu sementaranya (predecessor))

Baris 75 (Pindah iterasi ke arah cabang sisi kanan)

Baris 76 (Jika input waktu dari pengguna lebih kecil sama dengan iterasi node saat ini)

Baris 77 (Pindah menyusuri turun ke cabang sebelah kiri)

Baris 78 (Bila usai, mengembalikan titik letak predecessor ke sistem jadwal)

<img width="840" height="440" alt="Screenshot 2026-05-24 091449" src="https://github.com/user-attachments/assets/1471c2a4-ade2-4ceb-94ea-946df60bb1e1" />

Baris 80 (Mendefinisikan fungsi cek_dan_tambah_jadwal untuk menyaring dan mendaftarkan jadwal bebas tabrakan waktu)

Baris 81 (Memanggil fitur find_predecessor untuk mengetahui eksistensi sesi kegiatan kelas sebelumnya)

Baris 82 (Mengevaluasi apabila pencarian mengonfirmasi ada kelas sebelumnya/tidak kosong)

Baris 83 (Logika filterasi: Jika jadwal Predecessor tersebut belum tuntas alias jam selesainya melampaui jam mulai jadwal baru)

Baris 84 (Memunculkan peringatan teks tabrakan (overlap) bersama jam kelas sebelumnya ke konsol)

Baris 85 (Mengembalikan flag instruksi False guna membatalkan pendaftaran)

Baris 87 (Memanggil pelacak find_successor untuk menganalisis sesi jadwal sesudahnya)

Baris 88 (Mengevaluasi apakah pelacakan penerus terkonfirmasi menjumpai jadwal)

Baris 89 (Logika filterasi: Jika target waktu selesai aktivitas ini bablas melampaui waktu mulai agenda Successor)

Baris 90 (Mencetak peringatan ekses rentang durasi yang membentur jadwal penerusnya)

Baris 91 (Mengembalikan kegagalan proses lewat status False)

Baris 93 (Kondisi saat validasi berlalu mulus, panggil insert_node agar menyimpan datanya ke dalam pohon)

Baris 94 (Memunculkan notifikasi kelas telah berstatus disahkan ke layar)

Baris 95 (Mengembalikan sinyal positif True penyisipan berhasil)

Baris 97 (Mendefinisikan operasi struktur cetak_jadwal menerapkan teknik penelusuran rekursif In-Order Traversal)

Baris 98 (Syarat penghenti rekursi bilamana iterasi jatuh pada posisi fiktif/kosong)

Baris 99 (Mendorong pemanggilan berulang menyelami sub-pohon sayap kiri (waktu pagi))

Baris 100 (Merender keluaran visual jadwal berisi nilai mulai, selesai, dan ruang dengan minimum isian nol (04d))

Baris 101 (Mendorong pemanggilan berulang merambat pada sub-pohon sayap kanan (waktu sore))

Baris 103 (Mendefinisikan pembungkus CLI tampilkan_semua demi menampilkan jadwal secara total)

Baris 104 (Mencetak baris batas pemanis header tampilan jadwal)

Baris 105 (Mendeteksi jikalau kondisi database internal di self.root amat kosong melompong)

Baris 106 (Memunculkan indikator status bawaan jika sesi kosong tak ada kelas)

Baris 107 (Jika pohon telah ditanami simpul aktivitas, lakukan perintah bawahnya)

Baris 108 (Perintahkan rendering node pohon mendelegasikan tugas ke iterasi cetak_jadwal)

<img width="840" height="440" alt="Screenshot 2026-05-24 091449" src="https://github.com/user-attachments/assets/c4d1079e-86b4-4f78-9a1c-2bf720e5a0b7" />

Baris 110 (Mendefinisikan metode gerbang eksekusi Interface Command Line bernama main)

Baris 111 (Mencetak instansiasi objek operasional dari kelas induk kalendernya)

Baris 112 (Deklarasi nilai awal peubah pilih yang ditugaskan mengatur laju daur ulang menu)

Baris 113 (Pembangunan instruksi while loop yang merotasi terus layar menu jikalau user menolak menginput 5)

Baris 114 (Memunculkan judul antar muka sistem di console)

Baris 115 (Menyajikan item list perintah nomor satu di menu layar konsol)

Baris 116 (Menyajikan item list perintah nomor dua pembatalan kelas)

Baris 117 (Menyajikan item list perintah inkuiri jadwal untuk list nomor tiga)

Baris 118 (Menyajikan item list pengecekan tetangga selang waktu di nomor empat)

Baris 119 (Menyajikan fungsi pintu keluar program menu lima)

Baris 121 (Menyematkan kurungan mitigasi eksepsi inputan try saat mengonversi perintah)

Baris 122 (Menampung respons konversi basis 10 berupa integer nomor menu pilihan pemakai piranti)

Baris 123 (Blok pencegat kesalahan ValueError manakala tipe bukan susunan angka valid masuk ketikan)

Baris 124 (Memunculkan teks informasi bahwa ketikan wajib sebuah angka riil)

Baris 125 (Memaksa while melompat mengabaikan baris sisanya agar mulai kembali di titik awal)

Baris 127 (Pengujian kondisi percabangan jika entri penunjuk bernilai sama persis satu)

Baris 128 (Kurungan pengaman masukan error handling parameter jam registrasi baru kelas)

Baris 129 (Petunjuk penggunaan bentuk struktur waktu per 24 jam)

Baris 130 (Menerima konversi teks masuk parameter waktu permulaan sebagai Integer)

Baris 131 (Menerima konversi perintah teks batas durasi parameter berwujud nilai Integer)

Baris 132 (Evaluasi rasionalisasi jadwal manakala ujung selesainya malah bertolak lebih awal ketimbang waktu start)

Baris 133 (Memberitahukan kekeliruan rasional batas tempo kalender tersebut)

Baris 134 (Mengembalikan ritme skrip ke posisi kepala while menu)

Baris 135 (Menerima input penampung data String penamaan nama kelas mata kuliah yang dipesan)

Baris 136 (Mengoper sekumpulan parameter di atas ke fungsi pengendali kerangka cek_dan_tambah_jadwal)

Baris 137 (Aksi reaksi manakala pengisian input terganggu interupsi abjad yang membatalkan int())

Baris 138 (Cetak output kegagalan verifikasi parsing format integer menu satu)

<img width="841" height="428" alt="Screenshot 2026-05-24 091631" src="https://github.com/user-attachments/assets/6549709a-4d55-4beb-b7fb-cf0ea646ce87" />

Baris 140 (Pengujian aliran jikalau parameter variabel di isian menu berbunyi numerik angka dua)

Baris 141 (Konstruksi mitigasi parameter hapus agar lepas dari crash type variable)

Baris 142 (Pemunculan arahan panduan membatalkan mata kuliah)

Baris 143 (Parsing tangkapan konversi durasi waktu jam kelas yang diincar pembatalannya)

Baris 144 (Menyerahkan tanggung jawab memicu fungsi internal pembatalan kalender sekaligus melacak status balikannya)

Baris 145 (Kondisi saat fungsi memulangkan hasil konfirmasi penelusuran valid (True))

Baris 146 (Cetak validasi perolehan sukses dengan menampakkan modifikasi nol per jam yang dihapus)

Baris 147 (Kondisi berlawanan dimana rutinitas pengapusan gagal mencocokkan hasil)

Baris 148 (Penegasan pemberitahuan data jadwal terlampau absen/fiktif)

Baris 149 (Klausa jebakan pencegahan error yang sama saat diinput string kosong/abjad pada opsi hapus)

Baris 150 (Keterangan bahwa yang diinput menyalahi kaidah ValueError)

Baris 152 (Kondisi verifikasi opsi tatkala user menekan instruksi angka tiga)

Baris 153 (Memerintahkan metode perangkaian cetak kalender di hadapan pengguna visual)

Baris 155 (Pengujian aliran saat permintaan nomor menginjak rute nomor empat pencarian komparatif)

Baris 156 (Tameng sistem try supaya variabel integer jam tak dihancurkan teks aneh)

Baris 157 (Input konversi parameter dasar integer komparasi pengintaian celah renggang)

Baris 158 (Meneruskan operasi pemeriksaan nilai tetangga ke arah fungsi komparator sebelumnya)

Baris 159 (Meneruskan operasi penemu nilai pengganti terdekat yang mengekor pasca target tersebut)

Baris 161 (Mencetak pelengkap bingkai teks komparasi lengkap dengan indikasi angka target rujukan)

Baris 162 (Validasi pengadaan nilai komparatif riwayat kelas sebelumnya)

Baris 163 (Mencetak laporan sesi pra-target. (Catatan: Bug di sini, karena parameter propertinya memanggil .agenda padahal deklarasi variabel awal memakai self.kelas))

Baris 164 (Situasi cabang di mana penjelajahan pra-target mentok mendapati None)

Baris 165 (Memublikasikan simpulan bahwasanya belum ada eksistensi kelas terdahulu)

<img width="846" height="247" alt="Screenshot 2026-05-24 091646" src="https://github.com/user-attachments/assets/175db389-5bff-4c01-99df-d4bc0b4403d0" />

Baris 167 (Validasi pengadaan parameter sub-objek pasca-target/pengganti selanjutnya)

Baris 168 (Mencetak detil spesifik identitas sesi pasca-target. (Catatan: Bug .agenda yang sama juga ada pada baris kode baris ini))

Baris 169 (Situasi percabangan hampa node sesudahnya)

Baris 170 (Mencetak rekap nihil dari kegiatan penggantinya pasca acuan)

Baris 171 (Bagian pertahanan blokade ketikan aksara di fitur komparator)

Baris 172 (Terbit info peringatan ValueError khusus menu komparasi interval keempat ini)

Baris 174 (Validasi menu pamungkas penghentian siklus aplikasi nomor lima)

Baris 175 (Kalimat pelepasan/akhir yang terbit memecah jeda while utama sebelum terputus permanen)

Baris 176 (Jaring blokade menu buangan di saat pilih bukan berkisar 1 sampai dengan 5)

Baris 177 (Menegaskan perlakuan invalid/non-menu)

Baris 180 (Sintaks proteksi bawaan bahasa pemrograman Python jika modul utama file dieksekusi independen)

Baris 181 (Memanggil fungsi main)

# output code
<img width="726" height="384" alt="Screenshot 2026-05-24 145444" src="https://github.com/user-attachments/assets/d380ef8d-1bdd-4d35-a65e-4edafd08216c" />
<img width="720" height="387" alt="Screenshot 2026-05-24 145523" src="https://github.com/user-attachments/assets/b5c264b8-44d5-429a-b4cc-20a4175675cb" />
<img width="716" height="387" alt="Screenshot 2026-05-24 145614" src="https://github.com/user-attachments/assets/1d4d0791-445e-46de-8725-7c48cea9118c" />
<img width="696" height="386" alt="Screenshot 2026-05-24 145809" src="https://github.com/user-attachments/assets/e862a980-8b3c-4011-8e0a-986802765721" />
<img width="706" height="377" alt="Screenshot 2026-05-24 145836" src="https://github.com/user-attachments/assets/8532db43-3c23-4c37-9dcc-ffcaa174cdbd" />


Iterasi 1: Tambah Jadwal Awal & Tampilkan

input : Menu 1 (0900-1030 Aljabar Matriks), Menu 1 (1300-1500 RPL), lalu Menu 3.

output : Pesan BERHASIL muncul dua kali. Saat Menu 3 dipanggil, daftar jadwal tercetak rapi secara berurutan.

Iterasi 2: Pencegahan Jadwal Bentrok (Tabrakan)

input : Menu 1 (1000-1100 PKn), lalu Menu 1 (1230-1330 Agama Islam).

output : Sistem menolak dan mencetak peringatan GAGAL: Tabrakan... karena mendeteksi waktu kelas yang tumpang-tindih dengan jadwal yang sudah ada.

Iterasi 3: Pencarian Celah Kosong & Penambahan Valid

input : Menu 4 (cek jam 1130), lalu Menu 1 (1100-1200 Pengling).

output : Menampilkan indikator rapat sebelum dan sesudahnya, lalu mencetak pesan BERHASIL karena jadwal 'Pengling' berada di waktu yang benar-benar kosong.

Iterasi 4: Pembatalan Jadwal

input : Menu 2 (hapus jam 0800 ), Menu 2 (hapus jam 1100 Pengling), lalu ditutup dengan Menu 3.

output : Muncul penolakan Jadwal tidak ditemukan! untuk jam 0800, lalu pesan Jadwal... berhasil dibatalkan untuk jam 1100. Menu 3 menunjukkan daftar jadwal kembali utuh menyisakan dua kelas awal.



