# Asennusohje

## Local

Lataa tai kloonaa sovellus Githubista (https://github.com/hmhei/Tsoha2020).

Navigoi komentorivillä sovelluksen juurikansioon, asenna virtuaaliympäristö (python -m venv venv) ja aktivoi se (source venv/bin/activate).

Asenna vaaditut riippuvuudet (pip install -r requirements.txt).

Käynnistä ohjelma juurikansiosta (python run.py). Tämän jälkeen voit sulkea ohjelman (CTRL + c). Sovelluksen tietokanta (loans.db) on nyt luotu application-kansioon.

Navigoi application-kansioon, ja avaa tietokanta (sqlite3 loans.db). Asenna admin-tunnukset (INSERT INTO account (name, username, password, address, phone, admin) VALUES ('Ylläpitäjä', 'admin', 'admintest', '-', '-', 1);

Admin-tunnukset on nyt luotu, joten voit poistua sqlitesta (.exit).

Käynnistä sovellus kuten aiemmin (python run.py), ja navigoi selaimessasi osoitteeseen (localhost:5000).

Olet nyt valmis käyttämään sovellusta! Muistathan noudattaa sovelluksessa annettuja kirjautumis- ja käyttöohjeita.

## Remote
