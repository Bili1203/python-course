class Tube:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.operation = None
        self.volume = None
        self.area = None

        history.append(self)

    def tube_volume(self):
        self.operation = "volume"
        self.volume = f"{self.height*3.14*self.radius**2:.2f}"

        return self.volume

    def tube_area(self):
        self.operation = "area"
        self.area = f"{3.14*self.radius**2:.2f}"

        return self.area

    def history(self):
        if self.operation == "volume":
            return f"Radius Tabung {self.radius}, Tinggi Tabung {self.height}, Volume Tabung {self.volume}"

        elif self.operation == "area":
            return f"Radius Tabung {self.radius}, Tinggi Tabung {self.height}, Luas Alas Lingkaran Tabung {self.area}"

    @classmethod
    def new_tube(cls):
        radius = float(input("Masukkan Jari-Jari Tabung: "))
        height = float(input("Masukkan Tinggi Tabung: "))
        return cls(radius, height)


history = []

print("==Tube Calculator==")
use = input("Mau Menggunakan Calculator (y/n)? ")
while use == "y":
    try:
        main = "y"
        tube = Tube.new_tube()

    except ValueError:
        print("Invalid Data Type")

    except KeyboardInterrupt:
        exit()

    except:
        print("Something Went Wrong")

    else:
        while main != "n":
            main = "n"
            print("1 Hitung Luas Lingkaran Alas\n"
                  "2 Hitung Volume Tabung")
            calc = input("Apa yang ingin dihitung? ")

            if calc == "1":
                print(f"Luas Lingkaran Alas Tabung {tube.tube_area()}")

            elif calc == "2":
                print(f"Volume Tabung {tube.tube_volume()}")

            else:
                print("Invalid Input")
                main = input("Mau Coba Lagi (y/n)? ")

            use = input("Apakah Masih ingin Menggunakan Calculator (y/n)? ")

print("==Usage History==")
for items in history:
    print(tube.history())
