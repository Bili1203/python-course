def celcius_farenheit(temp):
    return (temp * 9/5) + 32

def farenheit_celcius(temp):
    return (temp - 32) * 5/9

def celcius_kelvin(temp):
    return temp + 273

def kelvin_celcius(temp):
    return temp - 273

def farenheit_kelvin(temp):
    return (temp - 32) * 5/9 + 273

def kelvin_farenheit(temp):
    return (temp - 273) * 9/5 + 32

main_again = "y"

while main_again != "n":
    print ( "==Temperature Converter==")
    print ( "1 Celcius   -> Farenheit\n"
            "2 Farenheit -> Celcius\n"
            "3 Celcius   -> Kelvin\n"
            "4 Kelvin    -> Celcius\n"
            "5 Kelvin    -> Farenheit\n"
            "6 Farenheit -> Kelvin")

    try:
        strt =  int(input("Apa Yang Ingin Anda Lakukan: "))

    except ValueError:
        print("Invalid Data Type Input\n")

    else:
        if strt in range(1, 7): 
            again = "y"
            while again != "n":
                try:
                    temp = float(input("Masukkan suhu yang ingin dikonversi: "))
                except ValueError:
                    print("Invalid Data Type Input")
                    again = input("Apakah Anda Ingin mengulang (y/n)? ")
                    print ("")
                else:
                    again = "n"
                    if strt == 1:
                        print(f"Suhu Akhir Anda: {celcius_farenheit(temp):.1f}°F")
                    elif strt == 2:
                        print(f"Suhu Akhir Anda: {farenheit_celcius(temp):.1f}°C")
                    elif strt == 3:
                        print(f"Suhu Akhir Anda: {celcius_kelvin(temp):.1f}K")
                    elif strt == 4:
                        print(f"Suhu Akhir Anda: {kelvin_celcius(temp):.1f}°C")
                    elif strt == 5:
                        print(f"Suhu Akhir Anda: {kelvin_farenheit(temp):.1f}°F")
                    elif strt == 6:
                        print(f"Suhu Akhir Anda: {farenheit_kelvin(temp):.1f}K")
                    
                    main_again = input("Apakah Anda Ingin Menggunakan Converter (y/n)? ")

        else:
            print("Invalid Input\n")