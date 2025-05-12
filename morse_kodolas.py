import os
os.system("cls")
morse={}
with open("morsekodok.txt","r", encoding="utf-8") as beolvas:
    for sor in beolvas:
        kod = sor.split()
        morse.append(kod)
szoveg=input("Adj meg egy betűt: ")
for betu in szoveg:
    betu = betu.upper()
    if betu in morse:
        print(morse[betu])