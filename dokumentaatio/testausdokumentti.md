# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

Yksikkötestauksen kattavuusraportti on löydettävissä täältä:
[![codecov](https://codecov.io/gh/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/branch/main/graph/badge.svg?token=KEMF99W3XG)](https://codecov.io/gh/susannakinnunen/tiralabra-tiedontiivistys-algoritmit)

Kuva testauksen kattavuusraportista 4.2. ja 12.2.:

![Testikattavuusraportti-kuva 4.2.](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/Coveragereport%20from%202023-02-04%2011-21-23.png)

![Testikattavuusraportti-kuva 12.2.](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/Coverage_report%20from%202023-02-12%2013-43-30.png)

## Mitä on testattu, miten tämä tehtiin?

Projekti koostuu kokonaisuudessaan kahdesta eri algoritmista, jotka ovat Huffman- ja LZ77 -tiedontiivistysalgoritmit. Tällä hetkellä Huffmanin algoritmiin perustuva ohjelma on lähes valmis ja LZ77-ohjelmaa ei ole vielä kunnolla aloitettu. 

Huffmanin algoritmiin perustuva ohjelma on testattu yksikkötestein pytest-kirjaston avulla. Ohjelman kaikki funktiot on testattu (paitsi käyttöliittymän eli ui_huffman.py-tiedoston sisältö). Ohjelman toimivuutta on myös testattu end-to-end -testauksella. Tämä tarkoittaa sitä, että testit tarkistavat onko alkuperäisen tekstitiedoston sisältö sama kuin dekompressoidun. Testit tarkistavat myös, että kompressoitutiedosto on kooltaan vähintään 40% pienenmpi kuin alkuperäinen.

## Minkälaisilla syötteillä testaus tehtiin?
Huffmanin algoritmin end-to-end -toiminnallisuutta sekä kompressoidun tiedoston pienemmyyttä on testattu englanninkielisellä Kalevalalla. Jo pelkästään näillä testeillä saadaan testattua kaikkia funktioita. Tämä testaaminen löytyy polusta src/tests/test_huffman_coding_kalevala.py.

Huffmania on myös testattu itseluodulla "siansaksa"-tiedostolla ja hyvin pienillä merkkijonoilla tiedostossa src/tests/test_huffman_coding_small_and_nonsense.py. Näitä testejä on tehty saman aikaisesti ohjelman kanssa. Vaikka näiden testien merkityksellisyys lopullisen ohjelman toimivuuden kannalta voi olla turhaa, niin niistä oli paljon apua yksittäisten funktioiden toimivuuden ja toiminnallisuuden selvittämisessä ohjelmaa tehdessä.

## Miten testit voidaan toistaa?
Testit voi toistaa komentorivillä menemällä ohjelman juurikansioon ja ajamalla koodin ```poetry run pytest src```.
