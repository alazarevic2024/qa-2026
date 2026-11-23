korisnik_lista = ["probni_korisnik", "123", "QA", 2026, "ITAcademy", 0]
korisnik_recnik = {"korisnicko_ime":"probni_korisnik", "sifra":"123", "smer":"QA"}

class Korisnik:
    korisnicko_ime = ""
    sifra = ""
    smer = ""
    godina_upisa = 0
    krediti  = 0
    ustanova = "ITAcademy"

    def __init__(self, korisnicko_ime, sifra, smer, godina_upisa, krediti=0): # inicijalizator / konstruktor
        print("Kreiram objekat klase korisnik!")
        self.korisnicko_ime = korisnicko_ime
        self.sifra = sifra
        self.smer = smer
        self.godina_upisa = godina_upisa
        self.krediti = krediti

    def promeni_smer(self, novi_smer):
        self.smer = novi_smer
        print(f"Korisnik {self.korisnicko_ime} je promenio smer na {self.smer}")

    def __str__(self):
        return f"Ovo je instanca klase Korisnik, sa korisnickim imenom {self.korisnicko_ime}"

    def dodeli_kredite(self, osvojeni_krediti):
        self.krediti += osvojeni_krediti
    

korisnik1 = Korisnik("marko", "123", "Python", 2025)
print(korisnik1.korisnicko_ime, korisnik1.smer, korisnik1.godina_upisa)

korisnik1.smer = "QA"
print(korisnik1.korisnicko_ime, korisnik1.smer, korisnik1.godina_upisa)

korisnik2 = Korisnik("petar", "543", "QA", 2026)
korisnik3 = Korisnik("marija", "123", "Java", 2026)

lista_korisnika = [korisnik1, korisnik2, korisnik3]
for korisnik in lista_korisnika:
    if korisnik.godina_upisa == 2026 and korisnik.smer == "QA":
        print("Ocekivano - 2026 QA")
    else:
        print(f"Greska - korisnik {korisnik.korisnicko_ime} je smer {korisnik.smer} a generacija: {korisnik.godina_upisa}")

# promeni_smer() - ne moze - pripada klasi korisnik, zahteva njen objekat
korisnik1.promeni_smer("iOS")
print(korisnik1.smer)

print(korisnik1)
print(korisnik1.krediti)
korisnik1.dodeli_kredite(50)
print(korisnik1.krediti)