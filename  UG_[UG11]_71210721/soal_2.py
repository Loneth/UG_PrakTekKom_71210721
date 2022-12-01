def kelipatan_sembilan(a):
    # hasil = b % a
    if a % 9 == 0:
        hasil = "benar"
    else:
        hasil = "salah"
    print(hasil)


print("Pemeriksa kelipatan 9")
a = int(input("Masukkan kelipatan 9 yang ingin diperiksa: "))
kelipatan_sembilan(a)
