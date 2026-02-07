InternetSpeed=int(input("Silahkan masukkan kecepatan internetmu"))

while InternetSpeed>0:
  if InternetSpeed>=50: 
    print("bguz")
    break
  elif InternetSpeed<50 and InternetSpeed>=25:
    print("aman")
    break
  elif InternetSpeed<25 and InternetSpeed>=1:
    print("jleg")
    break

else:
  print('parah si')