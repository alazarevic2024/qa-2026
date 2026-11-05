import random

broj_od_racunara = random.randint(1, 10)
broj_od_korisnika = int(input("Unesite ceo broj izmedju 1 i 10: "))

pogodak = broj_od_racunara == broj_od_korisnika  # Frue / False

print("Pogodak:", pogodak)
print(f"Vas broj: {broj_od_korisnika}, Racunar: {broj_od_racunara}")