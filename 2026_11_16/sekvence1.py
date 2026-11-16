# rezultati testova - promenljive
test1 = "PASS"
test2 = "FAIL"
test3 = "PASS"

print(test1)
print(test2)
print(test3)

# rezultati testova - lista 
lista_testova = ["PASS", "FAIL", "PASS"]


opseg = range(5, 10, 2)
print(opseg)
for x in opseg:
    print(x)

# string - sekvenca
   #      01234
poruka = "Hello"
# print(poruka[0])
# print(poruka[1])
# print(poruka[2])
# print(poruka[3])
# print(poruka[4])
         #0,1,2,3,4       
broj_karaktera = len(poruka) 
print("Broj karaktera u promenljivoj poruka je:", broj_karaktera)
for x in range(broj_karaktera):
    print(poruka[x])

poruka1 = "Hello World"
# print(poruka1[0])
# poruka1[0] = "C" - string nije mutabilan - nije moguce
print(type(poruka1))

korisnicko_ime = "testKorisnik"
print(korisnicko_ime.lower())
print(korisnicko_ime.upper())

ime = "marija"
prezime = "petrovic"
print(ime.capitalize())
print(prezime.capitalize())

lozinka = "   s i  f ra   "          
print(len(lozinka))

formatirana_lozinka = lozinka.strip()
formatirana_lozinka = formatirana_lozinka.replace(" ", "") # " " -> ""
print(formatirana_lozinka)
if len(formatirana_lozinka) >= 8:
    print("Duzina lozinke je odgovarajuca")
else:
    print("Lozinka je prekratka")

# Liste                     0         1       2         3 
registrovani_korisnici = ["marija", "ana", "petar", "jovana"]
# print(registrovani_korisnici[0])
# print(registrovani_korisnici[1])
for indeks in range(len(registrovani_korisnici)): # 0, 1, 2, 3
    print(registrovani_korisnici[indeks])

for korisnik in registrovani_korisnici:
    print(korisnik)

# dodavanje clanova u listu 
registrovani_korisnici.append("marko")
print(registrovani_korisnici)
# izmena korisnika
registrovani_korisnici[0] = "maja"
print(registrovani_korisnici)

registrovani_korisnici.remove("marko") # brisanje po vrednosti
print(registrovani_korisnici)

# brisanje po indeksu 
registrovani_korisnici.pop(0)
print(registrovani_korisnici)
del registrovani_korisnici[1]
print(registrovani_korisnici)