
# Keskustelusovellus

## Käyttöohjeet

Kloonaa tämä repositorio tietokoneellesei ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi
```bash
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

<code>
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
</code>
<br>
Määritä tietokannan skeema komennolla

<code>
$ psql < schema.sql
</code>
<br>
Voit käynnistää sovelluksen komennolla

<code>
$ flask run
</code>

## Nykyinen toiminnallisuus

Sovelluksen tämänhetkisessä tilassa voit luoda oman käyttäjän tai kirjautua sisään luodulle käyttäjälle. Aloitusnäytöllä näet luodut keskusteluketjut ja niihin liittyvää tietoa. Voit luoda omia keskusteluketjuja ja siirtyä niihin katsomaan ketjuun lähetettyjä viestejä ja voit myös lisätä omia viestejä ketjuun. Tällä hetkellä on vain peruskäyttäjiä ja ketjuja tai viestejä ei voi muokata eikä poistaa. Sovellus toimii vain paikallisesti eikä sitä ole jaettu fly.io palveluun. Sovelluksen tietoturva on vielä tietyin osin puutteellinen, mutta se tulee päivittymään.

## Kuvaus

Kyseessä on keskustelusovellus, jossa on eri keskusteluketjuja joita voi luoda itse ja joihin voi lisätä viestejä. Sovelluksen käyttäjätyypit ovat peruskäyttäjä ja ylläpitäjä.
Sovelluksessa voi muokata ja poistaa omia viestejä ja keskusteluketjuja. Ylläpitäjä voi myös muokata ja/tai poistaa viestejä. Keskusteluketjuille tulee määritellä keskusteluketjun tyyppi,
esimerkiksi urheilu, ruoka tai koulu. Kyseessä on siis ns. foorumi.

## Perusominaisuudet

* Käyttäjä voi luoda uuden käyttäjän tai kirjautua omalle käyttäjälleen
* Käyttäjä voi luoda keskusteluketjuja ja lisätä viestejä keskusteluketjuihin
* Käyttäjä voi muokata tai poistaa luomiaan keskustelujketjuja tai viestejä
* Ylläpitäjä voi muokata tai poistaa kaikkia keskusteluketjuja tai viestejä
* Käyttäjä voi hakea viestejä sanan perusteella
* Käyttäjä voi hakea keskusteluketjuja aiheen eli ketjun tyypin perusteella
* Keskusteluketjussa näkyy ketjun otsikko, viimeisen viestin lähetysaika ja sisältö

