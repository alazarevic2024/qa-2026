    #        Ime        godine  verifikovan 
korisnik1 = ["Marko",      30,      True]
korisnik2 = ["Jovana",     35,      False]
korisnik3 = ["Ana",        28,       True]

korisnici = [
    #   0    1   2
    ["Marko",30,True], # 0
    ["Jovana",35,False], # 1
    ["Ana",28,True] # 2
 ]

print(korisnici[0][1])

# Tuple - sekvence
test_podaci = ["admin", "123", True] # lista
test_podaci1 = ("admin", "123", True) # tuple

test_podaci[0] = "admin111"
# test_podaci1[0] = "admin111" - nije moguca izmena u tuple

primer_lista = ["proba"]
primer_tuple = ("proba",)
print(type(primer_tuple))