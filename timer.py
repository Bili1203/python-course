import time

detik = int(input("Masukkan Berapa Detik : "))
menit = int(input("Masukkan Berapa Menit : "))
jam = int(input("Masukkan Berapa Jam : "))
waktu = detik + menit*60 + jam*3600
for x in range(waktu + 1):
    print(waktu - x)
    time.sleep(1)
print("Waktu Habis")