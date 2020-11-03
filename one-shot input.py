import PySimpleGUI as sg
layout = [ [sg.Text("Name"), sg.Input()], [sg.Button("OK")] ]

window = sg.Window("Hello App", layout)
#create window
window.read()
#print window