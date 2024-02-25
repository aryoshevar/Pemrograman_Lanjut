#Tugas No.2
#Kasir pada restaurant

def menu():
    sum = 0
    start = "1"
    while start != "0":
        user_input = input()
        if user_input == "Nasi Goreng":
            sum += 10000
        elif user_input == "Mie Goreng":
            sum += 5000
        elif user_input == "Air Putih":
            sum += 3000
        elif user_input == "Es Teh":
            sum += 4000
        elif user_input == "Selesai":
            print("Harga: " , sum)
            start = "0"
        else:
            print("Menunya tidak ada pilihan")

print("-------------------------------------")
print("Selamat datang di Restaurant ACIKIWIR")
print("-------------------------------------")
print("\nPilih Menu: ")
print("1. Nasi Goreng   Rp.10.000")
print("2. Mie Goreng    Rp.5.000")
print("3. Air Putih     Rp.3.000")
print("4. Es Teh        Rp.4.000")
print("Ketik 'Selesai' untuk menyelesaikan pesanan!")
print("\nPesanan: ")
menu()