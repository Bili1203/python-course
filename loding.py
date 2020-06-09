import time
print ("Mohon Tunggu")

a = 0
while a < 3:
    for x in range (0,4):
        b = "Loading" + "."  * x
        print(b)
        time.sleep(0.5)

    a += 1

print("Silahkan Masuk")