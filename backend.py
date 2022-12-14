import sqlite3

def create_database():
    conn = sqlite3.connect("member_database.db")
    query = (""" CREATE TABLE IF NOT EXISTS MEMBERS (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        first_name VARCHAR(25) NOT NULL,
        last_name VARCHAR(25) NOT NULL,
        adress VARCAHR(50) NOT NULL,
        zip_code INTEGER NOT NULL ); """)
    conn.execute(query)
    conn.close()

def insert_contact(first_name, last_name, adress, zip_code):
    insert_conn = sqlite3.connect("member_database.db")
    insert_conn.execute(""" INSERT INTO MEMBER_DATABASE (first_name, last_name, adress, zip_code, member_id) 
        VALUES (?, ?, ?, ?) """, (first_name, last_name, adress, zip_code))
    insert_conn.commit()
    insert_conn.close()

def view_all_tasks():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Member_list')
    results = cursor.fetchall()
    return results