import sqlite3

conn = sqlite3.connect("member_database.db")
query = (
    """ CREATE TABLE MEMBERS (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    adress VARCAHR(50) NOT NULL,
    zip_code INTEGER NOT NULL ); """
         )

conn.execute(query)
conn.close()