def prikazi_poruku():
    print("Zdravo")

prikazi_poruku()

x = [1, 2, 3] # lista
# izracunaj duzinu liste
print(len(x))


def pozdravi_korisnika(ime): # funkcija sa 1 obaveznim ulaznim parametrom 
    print(f"Zdravo {ime}")

pozdravi_korisnika(ime="Ana") # poziv funkcije

def pozdravi_korisnika1(ime=""):
    if ime != "":
        print(f"Zdravo {ime}")
    else:
        print(f"Zdravo! (mozete uneti svoje ime)")

pozdravi_korisnika1()
pozdravi_korisnika1("Marko")

def saberi(broj1, broj2):
    zbir = broj1 + broj2
    return zbir

        # dobijena povratna vrednost
print(saberi(10, 5))
dobijeni_rezultat = saberi(10,5)

print(dobijeni_rezultat)

def izracunaj_popust(cena, popust=0):
    nova_cena = cena - cena * popust / 100
    print(nova_cena)
    return nova_cena

cena_sa_popustom = izracunaj_popust(2000, 20)
print(cena_sa_popustom)
cena_sa_popustom = izracunaj_popust(1800)
print(cena_sa_popustom)


def test_login():
    print("Proveravamo login...")

def test_registracija():
    print("Proveravamo registraciju...")

def pokreni_test(zeljeni_test):
    print("**** Pocetak testa ****")
    zeljeni_test()
    print("*** Kraj testa ****")


pokreni_test(test_login)

# def dupliraj(broj):
#     return broj * 2

# print(dupliraj(5))

dupliraj = lambda broj: broj * 2
print(dupliraj(5))

import time
# Tajmer - odbrojavanje
def odbrojavanje(sekunde):
    print(sekunde)
    time.sleep(1)
    if sekunde > 0:
        odbrojavanje(sekunde-1)

odbrojavanje(5)