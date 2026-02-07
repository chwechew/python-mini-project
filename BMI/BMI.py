Tinggi=float(input("Silahkan masukan tinggi anda dalam cm: "))
TinggiU=Tinggi/100
Berat=float(input("Silahkan masukan berat anda dalam kg: "))
BMI=Berat/(TinggiU**2)

if (BMI<16):
  print("makan kak")
elif (BMI>=16 and BMI<18.5):
  print("mamam kak")
elif (BMI>=18.5 and BMI<25):
  print("bagus kak")
elif (BMI>=25 and BMI<30):
  print("semangat kak")
elif(BMI>=30):
  print("waduh kak")

print("BMI anda adalah: {0} ".format(BMI), end="")