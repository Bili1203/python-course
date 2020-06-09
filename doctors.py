print('Doctor Database')

doctors = []

def person(doctorname, doctorage, doctorspeciality, name):
    doctorname = {}
    doctorname['name'] = name
    doctorname['age'] = doctorage
    doctorname['speciality'] = doctorspeciality
    doctors.append(doctorname)

def sebut(list):
    for n in list:
        doctorname = n['name']
        doctorage = n['age']
        doctorspeciality = n['speciality']
        print(f'\nName: {doctorname}\nAge: {doctorage}\nName: {doctorspeciality}')

while True:
    add = input('Add doctor (y/n): ')
    if add == 'n':
        break
    elif add =='y':
        name = input('Enter name: ')
        age = input('Enter age: ')
        speciality = input('Enter speciality: ')
        person(name, age, speciality, name)
    else:
        print('Input invalid')

sebut(doctors)