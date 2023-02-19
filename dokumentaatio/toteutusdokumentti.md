# Toteutusdokumentti (keskeneräinen)

## Huffmanin algoritmi

Huffmanin tiedontiivistysalgoritmiin perustuva ohjelma ottaa .txt-muotoisen tiedoston ja pakkaa ja purkaa sen. Toistaiseksi ohjelma suorittaa sekä pakkaamisen että purkamisen yhdellä kerralla.
Tähän tulee mahdollisesti muutoksia.

Yleisesti tässä toteutuksessa algoritmin kompressointiosa toimii niin, että se:
1. Luo frekvenssitaulun tiedoston merkeille eli laskee kuinka monesti merkki ilmenee tiedostossa
2. Luo minimipinon, eli pienimmän frekvenssin merkki on pinossa päällimäisenä. Merkeistä frekvensseineen luodaan solmuja.
3. Luo huffmanin puun:
  - minimipinon pienimmät solmut "mergetään" yhdeksi solmuksi laskemalla niiden frekvenssit yhteen niin kauan, että minimipinossa on enää yksi solmu jäljellä. Kahdesta mergetystä tulee aina mergetyn solmun lapsia.
4. Puussa oleville solmuille annetaan binäärimuotoiset koodit (merkkeinä nollia ja ykkösiä). Kunkin merkin koodit tallennetaan python-sanakirjaan.
5. Alkuperäinen teksti kirjoitetaan koodeilla ja siihen lisätään ylimääräisiä bittejä, jotta se olisi kahdeksalla jaollinen.
6. Kahdeksalla jaollinen koodattu merkkijono muutetaan tavuiksi.
7. Tavut kirjoitetaan kompresoiduksi tiedostoksi.

...ja dekompressointiosa toimii niin, että se:
1. Tavuesitys haetaan kompressoidusta tiedostosta.
2. Siitä poistetaan ylimääräiset bitit.
3. Koodi puretaan sanakirjan avulla alkuperäiseksi merkkijonoksi.
4. Merkkijono tallennetaan tiedostoon.



## LZ77-algoritmi

LZ77-tiedontiivistysalgoritmiin perustuva ohjelma ottaa .txt-muotoisen tiedoston ja pakkaa sen. Ohjelmaan lisätään lähiviikkoina myös dekompressointiominaisuus. 

Ohjelman toteuttama kompressointi yksinkertaistettuna:
1. Tekstitiedoston sisältö tallennetaan merkkijonona.
2. Merkkijonoa aletaan käydä läpi kahden erilaisen "ikkunan avulla". Nämä ovat suurempi etsintäikkuna ja pienempi edessäkulkevaikkuna.
3. Edessäkulkeva ikkuna tarkastaa, onko etsintäikkunassa tismalleen samaa merkkiä (jos edessäkulkevassa on vain yksi merkki) tai samaa osamerkkijonoa (jos siinä on useampi merkki).
4. Jos "match" löytyy, niin silloin tupleen tallennetaan tieto siitä, mistä indeksistä match alkaa ja kuinka pitkä matchin pituus on.
5. Jos matchia ei löydy, niin silloin tupleen tallennetaan se merkki, jolle matchia ei löytynyt.
6. Tuplet tallennetaan listaan.
7. Alkuperäisen tiedoston merkkijonoa aletaan siis käymään merkkijono kerrallaan läpi, ja jos merkille ei löytynyt ikkuinoista matchia, listaan tallenetaan tieto merkistä.
8. Jos match löytyy, tarkastetaan vielä seuraavatkin merkit "mätsäävätkö" ne ja kaikista pisin mätsäävä pätkä tallennetaan tupleen kohdassa 4 mainitulla tavalla. 
9. Tuplelistan tiedot muutetaan biteiksi ja edelleen tavuiksi, jotka tallennetaan .bin-tiedostoon. Tämä on ohjelman tuottama kompressoitu tiedosto.


