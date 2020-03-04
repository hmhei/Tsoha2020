# KÄYTTÖTAPAUKSIA

## TOTEUTETTU

Käyttäjänä haluan rekisteröityä uudeksi käyttäjäksi, jotta voin käyttää järjestelmää.
  * INSERT INTO account (name, username, password, address, phone, admin) VALUES (?, ?, ?, ?, ?, False);

Käyttäjänä haluan kirjautua sisään luomillani tunnuksilla, jotta voin käyttää järjestelmän toiminnallisuuksia.
  * SELECT * FROM account WHERE username = ? AND password = ?);

Käyttäjänä haluan lisätä uuden lainan, jotta kirjasto tietää lainanneeni kirjan.
  * INSERT INTO loan (name, due_date, returned, account_id, book_id) VALUES (?, ?, False, ?, ?);

Käyttäjänä haluan merkitä lainan palautetuksi, jotta kirjasto tietää palauttaneeni kirjan.
  * UPDATE loan SET name = ?, due_date = ?, returned = True, account_id = ?, book_id = ? WHERE Loan.id = ?;

Käyttäjänä haluan, että kukin laina kohdistuu juuri minuun, eikä kehenkään muuhun käyttäjään, ja että vain minä itse näen omat lainani eikä kukaan muu käyttäjä.

Käyttäjänä haluan poistaa lainan lainalistaltani, kun kys. laina on palautettu (jos sovellusta haluaa tulevaisuudessa jatkokehittää, niin voisi pohtia mikä olisi järkevin tapa toteuttaa tämä jako lainan palautuksen / lainamerkinnän poiston välillä. Kuitenkin tämän harjoitustyön puitteissa toiminnallisuus lienee OK nykyisessä muodossaan).
  * DELETE FROM loan WHERE Loan.id = ?;

Käyttäjänä haluan pystyä lukemaan kirjaston tietokannassa olevat kirjat, jotta voin nähdä, mitä kirjoja kirjastossa on olemassa.
  * SELECT * FROM book;

Käyttäjänä haluan pystyä muokkaamaan omia tietojani, jotta ne pysyvät ajan tasalla.
  * UPDATE account SET name = ?, username = ?, password = ?, address = ?, phone = ?, admin = False WHERE Account.id = current_user.id;

Ylläpitäjänä haluan pystyä lisäämään, lukemaan, muokkaamaan ja poistamaan kirjoja järjestelmässä, jotta kirjaston kirjatietokanta pysyy ajan tasalla.
  * INSERT INTO book (name, author, published, count, desc) VALUES (?, ?, ?, ?, ?);
  * SELECT * FROM book WHERE Book.id = ?;
  * UPDATE book SET name = ?, author = ?, published = ?, count = ?, desc = ? WHERE Book.id = ?;
  * DELETE FROM book WHERE Book.id = ?;

Ylläpitäjänä haluan pystyä näkemään kunkin kirjan laina/palautustilanteen kirjan tiedoista.
  * SELECT * FROM book WHERE Book.id = ?;

Ylläpitäjänä haluan pystyä hallinnoimaan sovelluksen käyttäjätietoja (luomaan, tarkastelemaan, muokkaamaan ja poistamaan käyttäjätietoja). 
  * INSERT INTO account (name, username, password, address, phone, admin) VALUES (?, ?, ?, ?, ?, False);
  * SELECT * FROM account WHERE Account.id = ?;
  * UPDATE account SET name = ?, username = ?, password = ?, address = ?, phone = ?, admin = False WHERE Account.id = ?;
  * DELETE FROM account WHERE Account.id = ?;
