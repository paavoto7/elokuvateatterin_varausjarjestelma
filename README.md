# Elokuvateatterin varausjärjestelmä

## Kuvaus

Tämä työ toteutettiin osana Turun Yliopiston ohjelmoinnin harjoitustyö -kurssia ja sen aiheena
oli elokuvateatterin varausjärjestelmä.  
Työssä tuli tehdä Pythonin avulla järjestelmä, jolla asiakas voi varata paikkoja
näytöksiin. Näytöksia tuli olla monia päivässä ja saleja tuli olla useita eri kokoisia.

Työ venyi kokonaisuudessaan yli 300 riviä pitkäksi kommentit ja tyhjät rivit mukaanlukien.
Optimointia ja koodin rakenteen parantelua ei ole turhan paljoa tehty rajallisen ajan vuoksi.

### Disclaimer
Kirjautumisjärjetelmä on tehty ainoastaan mockup-mielessä.
Tästä syystä kaikki on tarkoituksella tallennettu plain textinä.

## Käyttö

Kun ohjelman käynnistää, se kysyy haluaako käyttäjä kirjautua vai rekisteröityä.  
Tämän jälkeen itse varausjärjestelmä käynnistyy joko käyttäjä- tai ylläpitäjätilaan riippuen käyttäjästä.  

Asiakasnäkymässä voi ainoastaan varata paikan valitsemaansa näytökseen.  
Salia varatessa tulee syöttää salin edessä oleva järjestysnumero.

Ylläpitäjällä on oma käyttöliittymänsä, jossa se hallita järjestelmää.  
Se voi:
1. Lisätä salin
2. Lisätä elokuvan
3. Poistaa elokuvan
4. Nähdä asiakkaiden varaukset
5. Nähdä pyörimässä olevat elokuvat
6. Poistua

Ylläpitäjätilassa tulee olla tarkempi syötön kanssa.  
Salin nimi ja elokuvan tulee esimerkiksi elokuvaa poistaessa antaa merkilleen oikein.

## Ratkaisuperiaate

Mietin erilaisia lähestymistapoja ratkaisuun, mutta päädyin vain pelkkiin tavallisiin funktioihin.  
En lähtenyt olio-pohjaisella ratkaisulla etenemään, vaikka sitäkin pohdin.
Tietojen tallentaminen tuotti suurimman päänvaivan, kun piti päättää csv:n ja json:in välillä.  
Päädyin saleja sisällä pitävässä tiedostossa json:iin. Tämä ratkaisu saattoi paikoin tehdä koodista jokseenkin huonoa ja pitkää.

Kirjautumisjärjestelmä käyttää *credidentials.csv* tiedostoa kirjautumistietojen tallentamiseen.
Salasanoja ei ole salattu, koska en nähnyt sille tarvetta tässä työssä.

Ohjelma on jaettu kahteen tiedostoon, joista toisessa on kaikki itse varausjärjestelmään
liittyvä funktionaalisuus. Toisessa on taas kaikki kirjautumisjärjestelmään liittyvä.

Ohjelmassa on kirjautumisjärjestelmä, jonka avulla erotellaan käyttäjänäkymä ja hallintanäkymä.  
Hallintanäkymän saa syöttämällä käyttäjänimeksi sekä salasanaksi **admin**.

## Funktioiden käyttö

Ohjelmassa on *main* funktio, joka kutsuu muita funktioita.  
Kaikki erilliset funktionaaliset osat on pyritty parhaan mukaan jakamaan omiin funktioihin.  
Muutamassa funktiossa on yhdistetty asioita toiston vähentämiseksi.

**movie.py:**
- main
    - Käyttöliittymä sekä funktioiden kutsuminen
- reservation
    - Asiakkaan paikan varaus
- load_data
    - Lataa salit muistiin
- add_cinema
    - Salin lisäykseen
- movie_mod
    - Jossain salissa pyörivän elokuvan lisäämiseen tai poistamiseen
- write_data
    - Muutettujen tietojen tallentamiseen
- load_movies
    - Elokuvakatalogissa olevien elokuvien tulostaminen tai sinne lisääminen
- print_playing
    - Tulostaa saleissa pyörivät elokuvat
- populate
    - Täyttää salin lisäyksen yhteydessä ohjelman elokuvilla hydöyntäen satunnaisuutta

**account_system.py:**
- register
    - Rekisteröityminen
- login
    - Kirjautuminen
- update_reservation
    - Päivittää asiakkaan varauksen
- print_reservation
    - Tulostaa asiakkaiden varaukset moderaattorille

## Kirjastojen käyttö

Työssä käytettiin useita *Pythonin Standard Libraryyn* kuuluvia kirjastoja.

Itse työssä ei ole käytetty yhtään ulkoisia kirjastoja, vaikka se olisi saattanut olla kannattavaa.
Suosittu kirjasto **tabulate** olisi tehnyt printtauksesta huomattavasti paremman näköistä.

Toinen mahdollinen vaihtoehto olisi voinut olla jokin kirjasto, joka muuttaisi jsonin tasaiseksi.
Tämän voisi itsekin tehdä, mutta päädyin nykyiseen ratkaisuun, jotta kirjoittaminen onnistui suoraan.

Työn koodia formatoitiin käyttämällä työkalua nimeltä [Black](https://pypi.org/project/black/).
