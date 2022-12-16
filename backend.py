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
        address VARCAHR(50) NOT NULL,
        zip_code INTEGER NOT NULL ); """)
    conn.execute(query)
    conn.close()


def insert_contact(first_name, last_name, address, zip_code):
    insert_conn = sqlite3.connect("member_database.db")
    insert_conn.execute(""" INSERT INTO MEMBERS (first_name, last_name, address, zip_code) 
        VALUES (?, ?, ?, ?) """, (first_name, last_name, address, zip_code))
    insert_conn.commit()
    insert_conn.close()


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
                  [sg.Text("Adress", size=(15, 1)), sg.Input(key="-ADDRESS-")],
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
                               values["-ADDRESS-"],
                               values["-ZIPCODE-"])

                Windows.success_window("added")
                break

            elif event == sg.WIN_CLOSED or event == "-CANCEL-":
                break

        window.close()

    @staticmethod
    def view_window():
        conn = sqlite3.connect("member_database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()

        layout = [[sg.Push(),
                   sg.InputText(key='-SEARCH_BOX-', size=(30, 1)),
                   sg.Button("SEARCH", key="-SEARCH-")],
                  [sg.Text("")],
                  [sg.Push(),
                   sg.Table(values=rows,
                            headings=["Member ID", "First Name", "Last Name", "Address", "Zip Code"],
                            auto_size_columns=True,
                            justification="center",
                            num_rows=min(len(rows), 40),
                            row_height=25,
                            key='-TABLE-',
                            size=(600, 600)),
                   sg.Push()]]

        window = sg.Window("Members Table", layout, modal=True, font=default_font, size=(650, 500))
        window.read()

        # TODO: add button event for edit that opens up window with input boxes for all attributes.
        # TODO: add button event to delete a member
        # TODO: fix table size
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == '-SEARCH-':
                search_term = values['-SEARCH_BOX-']
                cursor.execute("SELECT * FROM members WHERE member_id LIKE ?"
                               "OR first_name LIKE ? " 
                               "OR last_name LIKE ?",
                               ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
                rows = cursor.fetchall()
                window['-TABLE-'].Update(values=rows)



        conn.close()
