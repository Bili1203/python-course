def ask_name():
    nama = input('What is ur name: ')
    return nama

def ask_data():
    jam_kerja = int(input('Enter your working hours: '))
    gaji_jam = int(input('Enter your rate per hour: '))   
    return jam_kerja, gaji_jam

def compute_pay(x, y):
    print(x,y)
    if x > 40:
        total = x * y + 500
    else:
        total =  x * y
    return total

def run():
    print ('SALARY COMPUTATION FOR EMPLOYEES')
    print ('-------------')
    name = ask_name()
    hour, rate = ask_data()
    pay = compute_pay(hour, rate)
    print (f'Hey {name}, your salary is {pay}')

run()