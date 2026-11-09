email_baza = "test@gmail.com"
sifra_baza = "123"

email_unos = "test@gmail.com"
sifra_unos = "1234"

# true ili false
rezultat_provere = email_baza == email_unos and sifra_baza == sifra_unos
if rezultat_provere:
    print("korisnik je uspesno ulogovan!")
    print("dobrodosli!")
    print("...")

print("Izvrsava se u svakom slucaju...")

# true / false 

print(bin(True))
print(bin(False))

brzina_vozila = 55
ogranicenje = 50
vec_imao_prekrsaje = False

if brzina_vozila > ogranicenje:
    print("Uruciti kaznu")    
    if vec_imao_prekrsaje:
        print("Oduzeti bodove")
    print("prva sledeca linija...")

print("Izvrsava se izvan provere u svakom slucaju")

# 
# dan_nedelji = "ponedeljak"
# if dan_nedelji == "ponedeljak":
#     print("postavi crvenu boju u kalendaru")
#     if prvi_ponedeljak_u_mesecu == True:
#         print("Danas je prvi ponedeljak u mesecu")
# elif dan_nedelji == "utorak":
#     print("postavi plavu boju")
# elif dan_nedelji == "sreda":
#     print("postavi zelena boju")
# elif dan_nedelji == "cetvrtak":
#     print("postavi zutu boju")
# else:
#     print("neispravan dan")

# unesi 1 - lista proizvoda
# unesi 2 - kupovina
# unesi 3 - izlazak iz aplikacije

# proizvod u ponudi
proizvod = "Telefon"
cena_proizvoda = 500
# korisnik 
ime = "marija"
stanje_na_racunu = 600


ulaz = int(input("Unesite:\n1 za pregled\n2 za kupovinu\n3 za izlaz\n"))
if ulaz == 1:
    print(f"Proizvod: {proizvod}\t Cena: {cena_proizvoda}")
elif ulaz == 2:
    print("Korisnik zeli da obavi kupovinu")
    if stanje_na_racunu >= cena_proizvoda:
        print("Uspesna kupovina!!!")
    else:
        print("Nemate dovoljno novca na racunu za kupovinu :(")
elif ulaz == 3:
    print("Korisnik zatvara aplikaciju.")
else:
    print("Pogresili ste unos")

print("izvrsava se u svakom slucaju...")

# varijnta sa petljom
# for i in range(5):  
#     korisnicko_ime = input("Unesite svoje ime: ")
#     stanje = input("Unesite svoje stanje na racunu: ")
#     ulaz = int(input("Unesite:\n1 za pregled\n2 za kupovinu\n3 za izlaz\n"))
#     if ulaz == 1:
#         print(f"Proizvod: {proizvod}\t Cena: {cena_proizvoda}")
#     elif ulaz == 2:
#         print("Korisnik zeli da obavi kupovinu")
#         if stanje_na_racunu >= cena_proizvoda:
#             print("Uspesna kupovina!!!")
#         else:
#             print("Nemate dovoljno novca na racunu za kupovinu :(")
#     elif ulaz == 3:
#         print("Korisnik zatvara aplikaciju.")
#     else:
#         print("Pogresili ste unos")

#     print("izvrsava se u svakom slucaju...")


# aplikacija podrzava dark i light temu
odabrana_tema = "dark"
detalji_odabrane_teme = ""

# varijanta - if else
if odabrana_tema == "dark":
    detalji_odabrane_teme = "Trenutna tema je tamna."
else:
    detalji_odabrane_teme = "Trenutna tema je svetla."

# varijanta - ternarni operator
                #         dodela ove vrednosti          ako je uslov true               druga opcija
detalji_odabrane_teme = "Trenutna tema je tamna." if odabrana_tema == "dark" else "Trenutna tema je svetla."