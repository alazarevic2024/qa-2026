//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {
    int broj1; // deklaracija
    broj1 = 5; // inicijalizacija

    int broj = 10; // deklaracija i inicijalizacija

    String poruka = "Hello";

    System.out.println(broj);
    System.out.println(poruka);

    Korisnik korisnik1 = new Korisnik("jovana", "123", "QA", 2025);
    Korisnik korisnik2 = new Korisnik("marko", "543", "Python", 2026);
    Korisnik korisnik3 = new Korisnik("marija", "111", "QA", 2026);

    System.out.println(korisnik1.korisnickoIme);
    System.out.println(korisnik1.toString());

    korisnik1.smer = "Android";

    System.out.println(korisnik1.prikaziKredite());
    korisnik1.dodeliKredite(50);
    System.out.println(korisnik1.prikaziKredite());
}