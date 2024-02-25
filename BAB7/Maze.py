"""
Nama: Aryo Sheva Ramadhani
NIM:  215150307111009
"""
x = y = 1

def maze(length, width, x, y):
    count = 0
    if x == length and y == width:
        count = 1
    else:
        if (x < length):
            count += maze (length,width,x+1,y)
        if (y < width):
            count += maze(length,width,x,y+1)
    return count

tinggi = int(input("Tinggi maze : "))
lebar = int(input("Lebar maze : "))
print(maze(tinggi, lebar, x, y))