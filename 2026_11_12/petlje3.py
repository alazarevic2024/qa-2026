import random

# broj = 10
# while broj > 0:
#     print("Hello")
#     broj -= 1

gorivo = 40

while gorivo > 0:
    print("voznja u toku")
    gorivo -= random.randint(4, 10)

print("voznja je zavrsena")


# kalkulator
# ako unese x kalkulator se iskljucuje 
# ako korisnik unese enter "" - samo ispisujemo trenutno stanje
# unoso broja, korisniku ispisujemo trenutni zbir
print("Dobrodosli u kalkulator, trenutna vrednost: 0")
zbir = 0

while True:
    unos = input("Unesite broj ili enter za proveru rezultata: ")
    if unos == "x":
        print("Korisnik je napustio kalkulator")
        break

    if unos == "":
        print("Trenutni rezultat je: ", zbir)
        continue

    if unos.isnumeric():
        zbir += int(unos)
        print("Trenutni rezultat je:", zbir)
    else:
        print("Dozvoljen je unos samo brojeva (ili x za napustanje programa)")