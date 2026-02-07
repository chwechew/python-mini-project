import string
import random

PanjangPW = int(input("Seberapa panjang passwordmu? Silahkan tulis dengan angka= "))
print('''Pilihlah karakter yang ingin kamu masukkan dalam password:
      1. Kapital 
      2. Angka 
      3. Tandabaca
      4. Exit''')

KarakterList = ""

while(True):
  choice = int(input("Silahkan pilih salah satu antara 1-4 di atas   "))
  if(choice == 1):
    KarakterList += string.ascii_letters
  elif(choice == 2):
    KarakterList += string.digits
  elif(choice == 3):
    KarakterList += string.punctuation
  elif(choice == 4):
    break
  else:
    print("Mohon tetap pilih salah satu angka di atas")

password = []

for i in range(PanjangPW):
  KarakterRandom = random.choice(KarakterList)
  password.append(KarakterRandom)

print("Password yang telah dibuat: " + "".join(password))