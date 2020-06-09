import datetime

year = int(input("masukkan tanggal :"))
month = int(input("masukkan bulan :"))
day = int(input("masukkan tanggal :"))

birthday = datetime.datetime(year ,month ,day )
age = (datetime.datetime.now() - birthday)

        #bornday = datetime.date(int(inp_year), int(inp_month), int(inp_day))
        #birthday = datetime.date(today.year, bornday.month, bornday.day)
        #if birthday < today:
            #yourage = today.year - bornday.year
        #lse:
            
            #yourage = today.year - bornday.year - 1
print('you are' + str(age.year) + 'years old!')
