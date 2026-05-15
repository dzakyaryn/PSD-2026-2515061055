class LoopingPlaylist:
    def __init__(self, max_lagu=3):
        self.MAXN = max_lagu
        self.playlist = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def TambahLagu(self, judullagu):
        if self.is_full():
            print("playlist penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.playlist[self.rear_idx] = judullagu
        print(f"Lagu {judullagu} berhasil ditambahkan")

    def PutarLaguBerikutnya(self):
        if self.front_idx == -1:
            print("PLAYLIST KOSONG. tidak ada yang bisa diputar.")
            return
        lagusekarang = self.playlist[self.front_idx]
        print(f"sedang memutar: {lagusekarang}")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN
        self.TambahLagu(lagusekarang)



def main():
    playlist = LoopingPlaylist()
    pilih = 0
    while pilih != 3:
        print("\n=== Playlist Lagu ===")
        print("1. Tambah Lagu")
        print("2. Putar Lagu berikutnya")
        print("3. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            val = (input("Nama lagu: "))
            playlist.TambahLagu(val)
        elif pilih == 2:
            playlist.PutarLaguBerikutnya()
        elif pilih == 3:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
