"""
Nama: Aryo Sheva Ramadhani
NIM: 215150307111009
"""
def check(original, edited):
    if edited == original:
        print("Palindrom")
    else:
        print("Bukan palindrom")

def reversed(word):
    reverse_word = word[::-1]
    check(word,reverse_word)

n = int(input("Jumlah huruf yang ingin diperiksa : "))
for i in range(n):
    kata = input("Tuliskan sebuah kata : ")
    reversed(kata)