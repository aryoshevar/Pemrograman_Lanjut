"""
Nama    : Aryo Sheva Ramadhani
NIM     : 215150307111009
Kelas   : Pemrograman Lanjut - B
"""

buah = ("apel", "jeruk", "anggur", "mangga")
harga_buah = {'apel' : 5000,
              'jeruk' : 4000,
              'anggur' : 6000,
              'mangga' : 4500}
keranjang = {}

def inputKeranjang(input, jumlah):

    if (input in keranjang.keys()):
        keranjang[input] += jumlah
    else:
        keranjang.setdefault(input, jumlah)

def totalHarga(keranjang, harga_buah):

    total_harga = 0
    # temp = keranjang.keys()

    for i in (keranjang.keys()):
        total_harga += (int(keranjang[i]) * int(harga_buah[i]))
    
    return total_harga

print("======Toko Buah======")

for i in (harga_buah.keys()):
    print (i, end="\t")
    print ("Rp.", harga_buah[i])

while(True):
    print()
    print("1. Masukkan ke keranjang")
    print("2. Cek Keranjang")
    print("3. Bayar")
    pilih = input("Pilih: ")
    if (pilih == '1'):
        input_buah = input("Pilih buah: ")
        jumlah = input("Jumlah: ")
        if (input_buah in buah):
            inputKeranjang(input_buah, jumlah)
        else:
            print("Buah tidak ditemukan")
    elif(pilih == '2'):
        for i in (keranjang.keys()):
            print(i, end="\t")
            print(keranjang[i])
    elif(pilih == '3'):
        print(totalHarga(keranjang, harga_buah))
        break