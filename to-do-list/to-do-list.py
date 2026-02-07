Penampung = []

def nambah():
  Input = input("Silahkan masukkan tugas: ")
  Penampung.append(Input)
  print(f"Tugas'{Penampung}'berhasil ditambahkan")

def lihat():
  if not Penampung: 
    print("Belum ada tugas yang ditambahkan")
  else:
    print("List tugasmu adalah: ")
    for i, Input in enumerate(Penampung, start=1):
      print(f"{i}.{Input}")

while True:
  print('''1. Tambah Tugas
2. Lihat Tugas''')
  
  PenampungNomor = input("Silahkan masukkan nomor: ")

  if PenampungNomor == '1':
    nambah()
  elif PenampungNomor == '2':
    lihat()
  else:
    print("Tidak valid")