class Vector:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.data = [None] * self.capacity

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def push_back(self, value):
        if self.length == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.length] = value
        self.length += 1

    def pop_back(self):
        if self.length > 0:
            self.length -= 1

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        return -1

    def set(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value

    def size(self):
        return self.length

    def display(self):
        elements = [str(self.data[i]) for i in range(self.length)]
        print("[" + ", ".join(elements) + "]")

    def clear(self):
        self.data = None
        self.capacity = 0
        self.length = 0

class Antrean_Manager:
    def __init__(self):
        self.antrean = Vector()
        self.indeks_now = 0

    def tambah_lagu(self, judul_lagu):
        self.antrean.push_back(judul_lagu)
        print(f"Berhasil menambahkan {judul_lagu} ke antrean")

    def putar_sekarang(self):
        if self.antrean.size == 0:
            print("Antrean lagu tidak ada")
            return
        lagu = self.antrean.get(self.indeks_now)
        print(f"sedang memutar: {lagu}")

    def next_lagu(self):
        if self.antrean.size == 0:
            print("Antrean lagu tidak ada")
        elif self.indeks_now < self.antrean.size() - 1:
            self.indeks_now += 1
            self.putar_sekarang()
        else:
            print("Ini lagu terakhir dalam antrean")
    def prev_lagu(self):
        if self.antrean.size == 0:
            print("Antrean lagu tidak ada")
        elif self.indeks_now > 0:
            self.indeks_now -= 1
            self.putar_sekarang()
        else:
            print("Ini sudah lagu terakhir")
    def hapus_lagu(self):
        if self.antrean.size() > 0:
            if self.indeks_now == self.antrean.size() - 1 and self.indeks_now > 0:
                self.indeks_now -= 1
            self.antrean.pop_back()
            print("lagu terakhir berhasil dihapus")
        else:
          print("Antrean lagu tidak ada")


def main():
    yd_music = Antrean_Manager()

    yd_music.tambah_lagu("Love me not")
    yd_music.tambah_lagu("Somebody pleasure")
    yd_music.tambah_lagu("Happiness")
    yd_music.tambah_lagu("lesti sayang riski billar")

    yd_music.antrean.display()

    yd_music.putar_sekarang()
    yd_music.next_lagu()
    
    yd_music.hapus_lagu()
    yd_music.putar_sekarang()

if __name__ == "__main__":
    main()