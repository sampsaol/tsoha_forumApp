
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

## Lopullinen toiminnallisuus

Sovelluksessa voit luoda oman käyttäjän tai kirjautua sisään luodulle käyttäjälle. Aloitusnäytöllä näet luodut keskusteluketjut ja niihin liittyvää tietoa. Voit luoda omia keskusteluketjuja ja siirtyä niihin katsomaan ketjuun lähetettyjä viestejä. Voit myös lisätä omia viestejä ketjuun. Ketjuissa olevista viesteistä voi tykätä. Voit luoda uusia kategorioita ketjuille ja voit katsoa vanhoja jo luotuja kategorioita. Sovellus toimii vain paikallisesti eikä sitä ole jaettu fly.io palveluun. Sovelluksessa ei pitäisi olla haavoittuvaisuuksia, en löytänyt CSRF-haavoittuvaisuutta, jota en olisi korjannut.. Sovelluksessa voi mielekkäästi navigoida eri sivujen välillä ja sovelluksen käyttäjäystävällisyyttä parannettu.

## Kuvaus

Kyseessä on keskustelusovellus, jossa on eri keskusteluketjuja joita voi luoda itse ja joihin voi lisätä viestejä. Sovelluksessa on vain peruskäyttäjiä.
Sovelluksessa voi tykätä omista ja muiden viesteistä (1 tykkäys per viesti).  Keskusteluketjuille tulee määritellä keskusteluketjun kategoria, esimerkiksi urheilu, ruoka tai koulu. Kyseessä on siis ns. foorumi.

## Perusominaisuudet

* Käyttäjä voi luoda uuden käyttäjän tai kirjautua omalle käyttäjälleen (toteutettu)
* Käyttäjä voi luoda keskusteluketjuja ja lisätä viestejä keskusteluketjuihin (toteutettu)
* Keskusteluketjussa näkyy ketjun otsikko, viimeisen viestin lähetysaika ja sisältö (toteutettu)
* Käyttäjä voi luoda uusia kategorioita ja nähdä jo luodut kategoriat
* Käyttäjä voi tykätä viesteistä

