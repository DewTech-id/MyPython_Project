# ===========================================================================================================================>>> LATIHAN PERHITUNGAN SEDERHANA <<<=========
# ================================================================<<< MEMBUAT PERHITUNGAN 4 JENIS BANGUN DATAR >>>=========================================================
# _________________________________________________________________________________________________________________________________________________________________________

import os, time

keliling = 0
luas = 0
ulang = False
bangun = ""
os.system('cls')

def mulai():
    global ulang
    print ("Selamat Datang Di Perhitungan Bangun Datar")
    input ("Tekan Enter Untuk Melanjutkan... ")
    os.system('cls')

    while True:
        global bangun
        print ("Berikut Merupakan Menu Pilihan Perhitungan Bangun Datar >>> ")
        print ("1. Bangun Persegi")
        print ("2. Persegi Panjang")
        print ("3. Bangun segitiga")
        print ("4. Bangun Jajar Genjang")
        menu = input ("Perhitungan Bangun Datar Yang diinginkan : ")
        os.system ('cls')

        if int(menu) < 1 or int(menu) > 4:
            input ("Maaf Menu Yang Anda Pilih Tidak Tersedia, Silahkan Mengulangi Kembali...")
            os.system('cls')

        else:
            print ("Berikut Merupakan Hasilnya >>> ")
            if int(menu) == 1:
                bangun = "PERSEGI"
                persegi()
                if ulang == False:
                    break
            
            elif int(menu) == 2:
                bangun = "PERSEGI PANJANG"
                persegi_panjang()
                if ulang == False:
                    break
            
            elif int(menu) == 3:
                bangun = "SEGITIGA"
                segitiga()
                if ulang == False:
                    break
            
            elif int(menu) == 4:
                bangun = "JAJAR GENJANG"
                jajargenjang()
                if ulang == False:
                    break
    selesai()

 # ===============================================================================================[ PERHITUNGAN PERSEGI ]======================= 
def persegi():
    global ulang, sisi
    print(" *** Silahkan Melakukan Inputan Berikut *** ")
    s = input ("Panjang Sisi Persegi : ")
    sisi = int(s)
    
    if int(sisi) > 0:
        keliling = 4 * sisi
        luas = sisi * sisi

        os.system ('cls')
        print ('Perhitungan Bangun Datar >> " [BANGUN PERSEGI] " ')
        print ("Panjang Sisi Persegi :", sisi)
        print ("Hasil Keliling :", keliling)
        print ("Hasil Luas :", luas)
        print ("Bentuk Bangun Dalam satuan * ")
        for i in range(sisi):
            print ("   ")
            for j in range(sisi):
                print("*", end=(" "))
        print (" ")
        ulang = False

    else:
        ulang = True
        print ("<<< ATTENTION >>>")
        input ("Silahkan Untuk Menggulangi Perhitungan, Hasil Yang Anda Inputkan Tidak Sesuai... (Bilangan Real) ")
        os.system('cls')

# ===========================================================================================[ PERHITUNGAN PERSEGI PANJANG ]======================= 
def persegi_panjang():
    global ulang, panjang, lebar
    print(" *** Silahkan Melakukan Inputan Berikut *** ")
    p = input ("Panjang Persegi Panjang : ")
    panjang = int(p)
    l = input ("Lebar Persegi Panjang : ")
    lebar = int(l)
    
    if panjang < lebar:
        ulang = True
        print ("<<< ATTENTION >>>")
        input ("Silahkan Untuk Menggulangi Perhitungan, Besar Panjang Lebih Kecil dibandingkan Lebar (*Panjang Harus Lebih Besar*)")
        os.system('cls')
    
    elif panjang > 0 and lebar > 0:
        keliling = 2 * (panjang + lebar)
        luas = panjang * lebar

        os.system ('cls')
        print ('Perhitungan Bangun Datar >> " [BANGUN PERSEGI PANJANG] " ')
        print ("Panjang Persegi Panjang :", panjang)
        print ("Lebar Persegi Panjang   :", lebar)
        print ("Hasil Keliling :", keliling)
        print ("Hasil Luas :", luas)
        print ("Bentuk Bangun Dalam satuan * ")
        for i in range(lebar):
            print ("   ")
            for j in range(panjang):
                print("*", end=(" "))
        print (" ")
        ulang = False

    else:
        ulang = True
        print ("<<< ATTENTION >>>")
        input ("Silahkan Untuk Menggulangi Perhitungan, Hasil Yang Anda Inputkan Tidak Sesuai... (Bilangan Real) ")
        os.system('cls')

# ===========================================================================================[ BANGUN SEGITIGA ]==========================================
def segitiga():
    global ulang

    print (" 1. Segitiga Sama Sisi ")
    print (" 2. Segitiga Siku-siku ")
    pilihan = input ("Jenis Segitiga Yang Anda Pilih ... ")
    os.system('cls')

    if int(pilihan) > 2 or int(pilihan) < 1:
        ulang = True
        print ("<<< ATTENTION >>>")
        input ("Silahkan Untuk Menggulangi Perhitungan, Hasil Yang Anda Inputkan Tidak Sesuai... (Pilihan Hanya 1 Dan 2) ")
        os.system('cls')

    elif pilihan == '1' or pilihan == '2': 
        print ("*** Silahkan Masukan Inputan Berikut ***")
        print (" Input Nilai Sesuai Dengan Aturan Bangun Tersebut ")

        a = input ("Alas Segitiga : ")
        alas = int(a)
        t = input ("Tinggi Segitiga : ")
        tinggi = int(t)
        m = input ("Kemiringan Segitiga : ")
        miring = int(m)

        keliling = alas + tinggi + miring
        luas = alas * tinggi / 2
        os.system('cls')
        
        if pilihan == '1':
            if alas == tinggi & alas == miring:
                print ('Perhitungan Bangun Datar >> " [BANGUN SEGITIGA SAMA SISI] " ')
                print ("Alas Segitiga :", alas)
                print ("Tinggi Segitiga   :", tinggi)
                print ("Hasil Keliling :", keliling)   
                print ("Hasil Luas :", luas)
                print ("Bentuk Bangun Dalam satuan * ")
                print (" ")
                for baris in range(alas):
                    for jarak in range(baris + 1, alas):
                        print (" ", end=(""))

                    for banyak in range(baris + 1):
                        print ("*", end=(" "))
                    print (" ")
                ulang = False

            else:
                ulang = True
                print ("<<< ATTENTION >>>")
                input ("Silahkan Untuk Menggulangi Perhitungan, Hasil Yang Anda Inputkan Tidak Sesuai... (Alas, Tinggi, Kemiringan Harus Sama) ")
                os.system('cls') 
        
        elif pilihan == '2':
            if alas == tinggi & alas != miring:
                print ('Perhitungan Bangun Datar >> " [BANGUN SEGITIGA SIKU-SIKU] " ')
                print ("Alas Segitiga :", alas)
                print ("Tinggi Segitiga   :", tinggi)
                print ("Kemiringan Segitiga   :", miring)
                print ("Hasil Keliling :", keliling)   
                print ("Hasil Luas :", luas)
                print ("Bentuk Bangun Dalam satuan * ")
                print (" ")
                for i in range(int(alas + 1)):
                    for j in range(i):
                        print ("*", end=(" "))
                    print (" ")
                ulang = False

            else:
                ulang = True
                print ("<<< ATTENTION >>>")
                input ("Silahkan Untuk Menggulangi Perhitungan, Hasil Yang Anda Inputkan Tidak Sesuai... (Alas Dan Tinggi Harus Sama Kecuali Kemiringan) ")
                os.system('cls') 

# ===========================================================================================[ BANGUN JAJAR GENJANG ]==========================================
def jajargenjang ():
    global ulang

    a = input ("Alas Jajar Genjang : ")
    alas = int(a)
    t = input ("Tinggi Jajar Genjang : ")
    tinggi = int(t)
    m = input ("Kemiringan Jajar Genjang : ")
    miring = int(m)

    keliling = 2 * alas + 2 * miring
    luas = alas * tinggi / 2
    os.system('cls')

    print ('Perhitungan Bangun Datar >> " [BANGUN JAJAR GENJANG] " ')
    print ("Alas Jajar Genjang :", alas)
    print ("Tinggi Jajar Genjang   :", tinggi)
    print ("Kemiringan Jajar Genjang   :", miring)
    print ("Hasil Keliling :", keliling)   
    print ("Hasil Luas :", luas)
    print ("Bentuk Bangun Dalam satuan * ")
    print (" ")

    for i in range(tinggi):
        for jarak in range(i):
            print (" ", end=(" "))
            
        for j in range(alas):
            print ("*", end=(" "))
        print (" ")

def selesai():
    global bangun
    print (" ")
    print ("Berikut Hasil Perhitungan Bangun Datar", bangun, "...")
    print (" ")
    print ("Apakah Anda Ingin Mengulagi Perhitungan Ini ???")
    akhir = input ('"Iya" (Jika Mengulangi) Dan "Tidak" (Jika Cukup) ... ')
    
    if str(akhir) == "Iya":
        os.system ('cls')
        keliling = 0
        lebar = 0
        mulai()
    
    else:
        os.system('cls')
        print ("Terima Kasih Telah Menggunakan Program Perhitungan Ini :) ")

mulai()
    
    