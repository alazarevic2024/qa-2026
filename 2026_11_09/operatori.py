email_u_bazi = "korisnik@gmail.com"
sifra_u_bazi = "1234"
# ----------------------------------
uneti_email = "korisnik@gmail.com"
uneta_sifra = "1234"

print(email_u_bazi == uneti_email) # True / False  - bool
print(sifra_u_bazi == uneta_sifra) # True / False  - bool

#operator and
print(email_u_bazi == uneti_email and sifra_u_bazi == uneta_sifra)

# operator or
# dozvoliti korisniku da ide dalje ako je uneo barem jedno od ova dva - email ili telefon
korisnikov_telefon = "0641231234"
korisnikov_email = "gfgdf@gmail.com"

# korisnik moze dalje ako je jedno od ova 2 stringa razlicito od ""
print(korisnikov_telefon != "" or korisnikov_email != "")

# operator not    
korisnik_ukljucio_notifikacije = True
korisnik_ukljucio_notifikacije = not korisnik_ukljucio_notifikacije # True -> False

# binarna vrednost
broj = 10 # int
print(bin(broj))
