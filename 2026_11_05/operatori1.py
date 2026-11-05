# opis mobilnog telefona
proizvodjac = "Samsung" # string
model = "S26" # string
cena = 800    # int 
url_do_slike = "https://primer-putanje.png"  # string

print(proizvodjac, model, cena, url_do_slike)
print("Proizvodjac:", proizvodjac)
print("Model:", model)

print(f"Proizvodjac: {proizvodjac}, Model: {model}, Cena: {cena} eur") # f string

# Proizvodjac: Samsung
# Model: S26
# Cena: 800 eur

# \n - novi red    \t - tab  
# \  

print(f"Proizvodjac:\t{proizvodjac},\nModel:\t{model},\nCena:\t{cena} eur")

# Ovo je knjiga "Uvod u Python"
knjiga = "Uvod u Python"
print(f"Ovo je knjiga \"{knjiga}\"")
print(f"Ovo je knjiga '{knjiga}'")
print(f'Ovo je knjiga "{knjiga}"')


proizvodjac = "Samsung" # string
model = "S26" # string
cena = 800    # int 

print(cena + 100)
print(cena)

kolicina = 3
popust = 500

ukupna_cena = cena * kolicina
print(ukupna_cena)
cena_sa_popustom = ukupna_cena - popust
print("Ukupno sa popustom:", cena_sa_popustom)

rezultat = 2 + 3 * 4   # prioritet ima mnozenje - rezultat: 14
print(rezultat)

rezultat = (2 + 3) * 4   # zagrada odredjuje prioritet - rezultat: 20
print(rezultat)

print(10 / 2)

# posebni aritmeticki operatori
a = 10
b = 3

print(a / b)
print (a // b) # deljenje bez ostatka
print(a % b) # celobrojni ostatak pri deljenju 3*3 = 9 + 1 = 10

print(2 ** 3)

# primer sa kutijama
proizvodi = 24 # broj proizvoda
kapacitet_kutije = 5 

punih_kutija = proizvodi // kapacitet_kutije
print(f"Punih kutija imamo: {punih_kutija}")

ostatak_proizvoda =  proizvodi % kapacitet_kutije
print(f"Ostalo nam je visak: {ostatak_proizvoda} proizvoda")

# test
# ukupan broj proizvoda: 24
# u kutiju staje: 5
# ocekivani visak proizvoda: 4
# ocekivani visak proizvoda: 4 


# Prijava greske:
# Koraci:
# Unet brojo proizvoda 24
# U kutiju staje: 5 proizvoda
#
# Ocekivano (zeljeno) stanje:
# Pune 4 kutije i 4 proizvoda viska
#
# Trenutno stanje:
# Punih kutija imamo 4.8 i imamo 4 proizvoda viska

temperatura = 5
print(-temperatura)

# skracenice
poeni = 100 
# dodati 50 poena
print(poeni + 50)
# poeni = poeni + 50
poeni += 50
print(poeni)
poeni -= 10
print(poeni)
poeni *= 2 #poeni = poeni * 2
print(poeni)

# lives: * * 
lives = 3
lives -= 1

# vezba - kalkulator
# broj1 = input("Unesite prvi broj: ")
# broj2 = input("Unesite drugi broj: ")
# zbir = int(broj1) + int(broj2)
# print(zbir)

#"20" + "26" -> "2026"
# "20" -> 20
# "26" - > 26
# 20 + 26

# povrsina kruga
poluprecnik = 10
pi = 3.14
povrsina = poluprecnik ** 2 * pi
print(povrsina)

# login na sistem
# baza podataka -------------------------
# |user name: admin                     |
# |password: 1234                       |
# ---------------------------------------
user_name_baza = "admin"
password_baza = 1234

unet_user_name = "admin"
uneta_sifra = 123456

print(user_name_baza == unet_user_name)
print(password_baza == uneta_sifra)


# Primer racunanja cene sa porezom 
porez = 0.2
cena = 200
cena_sa_porezom = cena ** porez + cena # dobijeno
print(cena_sa_porezom) 

# ocekivano
ocekivana_cena_sa_porezom = 240
# poredim dobijeni rezultat sa ocekivanim
print(f"Test je prosao: {cena_sa_porezom == ocekivana_cena_sa_porezom}")

# Prijava bug-a:
# Izracuvanje cene sa porezom - daje neocekivan rezultat
# Koraci za reprodukciju:
# porez 0.2, cena 200

# Trenutno stanje:
# 202.8853
# 
# Ocekivano stanje:
# cena sa porezom: 240
