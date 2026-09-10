# import ini jangan dihapus/diedit yak
import random


def totalPenjualan(data, n):
    total = 0
    for i in range(n):
        total += data[i][1]
    return total


def penjualanTertinggi(data, n):
    tertinggi = data[0]

    for i in range(n):  
        if data[i][1] > tertinggi[1]:
            tertinggi = data[i]

    return tertinggi


def diAtasRataRata(data, rata_rata):
    jumlah = 0
    
    for namaBarang, jumlah in penjualan.items():
        if jumlah > rata_rata:
            jumlah += 1
    return jumlah


# Program Utama - Jangan dihapus/diedit yak
angka = int(input("NIM: "))
random.seed(angka)

barang = [
    "Beras",
    "Minyak",
    "Gula",
    "Telur",
    "Kopi",
    "Teh"
]

penjualan = {}

for namaBarang in barang:
    penjualan[namaBarang] = random.randint(100, 500)

data = list(penjualan.items())
n = len(data)

print("\n===== Data Penjualan =====")
for namaBarang, jumlah in penjualan.items():
    print(namaBarang, ":", jumlah)

total = totalPenjualan(data, n)
tertinggi = penjualanTertinggi(data, n)
rataRata = total / n
jumlahDiAtasRataRata = diAtasRataRata(penjualan, rataRata)

print("\n===== Hasil Analisis =====")
print("Total penjualan        :", total)
print("Penjualan tertinggi    :", tertinggi[0], "(", tertinggi[1], ")")
print("Rata-rata penjualan    :", round(rataRata, 2))
print("Di atas rata-rata      :", jumlahDiAtasRataRata, "barang")