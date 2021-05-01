import PySimpleGUI as sg 

def ventana_principal(mayor_exp,emojis):
    '''Ventana principal del programa'''
    layout = [[sg.Button('Expectativa de vida',size=(50,2),key='-BOTON 1-')],
                [sg.Button('Emojis',size=(50,2), key='-BOTON 2-')],
                [sg.Text(text='')],
                [sg.Button('Salir',size=(50,2),key='-SALIR-')]]
    window = sg.Window('',layout,no_titlebar=True,margins=(2,30))

    while True:
        event, values = window.read()    
        if event == '-BOTON 1-':
            window.hide()
            ventana_Boton1(mayor_exp)
            window.un_hide() 
        if event == '-BOTON 2-':
            window.hide()
            ventana_Boton2(emojis)
            window.un_hide()
        if event == '-SALIR-':
            break
    window.close()

def ventana_Boton1(mayor_exp):
    '''Ventana que se abre luego de presionar boton 1 en ventana principal'''
    layout = [[sg.Text('20 estados con mayor expectativa de vida: '),sg.Combo(values=(mayor_exp))],
                [sg.Button('Volver',key='-VOLVER-')]]
    window = sg.Window('Expectativa de vida',layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-VOLVER-':
            break
    window.close()

def ventana_Boton2(emojis):
    '''Ventana que se abre luego de presionar boton 2 en ventana principal'''
    layout = [[sg.Button('', size=(8,4), key=f'celda-{x}-{y}')for y in range(4)] for x in range(3)]
                                                                
                
   
    window = sg.Window('Emojis',layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == '-VOLVER-':
            break
        elif event.startswith('celda'): 
            celda,x,y = event.split('-') 
            window[event].update(emojis[int(y)*3+int(x)])

    window.close()



