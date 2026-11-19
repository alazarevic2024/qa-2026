odabrani_smerovi = ["QA", "Python", "Java"] # lista
odabrani_smerovi.append("QA")
print(odabrani_smerovi)

odabrani_smerovi1 = {"QA", "Python", "Java"} # skup
odabrani_smerovi1.add("QA")
odabrani_smerovi1.add("Android")
print(odabrani_smerovi1)

for smer in odabrani_smerovi1:
    print(smer)