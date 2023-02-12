# Viikkoraportti 4

Tällä viikolla olen jatkanut Huffmanin algoritmin toteutusta. Nyt ohjelmalla voi sekä pakata että purkaa .txt-muotoisen tiedoston. Toistaiseksi ohjelma tekee molemmat toiminnot, sekä pakkaamisen että purkamisen, samalla kertaa.

Huffmanin algoritmiin liittyy paljon eri funktioita, joten koodin selvyyden parantamiseksi järjestin funktioita eri moduuleihin. Tämä oli haastavaa, minut yllätti mm. circular import -error, ja minun piti kokeilla tähän erilaisia "kikkoja". Tällä hetkellä HuffmanCodingDecompress-luokka perii HuffmanCodingCompress-luokan, joka perii HuffmanCodingInitial-luokan.
Tästä syystä myös HuffmanDecompress "joutuu ottamaan" parametrinä tekstitiedoston polun, vaikka se ei sitä tarvitse. Luulen, että tähän löytyy ratkaisu ajan kanssa.

Haastetta oli myös käyttöliittymän ajamisessa komentoriviltä. Käyttöliittymän skripti oli src/huffman nimisessä kansiossa, eikä komento poetry run src/huffman/ui_huffman.py toiminut. Tämän selvittämisessä meni aikaa. Ongelma ratkesi nyt ainakin sillä, että siirsin ui_huffman.py-tiedoston suoraan src-kansion alle.

Tällä viikolla yritin tehdä myös aikaisempia viikkoja parempia testejä. Loin isohkon "siansaksa"-tiedoston, johon pystyin itse määrittämään merkit ja niiden frekvenssit. Näin ollen pystyin testaamaan funktioita isolla tiedostolla.
Kun ohjelman toiminnallisuus alkoi olla valmis, niin pystyin kokeilemaan end-to-end -testausta englanninkielisen kalevala.txt-tiedoston avulla.

### Seuraava viikko

Seuravaalla viikolla siirryn LZ77-algoritmin pariin.

Käytetty aika: 25 tuntia
