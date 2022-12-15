from backend import *

create_database()

sg.theme("DarkGrey3")

layout = [
    [sg.Text("PACKAN'S MEMBERSHIP MANAGEMENT\n", font=header_font)],
    [sg.Text("Select an option below to proceed.", font=subtitle_font)],
    [sg.Button("ADD MEMBER", key="-ADD-", size=(20, 1)),
     sg.Button("VIEW MEMBERS", key="-VIEW-", size=(20, 1)),
     sg.Button("EDIT MEMBER", key="-EDIT-", size=(20, 1))]
]

window = sg.Window("PACKAN'S MEMBERSHIP MANAGEMENT", layout, font=default_font)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-ADD-":
        Windows.add_window()

    if event == "-VIEW-":
        print("VIEW")

    if event == "-EDIT-":
        print("EDIT")

window.close()