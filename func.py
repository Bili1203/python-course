def luas_persegi(panjang, lebar):
    return panjang * lebar
    
def volume_persegi(luas, tinggi):
    print(luas * tinggi)

panjang = int(input("Masukkan Panjang Persegi : "))
lebar = int(input("Masukkan Lebar Persegi : "))

#luas = luas_persegi(panjang, lebar)

tinggi = int(input("Masukkan Tinggi Persegi"))

volume_persegi(luas_persegi(panjang, lebar), tinggi)


def gaji_total(jam kerja, gaji per jam)
    if jam kerja > 50
        hasil = jam kerja * gaji per jam + 500
    else
        hasil = jam kerja * gaji per jam

'''
def luas_persegi(panjang,lebar):
    luas_persegi = panjang * lebar
    return luas_persegi

def volume_balok(luas_persegi,tinggi):
    volume = luas_persegi * tinggi
    print(volume)

panjang_input = int(input("Masukkan Panjang Persegi Panjang : "))
lebar_input = int(input("Masukkan Lebar Persegi Panjang : "))

luas = luas_persegi

luas_persegi(panjang_input, lebar_input)

tinggi_input = int(input("Masukkan Tinggi Balok : "))

volume_balok(luas, tinggi_input)
'''