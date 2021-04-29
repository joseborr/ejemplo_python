import PySimpleGUI as sg 

def ventana_principal(mayor_exp):
    layout = [[sg.Button('20 paises con mayor expectativa de vida',size=(50,2),key='-BOTON 1-')],
                [sg.Button('Boton 2',size=(50,2), key='-BOTON 2-')],
                [sg.Text(text='')],
                [sg.Button('Salir',size=(50,2),key='-SALIR-')]]
    window = sg.Window('Actividad 1 x Python Plus -TEORIA-',layout,no_titlebar=True,margins=(2,30))

    while True:
        event, values = window.read()    
        if event == '-BOTON 1-':
            window.hide()
            ventana_Boton1(mayor_exp)
            window.un_hide() 
        if event == '-BOTON 2-':
            window.hide()
            ventana_Boton2()
            window.un_hide()
        if event == '-SALIR-':
            break
    window.close()

def ventana_Boton1(mayor_exp):
    layout = [[sg.Text('20 paises ordenados segun expectativa de vida: '),sg.Combo(values=(mayor_exp))],
                [sg.Button('Volver',key='-VOLVER-')]]
    window = sg.Window('Boton 1',layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-VOLVER-':
            break
    window.close()

def ventana_Boton2():
    layout = [[sg.Text(text='aca va el layout del boton 2')],
                [sg.Button('Volver',key='-VOLVER-')]]
    window = sg.Window('Boton 1',layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-VOLVER-':
            break
    window.close()

