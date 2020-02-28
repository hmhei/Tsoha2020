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

**Käyttäjä:** 

  * voi tarkastella kirjaston kirjavalikoimaa ja kirjojen tietoja, 
  * voi tehdä lainoja, lainan palautuksia ja palautetuiksi merkittyjen lainojen poistoa. 
  * voi tarkastella, muokata ja tallentaa omia tietojaan.

**Ylläpitäjä:** 

  * Täysi CRUD-toiminnallisuus kahteen tietokantatauluun: kirja ('book') ja käyttäjä ('account').

**Yleistä:**

  * Sovelluksen eri näkymissä on melko kattavasti ohjeistusta sovelluksen käytöstä.

  * Kirjojen tiedoissa on nimi, kirjoittaja, julkaisuvuosi, kappalemäärä, kirjan kuvaus, sekä lukumäärätiedot hyllyssä/lainassa/'palautettu muttei poistettu lainalistalta'. Ainoastaan ylläpitäjä voi lisätä tai poistaa kirjoja kirjaston valikoimasta.

  * Ylläpitäjä voi tällä hetkellä luoda uusia käyttäjiä samalla tavoin kuin uusi käyttäjä voi rekisteröityä palveluun. Ylläpitäjä ei tarkoituksellisesti voi tällä hetkellä luoda uusia ylläpitäjätunnuksia, mutta tämä toiminnallisuus on varsin triviaalia lisätä tarvittaessa tulevaisuudessa.

  * Kun käyttäjä luo uuden lainan, vähenee kys. kirjan hyllyssä olevien lukumäärä vastaavasti. Lainojen määrää ei tällä hetkellä ole rajoitettu, kunhan kirjoja vain on hyllyssä. Kun käyttäjä merkitsee kirjan palautetuksi, lisääntyy kirjojen määrä hyllyssä vastaavasti. Lainasta jää edelleen merkintä käyttäjän lainalistalle (tilassa Palautettu = True), jonka käyttäjä voi sitten poistaa. Ylläpitäjä ei tällä hetkellä tarkoituksella pääse käsiksi yksittäisten käyttäjien lainoihin, mutta tämäkin toiminnallisuus on melko helppoa toteuttaa tulevaisuudessa, mikäli sille olisi tarvetta.

  * Laina ottaa nimensä kirjan lainahetken nimestä. Mikäli ylläpitäjä käy tämän jälkeen muuttamassa kirjan nimeä, muutos ei (tällä hetkellä) heijastu käyttäjän lainaaman kirjan nimeen. Tämä ei mielestäni kuitenkaan ole ongelma, sillä kys. lainan book_id kuitenkin sitoo lainan juuri siihen kirjaan, vaikka kirjan nimi olisikin muutettu, eli hyllylukumäärä yms. toimivat odotetusti (ja todellisuudessakin kirjan nimet harvoin vaihtuvat..).

**Käyttötapaukset:**

https://github.com/hmhei/Tsoha2020/blob/master/documentation/Kayttotapaukset.md

**Asennusohje:**

https://github.com/hmhei/Tsoha2020/blob/master/documentation/Asennusohje.md

## TIETOKANTAKAAVIO:

![Kirjaston lainausjärjestelmä](https://github.com/hmhei/Tsoha2020/blob/master/documentation/Tietokantakaavio.png)
