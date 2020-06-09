import random

angka = random.randint(1,10)

print("Tebak Angka dari 1 sampai 10")

try:

    while True:
        guess = int(input("Masukkan Angka : "))
        if guess < angka:
            print("Terlalu Kecil")
        elif guess > angka:
            print("Terlalu Besar")
        elif guess == angka:
            print("Tebakan Kamu Benar")
            break
        else:
            print("Masukkan Data Yang Benar")
except:
    print("Masukkan Data Yang Benar")