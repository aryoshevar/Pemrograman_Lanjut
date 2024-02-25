n = int(input("Jumlah bilangan genap yang akan disimpan: "))
count = 0

while (count != n):
    bil = int(input("Masukkan angka: "))
    if (bil % 2 == 0):
        print(bil, "\n")
        count += 1
    else:
        print("Bukan bilangan genap!\n")
