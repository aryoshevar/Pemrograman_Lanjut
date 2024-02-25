"""
Aryo Sheva Ramadhani
215150307111009
"""

class Calculator:
    def tambah(self, x, y):
        self.hasil = x + y
        if (self.hasil % 1 == 0):
            return int(self.hasil)
        else:
            return self.hasil
        
    def kurang(self, x, y):
        self.hasil = x - y
        if (self.hasil % 1 == 0):
            return int(self.hasil)
        else:
            return self.hasil
    
    def kali(self, x, y):
        self.hasil = x * y
        if (self.hasil % 1 == 0):
            return int(self.hasil)
        else:
            return self.hasil

    def bagi(self, x, y):
        self.hasil = x / y
        if (self.hasil % 1 == 0):
            return int(self.hasil)
        else:
            return self.hasil

calculator = Calculator()

def int_input(message):
    isValid = False
    result = ''
    while not isValid:
        try:
            result = int(input(message).strip())
        except ValueError:
            print('Input harus angka')
        else:
            isValid = True
    
    return str(result)

def float_input(message):
    isValid = False
    result = ''
    while not isValid:
        try:
            result = float(input(message).strip())
        except ValueError:
            print('Input harus bilangan real')
        else:
            isValid = True
    
    return str(result)

x = float_input("Bilangan 1: ")
y = float_input("Bilangan 2: ")
x = float(x)
y = float(y)

print ("Operasi: ")
print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")

isExit = False
while(not isExit):
    isChoice = int_input("Pilih: ")
    isChoice = int(isChoice)

    if isChoice == 1:
        print(f"{calculator.tambah(x, y)}")
        isExit = True
    elif isChoice == 2:
        print(f"{calculator.kurang(x, y)}")
        isExit = True
    elif isChoice == 3:
        print(f"{calculator.kali(x, y)}")
        isExit = True
    elif isChoice == 4:
        try:
            print(f"{calculator.bagi(x, y)}")
        except ZeroDivisionError:
            print("Tidak dapat dibagi dengan 0")
        else:
            isExit = True
    else:
        print("Operasi tidak ditemukan")