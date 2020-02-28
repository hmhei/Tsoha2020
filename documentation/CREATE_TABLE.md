#CREATE_TABLE -lauseet

CREATE TABLE account (

  id INTEGER NOT NULL,
  
  date_created DATETIME,
  
  date_modified DATETIME,
  
  name VARCHAR(144) NOT NULL,
  
  username VARCHAR(144) NOT NULL,
  
  password VARCHAR(144) NOT NULL,
  
  address VARCHAR(144) NOT NULL,
  
  phone VARCHAR(144) NOT NULL,
  
  admin BOOLEAN NOT NULL,
  
  PRIMARY KEY (id)
  
);

CREATE TABLE author (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  name VARCHAR(144) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE book (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  name VARCHAR(144) NOT NULL,
  published INTEGER NOT NULL,
  count INTEGER NOT NULL,
  desc VARCHAR(1050) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE loan (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  name VARCHAR(144) NOT NULL,
  due_date VARCHAR(144) NOT NULL,
  returned BOOLEAN NOT NULL,
  account_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY(account_id) REFERENCES account (id),
  FOREIGN KEY(book_id) REFERENCES book (id)
);

CREATE TABLE book_author (
  book_id INTEGER,
  author_id INTEGER,
  FOREIGN KEY(book_id) REFERENCES book (id),
  FOREIGN KEY(author_id) REFERENCES author (id)
);
