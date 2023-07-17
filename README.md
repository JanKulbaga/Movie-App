# Movie App - REST API

## Backend

Použítá verzia Pythonu: 3.11.1

- web framework Flask ako server
- flask-cors
- python-dotenv
- sqlite3 database

Potrebné doinštalovanie knižníc pre správny beh aplikácie

```
pip install Flask
pip install flask-cors
pip install python-dotenv
```

Pre beh aplikácie spustiť main.py pomocou jednoho z príkazov v CMD alebo termináli

```
python main.py
python3 main.py
```

V aplikácií existujú 5 možných end pointov, s ktorými môžeme pracovať

| End Point                                                | Popis                                                        |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| http://127.0.0.1:8080/api/v1/popular?page=1              | Vypíše v JSON formáte prvých 20 populárnych filmov           |
| http://127.0.0.1:8080/api/v1/top_rated?page=1            | Vypíše v JSON formáte prvých 20 najlepšie hodnotených filmov |
| http://127.0.0.1:8080/api/v1/alphabetical?page=1         | Vypíše v JSON formáte prvých 20 filmov od A-Z                |
| http://127.0.0.1:8080/api/v1/reverse_alphabetical?page=1 | Vypíše v JSON formáte prvých 20 filmov od Z-A                |
| http://127.0.0.1:8080/api/v1/movies?search=Avengers      | Vypíše v JSON formáte filmy, ktoré obsahujú názov Avengers   |

## Frontend

- HTML
- CSS
- JavaScript

Pre spustenie HTML stačí použiť obľubený prehliadač
