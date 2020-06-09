def gaji_fix(gaji,bonus):
        print(int(gaji) + int(bonus))

jam_kerja = input("Masukkan Jam Kerja Anda :")
gaji = input("Masukkan Gaji Anda :")
bonus = 0
if jam_kerja >= "50":
    bonus += 150
else:
    bonus += 0

gaji_fix(gaji,bonus)
