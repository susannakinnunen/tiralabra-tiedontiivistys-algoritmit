# Testausdokumentti

Sekä Huffman- että LZ77 -algoritmeja on testattu yksikkö- ja suorituskykytestein.

## Yksikkötestaus

### Yksikkötestauksen kattavuusraportti ja kuvat

Yksikkötestauksen kattavuusraportti on löydettävissä täältä:
[![codecov](https://codecov.io/gh/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/branch/main/graph/badge.svg?token=KEMF99W3XG)](https://codecov.io/gh/susannakinnunen/tiralabra-tiedontiivistys-algoritmit)

Kuva testauksen kattavuusraportista 2.3.:

![Testikattavuusraportti-kuva 2.3.](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/Coverage%20report%202023-03-02.png)


### Mitä on testattu, miten tämä tehtiin?

Projekti koostuu kokonaisuudessaan kahdesta eri algoritmista, jotka ovat Huffman- ja LZ77 -tiedontiivistysalgoritmit.

Molempia algoritmeja on testattu yksikkötestein pytest-kirjaston avulla. Pytest-kirjastoa on käytetty myös end-to-end -testauksessa. End-to-end -testit tarkastavat onko alkuperäisen tekstitiedoston sisältö sama kuin dekompressoidun.

Lisäksi algoritmien pakkaamien tiedostojen kokoja testataan ajamalla ohjelmat ja tarkistamalla, että niiden tuottamat pakatut tiedostot ovat niille annettujen ehtojen mukaiset (ehdot selitetty alhaalla tarkemmin).

### Minkälaisilla syötteillä testaus tehtiin?

Molempien algoritmien end-to-end -toiminnallisuutta sekä kompressoidun tiedoston pienemmyyttä on testattu englanninkielisellä Kalevalalla (tiedoston koko n. 500 kilotavua). Jo pelkästään näillä testeillä saadaan testattua molempien ohjelmien kaikkia funktioita. Nämä testit löytyvät poluista src/tests/test_huffman_coding_kalevala.py ja src/tests/test_lz77_kalevala.py.

Huffmanin algoritmia testataan myös isommalla (2.9 MB) itseluodulla tiedostolla ja hyvin pienillä merkkijonoilla tiedostossa src/tests/test_huffman_coding_small_and_nonsense.py. Näitä syötteitä käytetään yksittäisten funktioiden testaamiseen. Iso tiedosto koostuu tietyistä merkkejä, joten sitä oli helppo käyttää yksittäisten funktioiden palautusten oikeellisuuden tarkistamiseen. 

Yksikkötestejä on tehty saman aikaisesti ohjelmien kanssa. Näistä testeistä oli paljon hyötyä funktioiden toimivuuden ja toiminnallisuuksien selvittämisessä ohjelmaa tehdessä. LZ77-algoritmin yksittäisiä funktioita testaavat testit löytyvät test_lz77_small.py-tiedostosta. LZ77-algoritmin yksttäisiä funktioita on testattu vain pienillä merkkijonoilla, sillä sen testaaminen 2.9 megatavun tiedostolla vie paljon aikaa. Tätä isoa 2.9 MB tiedostoa käytetään LZ77-algoritmin suorituskykytestaamisessa.

Noin 500 kilotavun kokoisen tiedoston kompressoinnissa tarkastetaan, että Huffmanin algoritmin pakkaama tiedosto on vähintään 40 % alkuperäistä pienempi ja LZ77 algoritmin pakkaama vähintään 30 % pienempi.

Molempien algoritmien pakkaamien tiedostojen kokoja tarkastellaan myös 2.9 megatavun kokoisen tiedoston pakkaamisessa suorituskykytesteissä. Sen kohdalla molempien algoritmien pakkaman tiedoston tulee olla vähintään 40 % prosenttia pienempi.

### Miten testit voidaan toistaa?
Yksikkö- ja end-to-end -testit voi toistaa komentorivillä menemällä ohjelman juurikansioon ja ajamalla koodin ```poetry run pytest src```.

Huffmanin algoritmiin liittyvät testit voi ajaa juurikansiossa komentoriviltä kommennolla:

```poetry run python3 src/performance_test/huffman_performance.py```

ja LZ77-algoritmin komennolla:

```poetry run python3 src/performance_test/lz77_performance.py```

## Suorituskykytestaus

***Tarkempi suorituskykyvertailu löytyy toteutusdokumentista.***

Suorituskykytestausta on tehty Pythonin cProfile kirjaston avulla. 

Ensimmäisessä taulukossa on kompressointiin liittyvää statistiikkaa ja toisessa näytetään dekompressoinnin vastaavat mittaukset.

Syötteenä on n. 500 kilotavun kokoinen englanninkielinen Kalevala.

Ensimmäisellä rivillä lukee kuinka monta funktiokutsua on tehty ja missä ajassa.

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

### Suorituskykytestaus tulokset

**Huffman kompressointi**

![Huffman kompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/vol%202%20huffman%20compress%202023-03-02%2015-23-40.png)

**Huffman dekompressointi**

![Huffman dekompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/vol%202%20huffman%20decompress%202023-03-02%2015-26-12.png)

**LZ77 kompressointi**

![LZ77 kompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/lz77%20compression%202023-02-25%2014-27-47.png)

**LZ77 dekompressointi**

![LZ77 dekompressio suorituskyky kuva](https://github.com/susannakinnunen/tiralabra-tiedontiivistys-algoritmit/blob/main/dokumentaatio/kuvat/lz77%202023-02-25%2014-33-11.png)
