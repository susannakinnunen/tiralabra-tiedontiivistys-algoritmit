# Toteutusdokumentti

## Yleisrakenne

### Huffmanin algoritmi

***Huffmanin häviöttömään tiedontiivistysalgoritmiin perustuva ohjelma ottaa .txt-muotoisen tiedoston, jonka se pakkaa ja purkaa. Ohjelma suorittaa sekä pakkaamisen että purkamisen yhdellä kerralla.***

***Algoritmiin kuuluu oleellisesti minimipino ja Huffmanin puu -tietorakenteet.***

Tässä toteutuksessa algoritmin kompressointiosa toimii niin, että se:
1. Luo frekvenssitaulun tiedoston merkeille, eli se laskee kunkin merkin lukumäärän.
2. Luo minimipinon, eli pienimmän frekvenssin merkki on pinossa päällimäisenä. Merkeistä frekvensseineen luodaan solmuja.
3. Luo huffmanin puun:
  - minimipinon kaksi pienintä solmua "mergetään" yhdeksi solmuksi laskemalla niiden frekvenssit yhteen niin kauan, että minimipinossa on enää yksi solmu jäljellä. Kahdesta mergetystä tulee aina uuden solmun lapsia.
4. Puussa oleville solmuille annetaan binäärimuotoiset koodit (merkkeinä nollia ja ykkösiä). Kunkin merkin koodit tallennetaan python-sanakirjaan.
5. Alkuperäinen teksti kirjoitetaan koodeilla ja siihen lisätään ylimääräisiä bittejä, jotta se olisi kahdeksalla jaollinen.
6. Kahdeksalla jaollinen koodattu merkkijono muutetaan tavuiksi.
7. Tavut kirjoitetaan kompresoiduksi tiedostoksi.

...ja dekompressointiosa toimii niin, että se:
1. Tavuesitys haetaan kompressoidusta tiedostosta.
2. Siitä poistetaan ylimääräiset bitit.
3. Koodi puretaan sanakirjan avulla alkuperäiseksi merkkijonoksi.
4. Merkkijono tallennetaan tiedostoon.



### LZ77-algoritmi

***Häviöttömään LZ77-tiedontiivistysalgoritmiin perustuva ohjelma ottaa .txt-muotoisen tiedoston, jonka se pakkaa ja purkaa. Ohjelma suorittaa sekä pakkaamisen että purkamisen yhdellä kerralla.***

***Ohjelma käy läpi tekstitiedoston sisältöä kahden ikkunan avulla yhtäaikaa. Ikkunat on nimetty etsintäikkunaksi (search window) ja edelläkulkevaksi ikkunaksi (lookahead window). Kompressoituun tiedstoon on tallennettuna (distance, length, character)-tupleja. Tupleissa on joko character, eli merkki tai siinä annetaan "koordinaatit" merkin/merkkijonon sijaintiin tekstissä. Distance eli etäisyys neuvoo, kuinka kaukana merkki on ja length eli pituus kertoo merkkijonon pituuden.***

Ohjelman toteuttama kompressointi:
1. Tekstitiedoston sisältö tallennetaan merkkijonona.
2. Merkkijonoa aletaan käydä läpi kahden erilaisen "ikkunan avulla". Nämä ovat suurempi etsintäikkuna ja pienempi edessäkulkeva ikkuna.
3. Ohjelma tarkistaa, löytyykö etsintäikkunasta edelläkulkevassa ikkunassa näkyvää merkkijonoa. 
4. Jos "match" löytyy, niin silloin tupleen tallennetaan tieto siitä, mistä indeksistä match alkaa ja kuinka pitkä matchin pituus on.
5. Jos matchia ei löydy, niin silloin tupleen tallennetaan se merkki, jolle matchia ei löytynyt.
6. Tuplet tallennetaan listaan.

Yhteenvetoa tähän astisesta ja loppuosa:
7. Alkuperäisen tiedoston merkkijonoa aletaan käydä merkkijono kerrallaan läpi, ja jos merkille ei löytynyt ikkuinoista matchia, listaan tallenetaan tieto merkistä.
8. Jos match löytyy, tarkastetaan vielä seuraavatkin merkit "mätsäävätkö" ne ja kaikista pisin mätsäävä pätkä tallennetaan tupleen kohdassa 4 mainitulla tavalla. 
9. Tuplelistan tiedot muutetaan biteiksi ja edelleen tavuiksi, jotka tallennetaan .bin-tiedostoon. Tämä on ohjelman tuottama kompressoitu tiedosto.

Dekompressointi:
1. Binäärimuodossa oleva tiedosto muutetaan bittimerkkijonoksi.
2. Tämä merkkijono muutetaan takaisin tuplelistaksi.
3. Tuplelistan tietoja käytetään hyödyksi alkuperäisen tekstin uudelleen kirjoittamisessa. Tuplet käydään läpi listan järjestyksessä. Jos tuplessa on merkki se kirjoitetaan ylös alussa tyhjänä olevaan merkkijonoon. Tästä merkkijonosta muodostuu alkuperäisen tiedoston sisältö. Jos tuplessa ei ole merkkiä, se tarkoittaa, että siinä on tiedot "matchista" eli merkkijono löytyy jo kirjoitetusta tekstistä. Tässä tuplessa olevien tietojen avulla (kuinka kaukana ensimmäinen merkki on ja merkkijonon pituus) kyseinen merkkijono haetaan jo kirjoitetusta tekstistä. Tähän jo kirjoitettuun merkkijonoon lisätään haettu osamerkkijono.
4. Merkkijono kirjoitetaan .txt-tiedostoon.

## Suorituskyvyn vertailu

Tässä osiossa vertailllaan Huffmanin ja LZ77 algoritmien suorituskykyä 497.6 kilotavun kokoisen tiedoston pakkaamisessa ja purkamisessa.
Tämän lisäksi vertaillaan molempien algoritmien tuottamaa kompressoitua tiedostoa, kun kompressoitavana on 2.9 megatavun kokoinen tiedosto. Ohjeet näiden suorituskykytestien ajamiseen löytyvät testausdokumentista. 

Huffmanin algoritmi:
- pakkaaminen
  - aika keskimäärin: 0.5 sekuntia
  - pakatun tiedoston koko: 285.7 kB eli 57 % alkuperäisestä tiedostokoosta
 - purkaminen
    - aika keskimäärin: 1.3 sekuntia
 
 LZ77-algoritmi:
 - pakkaaminen
    - aika: eri kerroilla 50-80 sekuntia
    - pakatun tiedoston koko: 347.5 kB eli n. 70% alkuperäisestä tiedostokoosta
 - purkaminen
    - aika: 0.596 sekuntia

LZ77-algortimi siis pakkaa huomattavasti hitaammin ja pakattu tiedosto on suurempi kuin Huffmanin algoritmilla pakattu.

Alla olevasta kuvasta näemme, että LZ77-algoritmin funktio convert_into_bit_string vie yli 45 sekuntia aikaa (kokonaisaika 47 sekuntia). Tässä funktiossa käsitellään listaa, jossa on tupleja, joista löytyy alkuperäisen tekstitiedoston merkit ja niiden "matchit". Jokainen tuple muutetaan kahdeksalla jaollisiin bittijonoihin.

Tiedostosta tulee myös kovin suuri, sillä jokaiselle merkille varataan 15 bittiä, jotta suurin osa Extented ASCII-tauluun merkityistä merkeistä voidaan muuttaa bittijonoksi. Perinteisen ASCII-taulun merkeille tarvitsisi varata vain 8 bittiä, jolloin tiedoston kokoa saisi pienennettyä. (lähde: https://www.asciitable.com/#google_vignette)

#### 2.9 MB tiedoston pakkaaminen

Kun kyseessä on on liki 3 megatavun tiedosto, molemmat algoritmit pakkaavat tiedoston yhtä pieniksi. Kompressoidun tiedosto on n. 54% alkuperäisen tiedoston koosta. Huffmanin algoritmi on kuitenkin ylivoimaisesti nopeampi. Siinä menee aikaa n. 5 sekuntia, kun taas LZ77-algoritmin kompressointi vie reilu 6 minuuttia.

#### Kuvat suorituskykytestauksesta 497.6 kilotavun tiedosto

**Huffman kompressointi**

![Huffman kompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/vol%202%20huffman%20compress%202023-03-02%2015-23-40.png)

**Huffman dekompressointi**

![Huffman dekompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/vol%202%20huffman%20decompress%202023-03-02%2015-26-12.png)

**LZ77 kompressointi**

![LZ77 kompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/lz77%20compression%202023-02-25%2014-27-47.png)

**LZ77 dekompressointi**

![LZ77 dekompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/lz77%202023-02-25%2014-33-11.png)


Taulukon sarakkeiden nimet viittaavat seuraaviin asioihin:

**ncalls**
- kutsujen määrä

**tottime**
- koko aika käytetty tähän funktioon, poislukien alifunktioiden kutsuissa mennyt aika

**percall**
- tottime ja ncalls jakolaskun osamäärä

**cumtime**
- kumulatiivinen aika käytetty kyseiseen funktioon ja sen alifunktioihin

**percall**
- cumtimen ja primitiivisten kutsujen (ei rekursiiviset kutsut) osamäärä

**filename:lineno(function)**
- funktion tiedot

lähde: https://docs.python.org/3/library/profile.html

## Puutteet
LZ77-algoritmiin perustuva ohjelma on hyvin hidas, ja se ei käännä kaikkia utf-8-koodattuja merkkejä. Tämä johtuu siitä, että kun merkki käännetään bittjonoksi, niin se saa vain 15 bittiä käytettäväkseen. Utf-8-koddattu merkki voi olla pisimmillään neljän tavun pituinen. lähde: https://en.wikipedia.org/wiki/UTF-8

Kuten suorituskykytestauksesta huomataan, bittijonoiksi kääntäminen vie suurimman osan ajasta. Tämä on hieman yllättävää, sillä voisi ajatella, että pisimmän saman merkkijonon etsiminen veisi eniten aikaa. 

LZ77-ohjelman pakkaaman tiedoston koko voisi olla pienempi testauksessa mukana olevan n. 500 kilotavun kohdalla.

### Aikavaativuus
Huffmanin algoritmin aikavaativuus on O(n log n), kun n on merkkien määrä. Lähde: https://en.wikipedia.org/wiki/Huffman_coding
LZ77-algoritmin aikavaativuus on O(n), kun n on merkkien määrä. Lähde: https://ieeexplore.ieee.org/document/1096485

### Kaikki lähteet koottuna:
https://www.programiz.com/dsa/huffman-coding
https://docs.python.org/3/library/profile.html
https://en.wikipedia.org/wiki/UTF-8
https://en.wikipedia.org/wiki/Huffman_coding
https://ieeexplore.ieee.org/document/1096485
