score=input("Masukkan Nilai:")
try:
  if int(score) >= 90 and int(score) <= 100:
    print("A")
  elif int(score) >= 80 and int(score) <= 90:
    print("B")
  elif int(score) >= 70 and int(score) <= 80:
    print("C")
  elif int(score) >= 60 and int(score) <= 70:
    print("D")
  elif int(score) > 0 and int(score) <= 60:
    print("F")
  else:
    print("Salah input, masukkan angka")  
except ValueError: 
    print("Salah input, masukkan angka")
