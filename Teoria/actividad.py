import ventanas
import csv
import os
import json
import collections
import ventanas

#fuente https://ourworldindata.org/life-expectancy
path = 'files'
archivo_exp = 'life-expectancy.csv'
try: 
    path_arch = os.path.join(os.getcwd(),path)
    archivo = open(os.path.join(path_arch,archivo_exp),'r')
    csvreader = csv.reader(archivo,delimiter=',')
except:
    print('No se pudo abrir el archivo ' + archivo_exp)
header, lista = next(csvreader),list(csvreader)

def continente(cadena):
    '''devuelve boolean si la cadena ingresada es continente'''
    continentes = ['Africa','Americas','Asia','Europe','Oceania']
    return cadena in continentes
    

lista = list(map(lambda y:[y[0],float(y[3])],filter(lambda x:x[2]== '2019' 
                                                        and not continente(x[0]),lista)))

c = collections.Counter
mayor_exp = {}
for elem in lista:
    mayor_exp[elem[0]] = elem[1]
mayor_exp = c(mayor_exp).most_common(20) #los 20 paises que mayor expectativa de vida tienen en 2019
ventanas.ventana_principal(mayor_exp)


