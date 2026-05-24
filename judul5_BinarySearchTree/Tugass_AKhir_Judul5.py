class NodeKelas:
    def __init__(self, mulai, selesai, kelas):
        self.mulai = mulai
        self.selesai = selesai
        self.kelas = kelas
        self.left = None
        self.right = None


class KalenderBST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, mulai, selesai, kelas):
        if root is None:
            return NodeKelas(mulai, selesai, kelas)
        if mulai < root.mulai:
            root.left = self.insert_node(root.left, mulai, selesai, kelas)
        elif mulai > root.mulai:
            root.right = self.insert_node(root.right, mulai, selesai, kelas)
        return root

    def delete_node(self, root, mulai):
        if root is None:
            return root, False
        
        found = False
        if mulai < root.mulai:
            root.left = self.delete_node(root.left, mulai)
        elif mulai > root.mulai:
            root.right = self.delete_node(root.right, mulai)
        else:
            found = True
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right, found
            elif root.right is None:
                return root.left, found
            else:
                successor = self.find_min_node(root.right)
                root.mulai = successor.mulai
                root.selesai = successor.selesai
                root.kelas = successor.kelas
                root.right = self.delete_node(root.right, successor.mulai)
        return root

    def batalkan_jadwal(self, mulai):
        self.root, found = self.delete_node(self.root, mulai)
        return found

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current
    
    def find_successor(self, waktu_mulai):
        current = self.root
        successor = None
        while current is not None:
            if waktu_mulai < current.mulai:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor

    def find_predecessor(self, waktu_mulai):
        current = self.root
        predecessor = None
        while current is not None:
            if waktu_mulai > current.mulai:
                predecessor = current
                current = current.right
            else:
                current = current.left
        return predecessor

    def cek_dan_tambah_jadwal(self, mulai, selesai, kelas):
        pred = self.find_predecessor(mulai)
        if pred is not None:
            if pred.selesai > mulai:
                print(f"GAGAL: tabrakan dengan '{pred.kelas}' (Berakhir jam {pred.selesai:04d})")
                return False

        succ = self.find_successor(mulai)
        if succ is not None:
            if selesai > succ.mulai:
                print(f" GAGAL: Tabrakan dengan '{succ.kelas}' (Dimulai jam {succ.mulai:04d})")
                return False

        self.root = self.insert_node(self.root, mulai, selesai, kelas)
        print(f"BERHASIL: Jadwal '{kelas}' ditambahkan!")
        return True

    def cetak_jadwal(self, root):
        if root is not None:
            self.cetak_jadwal(root.left)
            print(f"- {root.mulai:04d} s/d {root.selesai:04d} | {root.kelas}")
            self.cetak_jadwal(root.right)

    def tampilkan_semua(self):
        print("\n=== JADWAL MATA KULIAH HARI INI ===")
        if self.root is None:
            print("(Belum ada jadwal)")
        else:
            self.cetak_jadwal(self.root)
        print("===================================")
def main():
    kalender = KalenderBST()
    pilih = 0
    while pilih != 5:
        print("\n=== SISTEM BOOKING JADWAL MATA KULIAH ===")
        print("1. Tambah Jadwal Baru (Insert)")
        print("2. Batalkan Jadwal (Delete)")
        print("3. Tampilkan Seluruh Jadwal (In-order)")
        print("4. Cek Kelas Terdekat (Predecessor/Successor)")
        print("5. Keluar")
        
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            continue
            
        if pilih == 1:
            try:
                print("\n[Gunakan format waktu 24 jam, contoh: 0900 untuk 09:00]")
                mulai = int(input("Waktu Mulai   : "))
                selesai = int(input("Waktu Selesai : "))
                if mulai >= selesai:
                    print(" Waktu selesai harus lebih besar dari waktu mulai!")
                    continue
                kelas = input("Kelas Mata Kuliah  : ")
                kalender.cek_dan_tambah_jadwal(mulai, selesai, kelas)
            except ValueError:
                print("Input waktu tidak valid!")
                
        elif pilih == 2:
            try:
                print("\n[Masukkan Waktu Mulai dari rapat yang ingin dibatalkan]")
                mulai = int(input("Waktu Mulai: "))
                berhasil = kalender.batalkan_jadwal(mulai)
                if berhasil:
                    print(f"Jadwal pada pukul {mulai:04d} berhasil dibatalkan.")
                else:
                    print("Jadwal tidak ditemukan!")
            except ValueError:
                print("Input waktu tidak valid!")
                
        elif pilih == 3:
            kalender.tampilkan_semua()
            
        elif pilih == 4:
            try:
                waktu = int(input("\nMasukkan waktu pengecekan (contoh: 1200): "))
                pred = kalender.find_predecessor(waktu)
                succ = kalender.find_successor(waktu)
                
                print(f"\n--- HASIL PENGECEKAN PADA PUKUL {waktu:04d} ---")
                if pred:
                    print(f"kelas Sebelumnya : {pred.mulai:04d} - {pred.selesai:04d} ({pred.kelas})")
                else:
                    print("Kelas Sebelumnya : (Tidak ada)")
                    
                if succ:
                    print(f"Kelas Selanjutnya: {succ.mulai:04d} - {succ.selesai:04d} ({succ.Kelas})")
                else:
                    print("Kelas Selanjutnya: (Tidak ada)")
            except ValueError:
                print("Input waktu tidak valid!")
                
        elif pilih == 5:
            print("Program selesai. Sampai jumpa!")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
