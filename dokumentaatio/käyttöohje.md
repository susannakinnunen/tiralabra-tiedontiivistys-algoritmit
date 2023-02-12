# Käyttöohjeet

## Käynnistys
1. Kloona projekti
2. Asenna Poetry: ```pip install poetry```
3. Asenna riippuvuudet: ```poetry install```
4. Aja ohjelma juurikansiosta: ```poetry run python3 src/ui_huffman.py```
 - Anna syötteenä .txt-tiedoston polku.
    - voit käytttää esimerkiksi kalevala.txt-tiedostoa, joka löytyy juurikansiosta
 - Ohjelma kertoo, mistä polusta löydät kompressoidun ja dekompressoidun version alkuperäisestä tiedostosta. 

## Testit
Testien suorittaminen ohjelman juurikansiosta: ```poetry run pytest src```

## Pylint
Pylintin ajaminen juurikansiosta ```poetry run pylint src```

