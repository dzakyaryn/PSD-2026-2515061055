def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort_pengeluaran(arr, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j]['harga'] < arr[pos]['harga']:
                pos = j
        if pos != i:
            tukar(arr, i, pos)


def main():
    try:
        n = int(input("Masukkan jumlah data jajan yang ingin dicatat: "))
    except ValueError:
        print("Input tidak valid!")
        return
    pengeluaran = []
    print("Masukkan elemen array:")
    for i in range(n):
        print(f"data ke-{i+1}:")
        hari = input("hari (misal: senin): ")
        jajan = input("nama jajan (misal: ayam geprek): ")
        while True:
            try:
                harga = int(input("harga (misal: 10000): Rp"))
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
        data_baru = {'hari': hari, 'jajan': jajan, 'harga': harga}
        pengeluaran.append(data_baru)
    print(f"Array sebelum diurutkan:")
    for item in pengeluaran:
        print(f"{item['hari']} | {item['jajan']} | Rp{item['harga']}")
    selection_sort_pengeluaran(pengeluaran, n)
    print("Array setelah diurutkan (Selection Sort):", end=" ")
    for item in pengeluaran:
        print(f"{item['hari']} | {item["jajan"]} | Rp{item['harga']}")



if __name__ == "__main__":
    main()
