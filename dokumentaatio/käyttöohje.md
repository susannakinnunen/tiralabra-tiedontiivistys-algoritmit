# Käyttöohjeet

## Käynnistys
1. Kloona projekti
2. Asenna Poetry: ```pip install poetry```
3. Asenna riippuvuudet: ```poetry install```
4. Aja Huffmanin ohjelma juurikansiosta: ```poetry run python3 src/ui_huffman.py``` ja LZ77 ohjelma: ```poetry run python3 src/ui_lz77.py```
 - Anna syötteenä .txt-tiedoston polku.
    - voit käyttää esimerkiksi kalevala.txt-tiedostoa, joka löytyy juurikansiosta (Huom. LZ77 toimii hyvin hitaasti isojen tiedostojen kanssa.)
 - Ohjelma kertoo, mistä polusta löydät kompressoidun ja dekompressoidun version alkuperäisestä tiedostosta. 
 
## Testit

### Yksikkö- ja end-to-end -testaus
Testien suorittaminen ohjelman juurikansiosta: ```poetry run pytest src```

### Suorituskykytestaus
Huffmanin algoritmiin liittyvät testit voi ajaa juurikansiossa komentoriviltä kommennolla:

```poetry run python3 src/performance_test/huffman_performance.py```

ja LZ77-algoritmin komennolla:

```poetry run python3 src/performance_test/lz77_performance.py```

## Pylint
Pylintin ajaminen juurikansiosta ```poetry run pylint src```

