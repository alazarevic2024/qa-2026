public class Korisnik {
    public String korisnickoIme;
    public String sifra;
    public String smer;
    public int godinaUpisa;
    private int krediti;

    public static String ustanova = "ITAcademy";

    public Korisnik(String korisnickoIme, String sifra, String smer, int godinaUpisa) {
        this.korisnickoIme = korisnickoIme;
        this.sifra = sifra;
        this.smer = smer;
        this.godinaUpisa = godinaUpisa;
    }

    @Override
    public String toString() {
        return "Korisnik: " + this.korisnickoIme + " smer: " + this.smer;
    }

    public int prikaziKredite() {
        return this.krediti;
    }

    public void dodeliKredite(int osvojeniKrediti) {
        this.krediti += osvojeniKrediti;
    }
}
