import csv
import collections
import requests

c = collections.Counter
archivo = open("/home/alumno/Descargas/appstore_games.csv","r")
csvreader = csv.reader(archivo,delimiter = ',')
next(csvreader)
juegos = list(filter(lambda x:x[12] == 'ES' or 'ES' in x[12] and x[7] == '0',csvreader))

print('Nombres de los Juegos en español gratuitos:')
for elem in juegos:
    print(elem[2])
archivo.seek(0)
next(csvreader)
juegos = {}
for elem in csvreader:
    if elem[6] not in ('' or ' '):
        juegos[elem[4]] = int(elem[6])

mejores = c(juegos).most_common(10)
print(dict(mejores))

archivo.close()