# Nama: Liandra Rabbani
# NIM: 2607267
# Kelas: 1C

# contoh procedure
def nama_fungsi():
    print("Hello ini Fungsi")

nama_fungsi()
nama_fungsi()

def salam(ucapan):
    print(ucapan)

salam("Selamat siang")

# contoh function
def penjumlahan(a, b):
    hasil = a+ b 
    print("Luas persegi panjang:", hasil)
    return hasil
penjumlahan (2,3)


def kuadrat(angka):
    return angka * angka
bilangan = int(input("Masukkan bilangan: "))
hasil1= kuadrat(bilangan)
print("Hasil kuadrat:", hasil1)

def pengurangan(a,b):
    print (a-b)
pengurangan(5,7)
pengurangan(8,9)

def volumeb(p,l,t):
    volume = p*l*t
    return volume
print (volumeb(10,11,12))

# default value
def greetings(nama = "Noci"):
    print (f"halo,{nama}!")

greetings()
greetings("jagat")
greetings("abdul")
greetings("siti")

# Keyword argument
def pengurangana(a,b, c=3):
    print("hasilnya adalah",a-b)
# menggunakan keyword argument
pengurangana(b=2,a=5)
# tidak menggunakan
pengurangana(2,5)

pengurangana(a=10,c=2,b=5)

# arbitary argument
def funcArgs(*angka) :
    print("angka terakhir yang dimasukkan yaitu",angka [-1])

funcArgs(1,2,8,9,4,5)


# Latihan 1 no 1
def fibo(angka):
    if angka <= 1:
        return
    elif angka==1:
        return [0]
    deret= [0,1]

    while len(deret)< angka:
        baru=deret[-1]+ deret[-2]
        deret.append(baru)
    return deret

jumlah= 10
hasil= fibo(jumlah)
print(jumlah,"deret fibonacci pertama:")
print(hasil)

# Latihan 1 no 2
def volumet(r,t):
    rumus = 22/7*r*r*t
    return(rumus)
print (volumet(3,7))
print (volumet(7,2))

# Latihan 1 no 3
def nilai(a,b,c,d):
    total = a+b+c+d
    rata = total / 5
    return total,rata

total,rata= nilai(2,3,5,10)
print("Total:",total)
print("rata-rata:",rata)

# Latihan 2
def login():
    user="Daspro2023"
    pw="Latihan"
    kesempatan = 3
    while kesempatan > 0:
        name = input("Masukkan username: ")
        passw= input("Masukkan Password: ")

        if (passw == pw):
            print("Login berhasil")
            return True
        else:
            kesempatan -=1
            if (kesempatan > 0):
                print ("Login gagalm sisa kesempatan", kesempatan)
            else:
                print("percobaan habis")
            return False


# Latihan 3
def hitung_waktu(j1, m1, d1, j2, m2, d2):
    mulai = (j1 * 3600) + (m1 * 60) + d1
    selesai = (j2 * 3600) + (m2 * 60) + d2
    
    selisih = selesai - mulai
    
    j = selisih // 3600
    m = (selisih % 3600) // 60
    d = selisih % 60
    
    print(f"Output: {j} jam - {m} menit - {d} detik")

hitung_waktu(8, 10, 20, 9, 15, 30)
