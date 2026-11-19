#            0         1       2    4
korisnik = ["Ana", "Markovic", 25, True]
print(f"Ime: {korisnik[0]}\nPrezime: {korisnik[1]}")

korisnik1 = {"ime":"Ana", "prezime": "Markovic", "godine":25, "aktivan": True}
print(f"Ime: {korisnik1['ime']}, Prezime: {korisnik1['prezime']}")

# proizvodi = ["laptop", "mis", "tastatura", "monitor"]

    #       0         1         2
poruke = ["Hello", "Zdravo", "Hallo"]
poruke1 = {
    "en":"Hello", 
    "sr":"Zdravo", 
    "de":"Hallo"
}
print(poruke1["en"])

poruke1["sr"] = "Dobar dan"
print(poruke1)

poruke2 = {}

proizvod = {
    "naziv":"Laptop",
    "cena": {
        "vrednost":85000,  # proizvod["cena"]["vrednost"]
        "valuta":"RSD"
    },
    "dostupan": True,
    "kolicina":5,
    "slike":["laptop1.png", "laptop2.png"]
}
print(proizvod["naziv"])
print(proizvod["slike"])
print(proizvod["cena"])

info_o_ceni = proizvod["cena"]  # {'vrednost': 85000, 'valuta': 'RSD'}
print(info_o_ceni["vrednost"])
print(info_o_ceni["valuta"])

print(proizvod["cena"]["vrednost"])


proizvodi = [
    {
    "naziv":"Laptop",
    "cena": {
        "vrednost":85000,  # proizvod["cena"]["vrednost"]
        "valuta":"RSD"
    },
    "dostupan": True,
    "kolicina":5,
    "slike":["laptop1.png", "laptop2.png"]
},
{
    "naziv":"Monitor",
    "cena": {
        "vrednost":35000,  # proizvod["cena"]["vrednost"]
        "valuta":"RSD"
    },
    "dostupan": False,
    "kolicina": 0,
    "slike":["laptop1.png", "laptop2.png"]
},
{
    "naziv":"Mis",
    "cena": {
        "vrednost":5000,  # proizvod["cena"]["vrednost"]
        "valuta":"RSD"
    },
    "dostupan": True,
    "kolicina":4,
    "slike":["laptop1.png", "laptop2.png"]
}
]

for pr in proizvodi:
    print(f"Naziv: {pr["naziv"]}\nCena: {pr["cena"]["vrednost"]} {pr["cena"]["valuta"]}")
    if pr["dostupan"]:
        print("Proizvod je dostupan")
    else:
        print("Proizvod nije na stanju.")
    print()
    print("##########################")

poruke1 = {
    "engleski":"Hello", 
    "sr":"Zdravo", 
    "de":"Hallo"
}
# print(poruke1["en"])
print(poruke1.get("en"))
if poruke1.get("en") != None:
    print(poruke1["en"])
else:
    print("Kljuc en ne postoji")