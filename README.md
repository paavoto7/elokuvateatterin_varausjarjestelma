# Elokuvateatterin varausjärjestelmä

## Kuvaus

Tämä työ toteutettiin osana ohjelmoinnin harjoitustyö -kurssia ja sen aiheena
oli elokuvateatterin varausjärjestelmä.  
Työssä tuli tehdä Pythonin avulla järjestelmä, jolla asiakas voi varata paikkoja
näytöksiin. Näytöksia tuli olla monia päivässä ja saleja tuli olla useita eri kokoisia.

## Ratkaisuperiaate

Mietin erilaisia lähestymistapoja ratkaisuun, mutta päädyin vain pelkkiin tavallisiin funktioihin.  
Tietojen tallentaminen tuotti suurimman päänvaivan, kun piti päättää csv:n ja json:in välillä.  
Päädyin saleja sisällä pitävässä tiedostossa json:iin. Tämä ratkaisu saattoi paikoin tehdä koodista
jokseenkin huonoa.

Ohjelmassa on kirjautumisjärjestelmä, jonka avulla erotellaan käyttäjänäkymä ja hallintanäkymä.

## Funktioiden käyttö

