import random

print('''Selamat datang di game tebak kata hewan
Maksimal kesalahan huruf yang ditebak adalah 10''')

Hewan = ['capybara','berangberang','panda','buaya','pelikan']
 
acak = random.choice(Hewan)

HurufTertebak = '' 

kesempatan = 10

while kesempatan > 0:
    tebakan = input("Silahkan ketik huruf yang ingin ditebak: ")
    HurufTertebak += tebakan
    wrong = 0

    for letter in acak:
        if letter in HurufTertebak:
            print(letter)
        else:
            print("_")
            wrong = 1
        
    if wrong == 0:
        print("Selamat! Kamu berhasil!")
        print("Katanya adalah: ", acak)
        break
     
    if tebakan not in acak:    
        kesempatan -= 1 # no of chances will be decreased by 1
        print("Tebakanmu salah. Coba huruf lainnya")
        print("Kamu masih ada", kesempatan, "lagi untuk menebak. ")
         
        if kesempatan == 0:
            print("Maaf kesempatanmu sudah habis")