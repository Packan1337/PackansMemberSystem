import PySimpleGUI as sg
from backend import *

create_database()

sg.theme("DefaultNoMoreNagging")

layout = [
    [sg.Text("PACKAN'S MEMBERSHIP MANAGEMENT", font=("Arial", 32))],
    [sg.Text("Select an option below to proceed.", font=("Arial", 24))],
    [sg.Button("ADD MEMBER", key="-ADD-"),
     sg.Button("VIEW ALL MEMBERS", key="-VIEW-"),
     sg.Button("EDIT OR REMOVE MEMBER", key="-EDIT-")]
]

window = sg.Window("PACKAN'S MEMBERSHIP MANAGEMENT", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-ADD-":
        print("ADD")

    if event == "-VIEW-":
        print("VIEW")

    if event == "-EDIT-":
        print("EDIT")

window.close()