print("program konversi uang asing ke rupiah")

print("")
def mata_uang_dunia():
    print("masukkan matauang yang akan di konversikan")
    print(" 1. dolar USA (RP.15.000)")
    print(" 2. EURO (RP.17.000)")
    print(" 3. RIYAL (RP 5.000)")
    print(" 4. Poundsterling (RP 20.500)")
print("")

masukan=0
mata_uang=0
hasil=0

while True:
    mata_uang_dunia()
    pilihan=input("masukan pilihan mu: ")
    pilihan=int(pilihan)

    if pilihan==1:
        masukan=input("Masukkan sebuah nominal: ")
        masukan=int(masukan)
        print("")
        mata_uang=16000
        hasil=masukan*mata_uang
        print(f" {masukan} Dolar USA senilai dengan{hasil} Rupiah")

    if pilihan==3:
        masukan=input("masukkan sebuah nominal: ")
        masukan=int(masukan)
        print("")
        mata_uang=5000
        hasil=masukan*mata_uang
        print (f" {masukan} Riyal senilai dengan{hasil} Rupiah")
    
    if pilihan==4:
        masukan=input("masukkan sebuah nominal: ")
        masukan=int(masukan)
        print("")
        mata_uang=20500
        hasil=masukan*mata_uang
        print (f" {masukan} Poundsterling senilai dengan {hasil} Rupiah")
    
    if pilihan==5:
        masukan=input("masukkan sebuah nominal: ")
        masukan=int(masukan)
        print("")
        mata_uang=18000
        hasil=masukan*mata_uang
        print(f" {masukan} EURO senilai dengan {hasil} Rupiah")
