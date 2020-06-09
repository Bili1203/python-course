openi = input("apakah anda ingin menggunakan kalkulator? (y/n)")

if openi == "y":
    print ("Silahkan")
else:
    exit()

while True:
    num1 = input("masukkan angka 1 :")
    num2 = input("masukkan angka 2 :")

    print ("Pilih salah satu")
    print ("1 = tambah")
    print ("2 = kurang")
    print ("3 = kali")
    print ("4 = bagi")
    operation = input("masukkan 1 / 2 / 3 / 4 : ")

    if operation == "1":
        print (int(num1) + int(num2))
    elif operation == "2":
        print (int(num1) - int(num2))
    elif operation == "3":
        print (int(num1) * int(num2))
    else: 
        print (int(num1) / int(num2))

    ending = input("apakah anda masih ingin menggunakan kalkulator? (y/n)")
    if ending == "y":
        continue
    else:
        break

    