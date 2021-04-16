import csv
import collections

c = collections.Counter

archivo = open("/home/alumno/Descargas/netflix_titles.csv","r")
archivo_nuevo = open("/home/alumno/Descargas/peliculas_2020.csv","w")

csvreader = csv.reader(archivo,delimiter = ',')

writer = csv.writer(archivo_nuevo)

encabezado = next(csvreader)
writer.writerow(encabezado)

pelis_2020 = filter(lambda x:x[7] == "2020",csvreader)

for elem in pelis_2020:
    writer.writerow(elem)

archivo.seek(0)
next(csvreader)
paises = []
for elem in csvreader:
    paises.append(elem[5])
paises = list(filter(lambda x:x != '',paises))
paises = collections.Counter(paises)

print('-'*40)
print(f'{"Pais":<20}{"Producciones":>20}')
print('-'*40)

for elem in paises.most_common(5):
    print(f'{elem[0]:<20}{elem[1]:>20}')

print('-'*40)
archivo.close()
archivo_nuevo.close()