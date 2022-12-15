import sqlite3
import PySimpleGUI as sg

header_font = ("Arial", 32)
subtitle_font = ("Arial", 24)
default_font = ("Arial", 16)

def create_database():
    conn = sqlite3.connect("member_database.db")
    query = (""" CREATE TABLE IF NOT EXISTS MEMBERS (
        member_id INTEGER PRIMARY KEY NOT NULL,
        first_name VARCHAR(25) NOT NULL,
        last_name VARCHAR(25) NOT NULL,
        adress VARCAHR(50) NOT NULL,
        zip_code INTEGER NOT NULL ); """)
    conn.execute(query)
    conn.close()

def insert_contact(first_name, last_name, adress, zip_code):
    insert_conn = sqlite3.connect("member_database.db")
    insert_conn.execute(""" INSERT INTO MEMBERS (first_name, last_name, adress, zip_code) 
        VALUES (?, ?, ?, ?) """, (first_name, last_name, adress, zip_code))
    insert_conn.commit()
    insert_conn.close()

def view_all_tasks():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM MEMBERS')
    results = cursor.fetchall()
    return results


class Windows:
    @staticmethod
    def success_window(type_of_success: str):

        layout = [[sg.Text(f"Successfully {type_of_success} member!")],
                  [sg.Push(), sg.Button("OK", key="-OK-"), sg.Push()]]

        window = sg.Window("Success!", layout, modal=True, font=default_font)

        while True:
            event, values = window.read()
            if event == "-OK-":
                window.close()
                break

    @staticmethod
    def add_window():
        layout = [[sg.Text("Add a new member\n", font=subtitle_font)],
                  [sg.Text("First name", size=(15, 1)), sg.Input(key="-FIRST_NAME-")],
                  [sg.Text("Last name", size=(15, 1)), sg.Input(key="-LAST_NAME-")],
                  [sg.Text("Adress", size=(15, 1)), sg.Input(key="-ADRESS-")],
                  [sg.Text("Zip Code", size=(15, 1)), sg.Input(key="-ZIPCODE-")],
                  [sg.Text("")],
                  [sg.Push(),
                   sg.Button("CANCEL", key="-CANCEL-", size=(20, 1)),
                   sg.Button("CONFRIM", key="-CONFIRM-", size=(20, 1))]]
        window = sg.Window("Add member", layout, modal=True, font=default_font)

        while True:
            event, values = window.read()

            if event == "-CONFIRM-":
                print(values["-FIRST_NAME-"])
                insert_contact(values["-FIRST_NAME-"],
                               values["-LAST_NAME-"],
                               values["-ADRESS-"],
                               values["-ZIPCODE-"])

                Windows.success_window("added")
                break

            elif event == sg.WIN_CLOSED or event == "-CANCEL-":
                break

        window.close()