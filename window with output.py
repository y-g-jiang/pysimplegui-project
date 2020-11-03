import PySimpleGUI as sg

layout = [
            [sg.Text("Name:"), sg.Input(key = "__NAME__")],
            [sg.Button("OK")]
         ]

window = sg.Window("test", layout)

event, values = window.read()

sg.Popup("你好," + values["__NAME__"])