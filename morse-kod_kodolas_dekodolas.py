import os
os.system("cls")

morse={}
morse[" "]= "  "
print("..--------------------------..")
print("..--Választási lehetőségek--..")
print("..--------1 Kódolás---------..")
print("..--------2 Dekódolás-------..")
print("..--------3 Kilépés---------..")
print("..--------------------------..")
valasztas=int(input("Kérlek add meg a választott számodat: "))
if valasztas==1:
#1
#kódolás (Bakó Bálint csinálta)
    with open("morsekodok.txt","r", encoding="utf-8") as beolvas:
        for sor in beolvas:
            kod = sor.split()
            if len(kod)==2:
                morse[kod[0]] = kod[1]
    szoveg=input("Adj meg egy szót vagy mondatot és kiírom morse-kódként: ")
    print("A kódolás: ")
    eredmeny = ""  
    for betu in szoveg:
        if betu in morse:
            kodolt = morse[betu]
            print(kodolt, end=" / ")
            eredmeny = eredmeny + kodolt + " / "
        else:
            print("'",betu,"' Ez a karakter nem tartozik a beolvasott txt-fájlba")
    with open("eredmeny_kodolas.txt", "w", encoding="utf-8") as kiiras:
        kiiras.write("Kódolás: " + eredmeny)
    input()


elif valasztas==2:

#2
#dekodolas (Bálint-Kraft Szilárd csinálta)
    with open("morsekodok.txt", "r", encoding="UTF-8") as beolvas:
        for sor in beolvas:
            kod = sor.strip().split()
            if len(kod) == 2:
                betu, kod_morse = kod
                morse[betu] = kod_morse

    morse_dekod = {}
    for k in morse:
        v = morse[k]
        morse_dekod[v] = k

    morse_be = input("Adj meg egy szót vagy mondatot morse-kódként és kíírom a magyar ABC betűi szerint: ")


    morse_betu = morse_be.strip().split()

    dekodolt_szo = ""
    for kod in morse_betu:
        if kod in morse_dekod:
            dekodolt_szo += morse_dekod[kod]
        else:
            print(f"{betu} Ez a kód nem tartozik a beolvasott txt-fájlba")
    print("A dekódolás: ")
    print(dekodolt_szo)
    input()

    with open("eredmeny_kodolas.txt", "w", encoding="utf-8") as kiiras:
        kiiras.write("Kódolás: " + dekodolt_szo)
    input()

elif valasztas==3:
    print("Kiléptél.")
else:
    valasztas=int(input("Kérlek válassz másik érvényes."))
 
