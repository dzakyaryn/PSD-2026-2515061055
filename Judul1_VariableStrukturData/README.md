# Pengelolaan antrean lagu pada Platform Streaming Musik

# Deskripsi Singkat
Pengelolaan antrean lagu pada platform streaming musik merupakan contoh nyata dimana data harus disimpan secara berurutan namun fleksibel. ketika pengguna memutar lagu, mereka dapat menambahkan lagu ke daftar antrean seperti "tambahkan ke antrean", menghapus lagu dari daftar antrean, atau hanya ingin berpindah maju atau mundur ke lagu tertentu secara instan. sistem harus mampu menampung antrean yang selalu berubah-ubah tanpa menghentikan proses pemutaran lagu yang sedang berjalan.

Untuk mengatasi masalah tersebut, struktur data yang paling tepat adalah vektor (array dinamis). Vektor dipilih karena memiliki  kemampuan  untuk  mengakses data  secara instan saat sistem harus melompat ke lagu tertentu. Vektor juga dapat memperbesar atau memperkecil kapasitas ruang saat antrean sudah penuh oleh lagu-lagu sehingga manajemen memori menjadi lebih dinamis dan fleksibel.

# Source Code
