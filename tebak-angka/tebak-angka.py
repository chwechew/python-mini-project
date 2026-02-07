import random

kuncijawaban = random.randint(1, 100)

while True:
  tebakan = int(input('Untuk memainkan game ini, silakan tebak angka dari 1 sampai 100 di kolom jawaban ini...'))
  if kuncijawaban<tebakan:
    print('Maaf tebakanmu terlalu tinggi. Coba lagi')
  elif kuncijawaban>tebakan:
    print('Maaf tebakanmu terlalu rendah, Coba lagi')
  else:
    print('Mantap tebakanmu benar!')
    break