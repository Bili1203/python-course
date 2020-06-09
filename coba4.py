class Bunga:
    
    def __init__(self, nama, klopak, harga):
        self.nama = nama
        self.klopak = klopak
        self.harga = harga

    @classmethod
    def input(cls):
        nama = input("Masukkan nama bunga:")
        klopak = int(input("Masukkan Jumlah:"))
        harga = float(input("Masukkan Harga:"))
        return cls(nama,klopak,harga)
    
    def bungaa(self):
        return f"Nama : {self.nama} , Jumlah : {self.klopak}, Harga : {self.harga}"

while True:
    last = Bunga.input()
    print(last.bungaa())
    ending = input("Apakah ingin mengisi lagi ?(y/n)")
    if ending == "y":
        continue
    else:
        break