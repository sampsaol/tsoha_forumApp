
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

Sovelluksen tämänhetkisessä tilassa voit luoda oman käyttäjän tai kirjautua sisään luodulle käyttäjälle. Aloitusnäytöllä näet luodut keskusteluketjut ja niihin liittyvää tietoa. Voit luoda omia keskusteluketjuja ja siirtyä niihin katsomaan ketjuun lähetettyjä viestejä ja voit myös lisätä omia viestejä ketjuun. Tällä hetkellä on vain peruskäyttäjiä ja ketjuja tai viestejä ei voi muokata eikä poistaa. Sovellus toimii vain paikallisesti eikä sitä ole jaettu fly.io palveluun. Sovelluksen tietoturvaa on korjattu ja sovelluksesta tehty mukavempi käyttää. Sovelluksesta puuttuu vielä olennaista toiminnallisuutta ja ulkonäköä tulee korjata.

## Kuvaus

Kyseessä on keskustelusovellus, jossa on eri keskusteluketjuja joita voi luoda itse ja joihin voi lisätä viestejä. Sovelluksen käyttäjätyypit ovat peruskäyttäjä ja ylläpitäjä (tällä hetkellä vain peruskäyttäjä).
Sovelluksessa voi muokata ja poistaa omia viestejä ja keskusteluketjuja (toiminnallisuus kehitteillä vielä). Ylläpitäjä voi myös muokata ja/tai poistaa viestejä. Keskusteluketjuille tulee määritellä keskusteluketjun tyyppi,
esimerkiksi urheilu, ruoka tai koulu. Kyseessä on siis ns. foorumi.

## Perusominaisuudet

* Käyttäjä voi luoda uuden käyttäjän tai kirjautua omalle käyttäjälleen (toteutettu)
* Käyttäjä voi luoda keskusteluketjuja ja lisätä viestejä keskusteluketjuihin (toteutettu)
* Käyttäjä voi muokata tai poistaa luomiaan keskustelujketjuja tai viestejä (kesken)
* Ylläpitäjä voi muokata tai poistaa kaikkia keskusteluketjuja tai viestejä (kesken)
* Käyttäjä voi hakea viestejä sanan perusteella (kesken)
* Käyttäjä voi hakea keskusteluketjuja aiheen eli ketjun tyypin perusteella (kesken)
* Keskusteluketjussa näkyy ketjun otsikko, viimeisen viestin lähetysaika ja sisältö (toteutettu)

