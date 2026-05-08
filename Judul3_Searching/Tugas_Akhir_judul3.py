def cari_nilai_ujian(daftar_nilai, n, nilai_target):
    low = 0
    high = n - 1
    while nilai_target >= daftar_nilai[low] and nilai_target <= daftar_nilai[high] and low <= high:
        if daftar_nilai[high] == daftar_nilai[low]:
            if daftar_nilai[low] == nilai_target:
                return low
            break
        pos = low + int(((nilai_target - daftar_nilai[low]) / (daftar_nilai[high] - daftar_nilai[low])) * (high - low))
        print(f"Posisi estimasi: {pos}, nilainya: {daftar_nilai[pos]}")
        if nilai_target > daftar_nilai[pos]:
            low = pos + 1
        elif nilai_target < daftar_nilai[pos]:
            high = pos - 1
        else:
            return pos
    if low < n and daftar_nilai[low] == nilai_target:
        return low
    return -1

def main():
    daftar_nilai = [45, 50, 52, 60, 65, 68, 70, 75, 82, 85, 88, 90, 95]
    n = len(daftar_nilai)
    print(f"Daftar Nilai Ujian Tersedia: {daftar_nilai}")
    print(f"Total data mahasiswa: {n}")
    while True:
        try:
            nilai_target = int(input("Masukkan nilai ujian yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    pos = cari_nilai_ujian(daftar_nilai, n, nilai_target)
    if pos != -1:
        print(f"Ketemu pada indeks ke-{pos}")
    else:
        print(f"Tidak ketemu")

if __name__ == "__main__":
    main()