# f(x) = 3x + 5

# def luas_persegi(panjang, lebar):
#     return panjang * lebar

# def volume_balok(luas, tinggi):
#     print(luas * tinggi)

# lebar = int(input('Berapakah lebar persegi: '))
# panjang = int(input('Berapakah panjang persegi: '))

# luas = luas_persegi(panjang, lebar)
# print(luas)

# tinggi = int(input('Berapakah tinggi baloknya: '))

# volume_balok(luas, tinggi)

# def awal():
#     print("Compute Pay")
#     print("===========")

# def pertanyaan():
#     nama = input("Siapakah nama pegawai: ")
#     jam = int(input("Berapa jam ia bekerja: "))
#     biaya = int(input("Berapa biaya per jam: "))

#     return nama, jam, biaya

# def computepay(jam, biaya):
#     if jam > 10:
#         return jam * biaya + 100
#     else:
#         return jam * biaya

# def run():
#    awal()
#    nama, jam, biaya = pertanyaan()
#    gaji = computepay(jam, biaya)
#    print(f"{nama} bekerja selama {jam} jam dan mendapatkan gaji {gaji}")

# run()

# def halo():
#     global siswa 
#     siswa = "Edu"
#     print(f"nama siswanya {siswa}")

# halo()
# print(f"nama siswanya {siswa}")


# murid = {
#     "nama" : "Edu",
#     "umur" : 17,
#     "rumah" : "Bekasi"
#  }

# murid = {}
# student = []

# def data(dictionary):
#     for key, value in dictionary.items():
#         print(key, value)

# def biodata():
#     nama = input("siapakah nama anda: ")
#     umur = input("berapakah umur anda: ")
#     rumah = input("dimana anda tinggal: ")

#     return nama, umur, rumah

# while True:
#     nama, umur, rumah = biodata()
#     murid["nama"] = nama
#     murid["umur"] = umur
#     murid["rumah"] = rumah

#     student.append(murid)

#     lagi = input("apakah anda mau make lagi (y/n)")
    
#     if lagi == "y":
#         continue
#     else:
#         break

# # data(murid)

# for x in student:
#     data(x)
# print(student)

murid = {}
student = []

def biodata():
    nama = input("Siapakah nama anda: ")
    umur = input("berapakah umur anda: ")
    rumah = input("dimana anda tinggal: ")

    return nama, umur, rumah

def vertikal(students):
    for student in students:
        for key, value in student.items():
            print(key, value)

while True:
    murid = {}
    nama, umur, rumah = biodata()
    murid["nama"] = nama
    murid["umur"] = umur
    murid["rumah"] = rumah

    student.append(murid)
    # print(student)

    lagi = input("apakah masih mau mengisi biodata (y/n): ")
    if lagi == "y":
        continue
    else:
        break

vertikal(student)