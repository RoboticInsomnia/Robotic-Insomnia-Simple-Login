import PySimpleGUI as sg

sg.theme('DarkAmber')  

layout = [  [sg.Text('Enter Username: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Robotic Insomnia Admin Login', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered: ', values[0])

window.close()