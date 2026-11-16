# opseg brojeva od 0 do 10
trazeni_broj = 20

for x in range(10):
    print("pretraga brojeva...")
    if x == trazeni_broj:
        print("Broj je pronadjen")
        break
else:
    print("Broj nije pronadjen")