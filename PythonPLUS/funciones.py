import csv
import os
import json

def abrir_archivo(path,archivo):
    '''abre y cierra archivo csv y retorna lista con elementos y header'''
    try:
        path_arch = os.path.join(os.getcwd(),path)
        archivo_a = open(os.path.join(path_arch,archivo),'r')
        csvreader = csv.reader(archivo_a,delimiter=',')
    except:
        print('No se pudo abrir el archivo ' + archivo)
    
    header, lista = next(csvreader),list(csvreader)
    archivo_a.close()
    return header, lista

def crear_json(path,archivo,dic):
    '''Crea archivo JSON a partir de un diccionario que recibe por parametro junto a la ruta'''

    path_arch = os.path.join(os.getcwd(),path)
    archivo_json = open(os.path.join(path_arch,archivo),'w')
    json.dump(dic,archivo_json,indent=4)
    archivo_json.close()

def continente(cadena):
    '''devuelve boolean si la cadena ingresada es continente'''
    continentes = ['Africa','Americas','Asia','Europe','Oceania']
    return cadena in continentes