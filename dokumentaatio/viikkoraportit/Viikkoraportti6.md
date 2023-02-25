# Viikkoraportti 6

Tällä viikolla toteutin LZ77-algoritmille dekompressointiosan. Sen lisäksi kasvatin kyseisen algoritmin etsintäikkunoiden kokoa viime viikkoisesta. Se auttoi pienentämään ja nopeuttamaan algoritmin toimintaa. 

Joka tapauksessa, tällä hetkellä toteutus on kuitenkin hidas isojen tiedostojen kanssa eikä kompressoi niitä alle 60% alkuperäisestä. Tämä johtuu siitä, koska lisäsin tallennettavan merkin bittimäärää seitsemästä viiteentoista. Tein tämän siksi, koska aikaisempi bittimäärä ei riittänyt monien merkkien tallentamiseen. Tähän voisi mahdollisesti auttaa se, että en tekisi bittijonosta tietyn pituista, vaan jokainen merkki käännettäisiin bittijonoksi ja siihen sitten lisättäisiin sen verran nollia, että siitä tulee kahdeksalla jaollinen. Ylimääräisten nollien määrä tallennettaisiin myös merkkijonoon. Tällainen toteutus on Huffmanin koodissa. Onko algoritmi tällaisenaan ok, vai pitäisikö sitä saada nopeammaksi?

Palautin Huffmanin algoritmin kaikki toiminnot, paitsi Node-luokan, samaan moduulin. Huffman toimii hyvin ja nopeasti, mutta siinä on sellainen bugi, että se ei toimi merkkijonoilla, joissa on pelkästään samaa merkkiä. Tällaisten merkkijonojen dekompressoitu tiedosto on tyhjä.

Tein ohjelmille suorituskykytestit, joiden kuvaukset löytyvät testausdokumentista. Jos suorituskykytestaukseen pitäisi tehdä lisäyksiä tai muutoksia, niin kuulen tästä mielelläni.

Ensi viikolla yritän saada Huffmanin toimimaan myös samanmerkkisillä tiedostoilla. Jos on tarpeen, niin yritän tehdä LZ77-algoritmista nopeamman. Suunnitelmana on myös käydä kaikkia projektiin liittyviä tiedostoja läpi ja tehdä niihin tarvittavia lisäyksiä ja siistimisiä.

Käytetty aika: 17 tuntia

