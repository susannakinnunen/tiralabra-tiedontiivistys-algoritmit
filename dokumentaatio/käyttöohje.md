# Käyttöohjeet

## Käynnistys
1. Kloona projekti
2. Asenna Poetry: ```pip install poetry```
3. Asenna riippuvuudet: ```poetry install```
4. Aja Huffmanin ohjelma juurikansiosta: ```poetry run python3 src/ui_huffman.py``` ja LZ77 ohjelma: ```poetry run python3 src/ui_lz77.py```
 - Anna syötteenä .txt-tiedoston polku.
    - voit käyttää esimerkiksi kalevala.txt-tiedostoa, joka löytyy juurikansiosta
 - Ohjelma kertoo, mistä polusta löydät kompressoidun ja dekompressoidun version alkuperäisestä tiedostosta. 
 - 19.2. Tällä hetkellä LZ77 vasta kompressoi ja toimii hitaasti isojen tiedostojen kanssa.

## Testit
Testien suorittaminen ohjelman juurikansiosta: ```poetry run pytest src```

## Pylint
Pylintin ajaminen juurikansiosta ```poetry run pylint src```

