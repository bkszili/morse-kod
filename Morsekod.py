import os
os.system("cls")

morse={}
#Beolvasás
with open("morsekodok.txt","r", encoding="utf-8") as beolvas:
    for sor in beolvas:
        kod = sor.split()
        if len(kod)==2:
            morse[kod[0]] = kod[1]
#Kiíratás
szoveg=input("Adj meg egy szót vagy mondatot és kiírom morse-kódként: ")
for betu in szoveg:
    if betu in morse:
        print(morse[betu], end=" ")
    else:
        print("'",betu,"'","Ez a betű nem tartozik a beolvasott txt-fájlba")