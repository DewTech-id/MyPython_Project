# ==================================================================================================================================>>> LATIHAN GAME SEDERHANA <<<=========
# ====================================================<<< MEMBUAT PERMAINAN MELAWAN MONSTER (BATTLE OF HEROES) >>>=========================================================
# _________________________________________________________________________________________________________________________________________________________________________
import os, time

Level = input ("Level Berapa Yang Ingin dimainkan ? ")
Jumlah = input ("Jumlah Skill Yang diinginkan 1 sampai 3 (MAX 3) ? ")
Banyak = int(Jumlah)
Power = 0
Total = 0
i = 0
c = 0
skill = []
CD = []

if Banyak == 1:
    print ("Jumlah Power Yang dimiliki 900")
    Power = 900

elif Banyak == 2:
    print ("Jumlah Power Yang dimiliki 950, Aturlah sesuai dengan keinginan mu. (Tips : Aturlah dengan BIJAK !!!) ")
    print ("*Catatan* : Skill Dengan Jumlah Power Terbesar, Otomatis Memiliki 1 Couldown Pada Awal Permainan---")
    Power = 950

elif Banyak == 3:
    print ("Jumlah Power Yang dimiliki 1000, Aturlah sesuai dengan keinginan mu. (Tips : Aturlah dengan BIJAK !!!) ")
    print ("*Catatan* : Skill Dengan Jumlah Power Terbesar, Otomatis Memiliki 1 Couldown Pada Awal Permainan---")
    Power = 1000

def Penyesuaian():
    global Banyak, Total, i
    while Banyak <= 3 & Banyak != 0:
        set = input ("Masukan Jumlah Power Dari Skill :")
        skill.append(set)
        Total = int(skill[i]) + Total
        

        if Total > Power:
            print ("Maaf Pengaturan Skill Anda Melebihi Batas Power Anda >> Max Power :", Power)
            Total = Total - int(skill[i])
            del skill[i]
            
        else:
            print ("Skill",i+1 ," =", int(skill[i]))
            Banyak -= 1
            i += 1

def clear():
    input ("Press Enter To Check Status...")
    os.system ("cls")

Penyesuaian()
clear()

print (")=======>> STATUS PERMAINAN <<=======(")
print ("Level Yang anda Mainkan LEVEL", Level)
print ("Jumlah Skill Yang Dimiliki Adalah", Jumlah)

def status():
    global Banyak2
    Banyak2 = int(Jumlah)
    s = 0
    while Banyak2 <= 3 & Banyak2 != 0:
        print ("Skill", s+1, "= Power ", skill[s])
        s += 1
        Banyak2 -= 1

status()
print ("=========================================")
print ("LEVEL 1 --> (Melawan Monster)")
print ("MONSTER : HP = 4800, DAMAGE = 65, SKILL : 115/ 5 Turn")
print ("HP Pemain : 1000")
input ("Press Enter To Start...")
os.system ("cls")

monster = 4800
pemain = 1000
turn = 0
max = 0
ulang = 1
Damage = 65

def Coldown():
    global CD, c, max
    """while c < int(Jumlah):
        if max < int(skill[c]):
           CD.append(c)
           CD[c] = 1
           max = int(skill[c])
           c += 1

        else:
            CD.append(c)
            CD[c] = 0
            c += 1"""
    while c < int(Jumlah):
        CD.append(c)
        while max < int(Jumlah):
            if int(skill[c]) > int(skill[max]) and int(skill[c]) != int(skill[max]):
                CD[c] = 1
                max += 1
            elif int(skill[c]) < int(skill[max]) and int(skill[c]) != int(skill[max]):
                CD[c] = 0
                max += 1
            else:
                max += 1

        max = 0
        c += 1


Coldown()

def langkah():
    global turn, Damage, c, CD, ulang
    c = 0
    if ulang == 1:
        turn += 1

        if turn % 5 == 0:
            Damage = 115

        else:
            Damage = 65

        if turn > 1 :
            while c < int(Jumlah):
                if CD[c] != 0:
                    CD[c] -= 1
                    c += 1
                else:
                    c += 1
            c = 0


def mulai ():
    global monster, pemain, CD, ulang, Damage, s
    s = 0
    print ("Turn -->", turn)
    print ("HP MONSTER :", monster)
    print ("HP Pemain :", pemain)
    print ("=======================")

    print ("Pilih Jenis Serangan Kepada Monster :")
    print ("0 PUNCH.. (NO COULDOWN) [DMG: 50]")

    while int(Jumlah) > s:
        print (s+1,") SKILL", s+1, "(COULDOWN", CD[s],") [DMG:",skill[s], "]")
        s += 1

    serangan = input ("serangan Yang Akan Diberikan Adalah : ")
    print ("")

#==================================================================================================================================================== 1 SKILL ===========
    if Jumlah == '1':
        if serangan == '0':
            monster -= 50
            pemain -= Damage
            print ("Anda Memberikan 50 Serangan Kepada Monster, PUKULAN YANG LUAR BIASA !!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1

        elif serangan == '1' and CD[0] == 0:
            monster -= int(skill[0])
            pemain -= Damage
            print ("Anda Memberikan", skill[0], "Serangan Kepada Monster, HAHAHA, AMBIL INI!!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
            CD[0] += 3

        else:
            print ("Maaf Skill Yang Anda Gunakan Sedang coldown")
            #print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            #pemain -= Damage
            ulang = 0

            
#==================================================================================================================================================== 2 SKILL  ===========
    elif Jumlah == '2':
        if serangan == '0':
            monster -= 50
            pemain -= Damage
            print ("Anda Memberikan 50 Serangan Kepada Monster, PUKULAN YANG LUAR BIASA !!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
        
        elif serangan == '1' and CD[0] == 0:
            monster -= int(skill[0])
            pemain -= Damage
            print ("Anda Memberikan", skill[0], "Serangan Kepada Monster, HAHAHA, AMBIL INI!!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
            CD[0] += 3

        elif serangan == '2' and CD[1] == 0:
            monster -= int(skill[1])
            pemain -= Damage
            print ("Anda Memberikan", skill[1], "Serangan Kepada Monster, HAHAHA, AMBIL INI!!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
            CD[1] += 3

        else:
            print ("Maaf Skill Yang Anda Gunakan Sedang coldown")
            #print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            #pemain -= Damage
            ulang = 0

#==================================================================================================================================================== 3 SKILL  ===========
    elif Jumlah == '3':
        if serangan == '0':
            monster -= 50
            pemain -= Damage
            print ("Anda Memberikan 50 Serangan Kepada Monster, PUKULAN YANG LUAR BIASA !!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
        
        elif serangan == '1' and CD[0] == 0:
            monster -= int(skill[0])
            pemain -= Damage
            print ("Anda Memberikan", skill[0], "Serangan Kepada Monster, HAHAHA, AMBIL INI!!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
            CD[0] += 3

        elif serangan == '2' and CD[1] == 0:
            monster -= int(skill[1])
            pemain -= Damage
            print ("Anda Memberikan", skill[1], "Serangan Kepada Monster, HAHAHA, AMBIL INI!!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
            CD[1] += 3

        elif serangan == '3' and CD[2] == 0:
            monster -= int(skill[2])
            pemain -= Damage
            print ("Anda Memberikan", skill[2], "Serangan Kepada Monster, HAHAHA, AMBIL INI!!!")
            print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            ulang = 1
            CD[2] += 3

        else:
            print ("Maaf Skill Yang Anda Gunakan Sedang coldown")
            #print ("Anda Menerima", Damage, "Serangan Dari Monster, AKU SANGAT BERSEMANGAT !!!")
            #pemain -= Damage
            ulang = 0
        
#==================================================================================================================================================== AKHIR SKILL ===========
while monster > 0 and pemain > 0:
    langkah()
    mulai()
    input ("Press Enter To Next Turn...")
    os.system ("cls")

    if monster <= 0:
        print ("Selamat Anda Memenangkan Pertandingan Ini")

    elif pemain <= 0:
        print ("sayang Sekali Anda Telah Gagal Mengalahkan Monster, Try Againn... ")