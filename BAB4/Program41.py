perusahaan = 'Microsoft'
list_pulau = ['Jawa', 'Sumatra', 'Sulawesi']

mahasiswa = {
    'nama': 'Lendis Fabri',
    'asal': 'Lamongan'
}

print(
    "Apakah 'c' ada di variabel perusahaan?",
    'c' in perusahaan
)
print(
    "Apakah 'z' tidak ada di variabel perusahaan?",
    'z' not in perusahaan
)
print(
    "Apakah 'Madura' ada di variabel list_pulau?",
    'Madura' in list_pulau
)
print(
    "Apakah 'Madura' tidak ada di variabel list_pulau?",
    'Madura' not in list_pulau
)
print(
    "Apakah atribut 'nama' ada di variabel mahasiswa?",
    'Lamongan' in mahasiswa['asal']
)