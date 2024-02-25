"""
Nama    : Aryo Sheva Ramadhani
NIM     : 215150307111009
Kelas   : Pemrograman Lanjut - B
"""

import csv,os

def create_csv():
    with open('users.csv', mode='w', newline='') as file_csv:
        csv_writer = csv.writer(file_csv, delimiter='\t')
        csv_writer.writerow(['ID,Pass,Akses'])

def login(username, password):
    with open('users.csv', mode='r', newline='') as file_csv:
        csv_reader = csv.DictReader(file_csv)
        for row in csv_reader:
            if row['ID'] == username and row['Pass'] == password:
                return int(row['Akses'])
    return -1

def add_user(username, password, akses):
    with open('users.csv', mode='a', newline='') as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerow([username, password, akses])

def access_check(akses):
    if akses == 1:
        file = open("hello.txt","r")
        line = file.readlines()
        print(line[0])
    else:
        file = open("hello.txt","r")
        line = file.readlines()
        print(line[1])

if os.path.exists('users.csv') == False:
    create_csv()

print("=====Sistem Login dan Registrasi=====")
print("Menu: ")
print("1. Login")
print("2. Registrasi")

pilihan = input("Pilih: ")
if pilihan == '1':
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    akses = login(username, password)

    if akses != -1:
        access_check(akses)
    else:
        print("Login gagal, username atau password salah!")

elif pilihan == '2':
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    akses = input ("Admin?")

    if akses == 'iamgod':
        akses = '1'
    else:
        akses = '0'

    add_user(username, password, akses)
    print("Registrasi sukses!")

else:
    print("Pilihan tidak valid. Silahkan coba lagi")