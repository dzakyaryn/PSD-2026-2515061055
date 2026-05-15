# Sistem pemutaran lagu berulang dalam playlist musik
# Deskripsi Singkat
Pengelolaan antrean lagu pada  aplikasi pemutar musik merupakan conntoh nyata dimana urutan media audio harus disusun secara terstruktur agar dapat diputar terus-menerus. Ketik pengguna menambahkan berbagai lagu ke dalam sebuah playlist, data berupa deretan audio tersebut membentuk daftar antrean yang mempresentasikan urutan hiburan berupa audio yang siap untuk didengarkan. Pengguna sering kali perlu mendengarkan musik secara terus-menerus tanpa jeda, seperti menginginkan pemutaran kembali secara otomatis setelah daftar urutan putarf mencapai batas akhirnya. Sistem harus mampu memutar lagu pertama kembali secara instan tanpa harus menghentikan aplikasi atau meminta pengguna menekan tombol putar secara manual satu per satu.

UNtuk mengatasi masalah tersebut, struktur data dan algoritma yanng sangat tepat untuk diterapkan pada skala pemutaran ini adalah circular queue. ALgoritma ini dipilih karena  memiliki cara kerja  yang sangat efisien dan cerdas dalam menghubungkan ujung akhir daftar putar kembali ke titik awal secara presisi menggunakan operasi matematika sisa . Circular queueu juga beroperasidengan mendaur ulang ruang memori dari lagu yang sudah selesai diputar untuk  diantrekan kembali,sehingga komputasinya sangat cepat,optimal dan fleksibel untuk memproses putaran siklus lagu  tanpa membebani kinerja memori perangkat keras pengguna.



