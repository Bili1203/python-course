count = 0 
while True: 
    username = input("\nUsername: ") 
    password = input("Password: ")
    count += 1
    if count == 3:
        print("Terlalu banyak mencoba") 
        break 
    else:
        if username == 'billy' and password == '1234':
            print("Berhasil Masuk")
            break 
        else:
            print("Coba Lagi")
            continue