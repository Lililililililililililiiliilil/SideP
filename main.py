# hello_world.py
import random, string, time
import PySimpleGUI as sg

sg.theme('LightBrown7')

layout = [[sg.Text("Бляяяя братан, включи майнер")],
          [sg.Button("НАМАЙНИТЬ")],
          [sg.Text('Биточки:'), sg.Text(size=(25, 1), key='-Bit-')],
          [sg.ProgressBar(100, orientation='horizontal', size=(30, 20), key='-PROG-')]]

window = sg.Window("Miner", layout)
window.read()

while True:  # The Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event.startswith("НАМАЙНИТЬ"):
        for number in range(1000, 0, -7):
            window['-Bit-'].update(number)
            window['-PROG-'].update_bar((1000 - number) % 100)
            time.sleep(.25)  # simulate read time
            window.refresh()
        window['-Bit-'].update('Спасибо за битки братанчик ;)')
window.close()
