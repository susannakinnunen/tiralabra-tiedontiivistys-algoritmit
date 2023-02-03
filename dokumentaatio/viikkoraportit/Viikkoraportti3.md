## Viikkoraportti 3

Tällä viikolla olen työskennellyt Huffmanin algoritmin parissa. Olen toteuttanut tiedoston kompressointiin liittyviä funktioita, ja tällä hetkellä koodi on sellaisessa vaiheessa, että sillä voi pakata tekstitiedoston.

Olen oppinut, kuinka Huffmanin puu toteutetaan, ja kuinka sen avulla pystytään antamaan puussa oleville lehdille (esim. tekstin merkeille) binäärikoodeja. Alkuperäisen tiedoston merkit muutetaan binäärikoodeiksi ja siitä saatu binäärimerkkijono muutetaan tavuiksi. Kun tavut tallenetaan tiedostoon, saadaan alkuperäinen tiedosto pakatussa muodossa.

Haastetta tuotti erityisesti se, mitä sen jälkeen tehdään, kun merkkijono on käännetty bittimerkkijonoksi. Toisin sanoen, kuinka binäärimerkkijonosta saadaan tiivistetty tiedosto. Löysin tietoa, että bittimerkkijonot tallennetaan tavuina. Tässä täytyi ottaa monia asioita huomioon. Koska binäärimerkkijono ei ole aina kahdeksalla jaollinen tavujakoa varten, siihen tuli lisätä extrabittejä ja niiden määrästä tuli myös lisätä informaatiota tavujonoon.

Seuraavaksi alan tekemään tiivistetyn tiedoston purkamiseen liittyviä toimintoja ja siirryn myös lz77-algoritmin pariin.
Tavoitteenani on myös tehdä HuffmanCoding-ohjelmasta ja siihen liittyvästä tesatuksesta selkeämpää. Ohjelmassa ei ole tällä hetkellä käyttöliittymää, vain debuggaus-mielessä rakennettu tulostusrunko koodin alaosassa. Kaikki funktiot on myöskin ajettava erikseen läpi. Tällä hetkellä TestHuffmanCoding-luokassa useassa yksittäisessä testifunktiossa tehdään alussa samat toimenpiteet luultavasti ainakin osittain turhaan. Tavoitteenani on käydä testit läpi ja tarkistaa, mitä alkutoimenpiteistä kannattaa laittaa def setUpiin. Siinä muutamia asioita, joita pyrin muuttamaan tulevina viikkoina.

Käytetty aika tällä viikolla: 16 tuntia