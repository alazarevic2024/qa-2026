# upisani korisnici
registrovani_korisnici = ["petar", "a n a ", "marija", "marko"]
# provera korisnika 
# korisnicko ime duze od 3 karaktera, zabranjena prazna mesta
neispravni_korisnici = [] # inicijalno prazna lista
for korisnik in registrovani_korisnici:
    formatirano_ime = korisnik.replace(" ", "")
    if len(formatirano_ime) > 3:
        print("Korisnicko ime je ispravno")
    else:
        print("Korisnicko ime nije ispravno")
        neispravni_korisnici.append(korisnik)

print(neispravni_korisnici)

# lista sa razlicitim tipovima podataka
#             0        1       2
proizvod = ["Telefon", 100, "Uredjaji"]
print(f"Proizvod u ponudi:\nNaziv: {proizvod[0]}\nCena: {proizvod[1]}\nKategorija: {proizvod[2]}")
# izmena cene
proizvod[1] =250
print(f"Proizvod u ponudi:\nNaziv: {proizvod[0]}\nCena: {proizvod[1]}\nKategorija: {proizvod[2]}")

for informacija in proizvod:
    print(informacija)

for indeks in range(len(proizvod)):
    print(indeks)
    print(proizvod[indeks])

#          0 - Telefon, 1 - 100, 2 - Uredjaji
# proizvod = ["Telefon", 100, "Uredjaji"]

for indeks, vrednost in enumerate(proizvod):
    print(f"Indeks: {indeks}, Vrednost: {vrednost}")

proizvod.clear()
print(proizvod)

korpa = ["Telefon", "Slusalice", "Punjac"]
print("Trenutna korpa:", korpa)
korpa.clear()
print(korpa)

korisnici = ["marija", "ana", "petar", "marko", "milos"]
dobitnici = korisnici[0:101]
print(dobitnici)

korisnici.sort()
print(korisnici)

brojevi = [5, 2, 1, 4, 7]