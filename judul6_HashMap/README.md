# Pencarian produk e-commerce berbasis SKU

# Deskripsi Singkat
Pencarian produk pada platform e-commerce berskala besar merupakan contoh nyata di mana jutaan barang harus dikelola secara terstruktur agar dapat ditemukan dengan sangat cepat tanpa adanya penundaan. Ketika pihak penjual menambahkan berbagai macam barang ke dalam sistem inventaris digital, data berupa kode Stock Keeping Unit (SKU) tersebut membentuk sebuah katalog raksasa yang merepresentasikan identitas unik setiap produk yang siap untuk ditransaksikan. Sistem sering kali perlu merespons kueri pencarian secara instan, seperti menampilkan harga, sisa stok, dan lokasi rak barang sesaat setelah kode SKU diketik atau dipindai (scan). Sistem harus mampu mencocokkan kode ini dan menangani potensi tabrakan indeks memori (collision) secara langsung, tanpa harus menghentikan aplikasi atau meminta mesin menelusuri daftar jutaan produk secara manual satu per satu. 

Untuk mengatasi masalah tersebut, struktur data dan algoritma yang sangat tepat untuk diterapkan pada skala pencarian ini adalah Hash Map dengan metode Separate Chaining. Algoritma ini dipilih karena memiliki cara kerja yang sangat efisien dan cerdas dalam menemukan lokasi barang menggunakan operasi penerjemahan key alfanumerik (SKU) menjadi alamat indeks langsung melalui fungsi hash. Hash Map Separate Chaining juga beroperasi dengan mengelompokkan data yang memiliki indeks identik secara logis ke dalam rantai linked list di setiap bucket-nya, sehingga proses komputasinya sangat cepat (O(1)), optimal, dan fleksibel untuk memproses pencarian maupun penyisipan jutaan produk baru tanpa membebani kinerja peladen (server) utama e-commerce.
#Source Code
<img width="840" height="423" alt="Screenshot 2026-06-09 225733" src="https://github.com/user-attachments/assets/ce85b196-e711-4cdb-a2fd-d38f2321d594" />
Baris 1: class Node: — Membuat cetakan (blueprint) untuk menyimpan data satu produk.

Baris 2: def __init__(self, sku, name): — Fungsi awal yang otomatis berjalan saat produk baru dibuat.

Baris 3: self.sku = sku — Menyimpan kode unik produk (SKU).

Baris 4: self.name = name — Menyimpan nama produk.

Baris 5: self.next = None — Menyiapkan sambungan untuk produk selanjutnya (awalnya kosong).

Baris 7: class SimpleHashMap: — Membuat sistem kerangka utama tabel hash.

Baris 8: def __init__(self, size=5): — Pengaturan awal sistem, menentukan jumlah rak memori (bawaannya 5).

Baris 9: self.size = size — Menyimpan jumlah rak ke dalam sistem.

Baris 10: self.table = [None] * size — Membuat jejeran rak-rak kosong sebanyak yang ditentukan.

Baris 12: def hash_func(self, sku): — Fungsi penentu produk akan ditaruh di rak nomor berapa.

Baris 13: return sum(ord(c) for c in str(sku)) % self.size — Rumus mengubah huruf SKU jadi angka nilai ASCII, dijumlahkan, lalu dibagi sisa (modulo) jumlah rak agar dapat indeks pas.

Baris 15: def insert(self, sku, name): — Fungsi untuk memasukkan produk ke dalam rak.

Baris 16: index = self.hash_func(sku) — Menghitung SKU ini harus masuk ke rak nomor berapa.

Baris 17: current = self.table[index] — Mengecek posisi data paling depan di rak tersebut.

Baris 19: while current: — Mengulang penelusuran jika rak sudah ada isinya.

Baris 20: if current.sku == sku: — Mengecek apakah SKU yang dimasukkan ternyata sudah ada di rak.

Baris 21: current.name = name — Jika ada, cukup perbarui namanya dengan yang baru.

Baris 22: return — Proses selesai, langsung keluar dari fungsi.

Baris 23: current = current.next — Lanjut cek produk di belakangnya jika SKU belum cocok.

Baris 25: new_node = Node(sku, name) — Jika dicek sampai habis SKU tidak ada, buat data produk baru.

Baris 26: new_node.next = self.table[index] — Sambungkan produk baru ke produk lama yang ada di rak itu.

Baris 27: self.table[index] = new_node — Taruh produk baru ini di posisi paling depan rak.
<img width="817" height="402" alt="Screenshot 2026-06-09 225758" src="https://github.com/user-attachments/assets/df27ca04-40c7-42f3-af40-9245b433137c" />
Baris 29: def search(self, sku): — Fungsi untuk mencari nama produk menggunakan SKU-nya.

Baris 30: index = self.hash_func(sku) — Hitung lagi produk ini seharusnya ada di rak nomor berapa.

Baris 31: current = self.table[index] — Datangi rak tersebut dan lihat barang paling depan.

Baris 33: while current: — Telusuri semua barang di dalam rak satu per satu.

Baris 34: if current.sku == sku: — Mengecek apakah SKU barang cocok dengan yang dicari.

Baris 35: return current.name — Jika cocok, berikan nama barangnya dan hentikan pencarian.

Baris 36: current = current.next — Jika belum cocok, cek barang selanjutnya di antrean rak.

Baris 37: return None — Jika rak sudah ditelusuri sampai habis tapi tidak ketemu, laporkan kosong.

Baris 39: def display(self): — Fungsi untuk mencetak isi sistem ke layar.

Baris 40: for i in range(self.size): — Mengurutkan dari rak nomor 0 sampai rak terakhir.

Baris 41: print(f"Rak [{i}]", end="") — Mencetak tulisan nama rak (contoh: "Rak [0]").

Baris 42: curr = self.table[i] — Mengambil isi dari rak tersebut.

Baris 43: while curr: — Selama ada isinya, lakukan pencetakan berulang.

Baris 44: print(f" -> [{curr.sku}: {curr.name}]", end="") — Cetak nama produk lengkap dengan tanda panah.

Baris 45: curr = curr.next — Bergeser ke produk selanjutnya di rak yang sama.

Baris 46: print(" -> NULL") — Jika isi rak habis, cetak "NULL" sebagai penutup barisan.

Baris 48: if __name__ == "__main__": — Memastikan blok ini hanya berjalan jika file dieksekusi langsung.

Baris 49: hm = SimpleHashMap(size=5) — Membuat aplikasi gudang baru yang punya 5 rak memori.

Baris 51 - 55: hm.insert(...) — Memasukkan 5 data contoh ke sistem (seperti TV, AC, Sepatu, dll).
<img width="817" height="402" alt="Screenshot 2026-06-09 225758" src="https://github.com/user-attachments/assets/525b70fc-38bf-4b88-8fa4-710902065917" />
Baris 57: hm.display() — Memerintahkan sistem menampilkan bentuk susunan rak yang baru saja diisi.

Baris 59: print("\nCari 'TV-55':", hm.search("TV-55")) — Meminta sistem mencari "TV-55" (pasti ketemu).

Baris 60: print("Cari 'HP-01':", hm.search("HP-01")) — Meminta sistem mencari "HP-01" (pasti tidak ketemu / None).

# Output Code
<img width="822" height="130" alt="Screenshot 2026-06-09 225835" src="https://github.com/user-attachments/assets/9fcc4c99-d761-4851-9eed-a4735225164c" />
Berdasarkan hasil output yang ditampilkan, terlihat bahwa fungsi hash berhasil mendistribusikan kelima data produk secara merata dan sempurna ke dalam lima slot rak memori yang tersedia (Rak 0 hingga Rak 4). Karena setiap SKU produk menghasilkan nilai indeks yang berbeda-beda, sistem tidak mengalami penumpukan data (collision), sehingga masing-masing rak hanya berisi tepat satu barang yang langsung diakhiri dengan penanda batas NULL. Selanjutnya, pada tahap uji coba pencarian, sistem berhasil menampilkan nama "Smart TV Samsung" saat mencari SKU 'TV-55' karena data tersebut cocok dan terdeteksi di dalam antrean rak yang dituju. Sebaliknya, saat sistem diminta mencari SKU fiktif 'HP-01', hasil yang dikembalikan adalah None (kosong) karena setelah rak tujuannya diperiksa hingga batas akhir antrean, kode barang tersebut memang tidak pernah tercatat di dalam memori.

# Link Youtube
https://youtu.be/Wk_IuYLRfYk
