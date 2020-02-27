# KIRJASTON LAINAUSJÄRJESTELMÄ

https://tsoha-lainaus.herokuapp.com/

Harjoitustyössä on tarkoitus tehdä kirjojen lainausjärjestelmä kirjastolle.

Kirjaston järjestelmässä kaksi erityyppistä tiliä:
 
  * käyttäjä eli asiakas (rajatut oikeudet), ja
  * ylläpitäjä eli esim. kirjaston työntekijä (laajemmat oikeudet).

Ylläpitäjän kirjautumistunnukset:

  * Käyttäjänimi: admin
  * Salasana: admintest

## TOIMINTOJA:

Käyttäjä: 

  * voi tarkastella kirjaston kirjavalikoimaa ja kirjojen tietoja, 
  * voi tehdä lainoja, lainan palautuksia ja palautetuiksi merkittyjen lainojen poistoa. 
  * voi tarkastella, muokata ja tallentaa omia tietojaan.

Ylläpitäjä: 

  * CRUD-toiminnallisuus kahteen tietokantatauluun: kirja ('book') ja käyttäjä ('account').

Kirjojen tiedoissa on nimi, kirjoittaja, julkaisuvuosi, kappalemäärä, kirjan kuvaus, sekä lukumäärätiedot hyllyssä/lainassa/'palautettu muttei poistettu lainalistalta'. Ainoastaan ylläpitäjä voi lisätä tai poistaa kirjoja kirjaston valikoimasta.

Käyttötapaukset:

https://github.com/hmhei/Tsoha2020/blob/master/documentation/Kayttotapaukset.md

## TIETOKANTAKAAVIO:

![Kirjaston lainausjärjestelmä](https://github.com/hmhei/Tsoha2020/blob/master/documentation/Tietokantakaavio.png)
