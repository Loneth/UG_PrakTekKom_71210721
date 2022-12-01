def penjumlahan(bil1, bil2):
    hasil = bil1 + bil2
    print(f"Hasil operasi dari {bil1} + {bil2} = {hasil}")


def pengurangan(bil1, bil2):
    hasil = (bil1 - bil2)
    print (f"Hasil operasi dari {bil1} - {bil2} = {hasil}")


def perkalian(bil1, bil2):
    hasil = (bil1 * bil2)
    print(f"Hasil operasi dari {bil1} * {bil2} = {hasil}")


def pembagian(bil1, bil2):
    hasil = (bil1 / bil2)
    print(f"Hasil operasi dari {bil1} / {bil2} = {hasil}")


print(f"{'=' * 10}")
print("Operasi Matematika")
print("1. Jumlah [+]")
print("2. Kurang [-]")
print("3. Kali   [*]")
print("4. Bagi   [/]")
print(f"{'=' * 10}")
# print("")
pilihan = int(input("Pilih operasi (1/2/3/4): "))
print(f"{'=' * 10}")
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

if pilihan == 1:
    penjumlahan(bil1, bil2)
elif pilihan == 2:
    pengurangan(bil1, bil2)
elif pilihan == 3:
    perkalian(bil1, bil2)
elif pilihan == 4:
    pembagian(bil1, bil2)
