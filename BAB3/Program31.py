thn = int(input("Masukkan Tahun: "))

if(thn % 4 == 0):
    if(thn % 100 == 0):
        if(thn % 400 == 0):
            print("Tahun Kabisat")
        else:
            print("Bukan Tahun Kabisat")
    else:
        print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")
