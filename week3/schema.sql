create table users (
    user_id integer primary key autoincrement,
    username varchar(50) not null ,
    email text not null
);

CREATE TABLE IdentityCard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL,
    person_id INTEGER,
    FOREIGN KEY(person_id)  REFERENCES users(user_id) ON UPDATE CASCADE
);
