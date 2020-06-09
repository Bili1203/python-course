class Bunga:
    
    def __init__(self, nama, klopak, harga):
        self.nama = nama
        self.klopak = klopak
        self.harga = harga

    def bungaa(self):
        return f"Nama bunganya adalah {self.nama} , Kelopaknya berjumlah {self.klopak}, Memiliki harga sebesar {self.harga}\n"

tulip = Bunga("tulip", 5, 14.0)
print(tulip.bungaa())

anggrek = Bunga("anggrek", 4, 20.0)
print(anggrek.bungaa())

mawar = Bunga("mawar", 3, 30.0)
print(mawar.bungaa())

