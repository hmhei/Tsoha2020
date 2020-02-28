# Asennusohje

## Local

Lataa tai kloonaa sovellus Githubista (https://github.com/hmhei/Tsoha2020).

Navigoi komentorivillä sovelluksen juurikansioon, asenna virtuaaliympäristö (python -m venv venv) ja aktivoi se (source venv/bin/activate).

Asenna vaaditut riippuvuudet (pip install -r requirements.txt).

Käynnistä ohjelma juurikansiosta (python run.py). Tämän jälkeen voit sulkea ohjelman (CTRL + c). Sovelluksen tietokanta (loans.db) on nyt luotu application-kansioon.

Navigoi application-kansioon, ja avaa tietokanta (sqlite3 loans.db). Asenna admin-tunnukset: INSERT INTO account (name, username, password, address, phone, admin) VALUES ('Ylläpitäjä', 'admin', 'admintest', '-', '-', 1);

Admin-tunnukset on nyt luotu, joten voit poistua sqlitesta (.exit).

Käynnistä sovellus kuten aiemmin (python run.py), ja navigoi selaimessasi osoitteeseen (localhost:5000).

Olet nyt valmis käyttämään sovellusta! Muistathan noudattaa sovelluksessa annettuja kirjautumis- ja käyttöohjeita.

## Remote

Luo komentoriviltä (sovelluksen juurikansiossa) sovellukselle paikka Herokuun (heroku create joku-nimi).

Lisää vielä paikalliseen versionhallintaan tieto Herokusta (git remote add heroku https://git.heroku.com/joku-nimi.git).

Nyt voit lähettää sovelluksen Herokuun:
  * git add .
  * git commit -m "Initial commit"
  * git push heroku master

Lisää komentoriviltä sovelluksen käyttöön tieto siitä, että sovellus on Herokussa (heroku config:set HEROKU=1).

Voit halutessasi tarkistaa tässä vaiheessa, onko sovelluksella jo olemassa tietokanta Herokussa (heroku pg:psql).

Mikäli tietokantaa ei ole (Tsoha-lainaus has no databases), voit lisätä tietokannan itse (heroku addons:add heroku-postgresql:hobby-dev).

Avaa Herokun tietokanta (heroku pg:psql), ja asenna admin-tunnukset: INSERT INTO account (name, username, password, address, phone, admin) VALUES ('Ylläpitäjä', 'admin', 'admintest', '-', '-', TRUE);

Kun admin tunnukset on luotu, voit poistua tietokannasta (\q).

Sovelluksen tulisi nyt toimia Herokussa (https://joku-nimi.herokuapp.com)

