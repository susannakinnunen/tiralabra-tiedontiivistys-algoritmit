# Toteutusdokumentti (keskeneräinen)

## Huffmanin algoritmi

Huffmanin tiedontiivistysalgoritmiin perustuva ohjelma ottaa .txt-muotoisen tiedoston ja pakkaa ja purkaa sen. Tällä hetkellä (12.2) ohjelma suorittaa sekä pakkaamisen että purkamisen yhdellä kerralla.
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

Toistaikseksi toteuttamatta. (12.2.)
