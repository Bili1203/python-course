real_user = "billy"
real_pass = "1234"

user_input = input("Masukkan Username: ")
pass_input = input("Masukkan Password: ")

if user_input == real_user and pass_input == real_pass:
    print ("login berhasil")
else:
    print("login gagal")