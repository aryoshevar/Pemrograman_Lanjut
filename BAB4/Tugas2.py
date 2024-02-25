"""
Nama    : Aryo Sheva Ramadhani
NIM     : 215150307111009
Kelas   : Pemrograman Lanjut - B
"""

mahasiswa = []

# Fungsi untuk memasukkan data mahasiswa dalam bentuk list dictionary
def insert_mahasiswa(nama, nim):
    mahasiswa.append({'nama' : nama, 'nim' : nim})
    return mahasiswa

# Fungsi untuk melakukan input mahasiswa
def input_mahasiswa():
    jumlah = int(input("Banyaknya mahasiswa yang akan ditambah: "))
    for i in range (jumlah):
        input_name = input("Masukkan Nama Mahasiswa: ")
        input_nim = input("Masukkan NIM Mahasiswa: ")
        print()
        name_title = convert_to_title(input_name)
        insert_mahasiswa(name_title, input_nim)

# Fungsi untuk mencari nama mahasiswa yang tersimpan
def search_name(nama):
    count = 0
    for i in range (len(mahasiswa)):
        if (nama in mahasiswa[i]['nama']):
            print("Nama Mahasiswa: ", mahasiswa[i]['nama'])
            print("NIM Mahasiswa: ", mahasiswa[i]['nim'])
            print()
            count += 1
    if (count == 0):
        print("Tidak ada mahasiswa yang bernama", nama)

# Fungsi untuk melakukan print seluruh nama mahasiswa
def print_mahasiswa():
    for i in range (len(mahasiswa)):
        print("Nama Mahasiswa: ", mahasiswa[i]['nama'])
        print("NIM Mahasiswa: ", mahasiswa[i]['nim'])
        print()

# Fungsi untuk mengubah string input menjadi kapital per kata
def convert_to_title(input_string):
    return input_string.title()

# Main Function
print("====Sistem Penyimpanan Data Mahasiswa====")
input_mahasiswa()

start = '1'
while (start != '0'):
    print("Pilih Operasi: ")
    print("1. Menambah mahasiswa")
    print("2. Mencari mahasiswa")
    print("3. Print list mahasiswa dengan cara slicing")
    print("4. Print mahasiswa")

    pilih = input("Pilih: ")
    print()

    if (pilih == '1'):
        input_mahasiswa()
    elif (pilih == '2'):
        cari = input("Cari nama mahasiswa: ")
        cari_title = convert_to_title(cari)
        search_name(cari_title)
    elif (pilih == '3'):
        index1 = int(input("Pilih index mahasiswa ke-"))
        index2 = int(input("Sampai ke-"))
        print(mahasiswa[index1:index2])
    elif (pilih == '4'):
        print_mahasiswa()
        start = '0'
    else :
        print("Operasi tidak ditemukan")
