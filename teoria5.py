import csv

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

paises = []
for elem in csvreader:
    paises.append(elem[5])
cant = []
for pais in paises:
    cant.append(paises.count(pais))

cantidades = list(zip(paises,cant))

def segundo(elem):
    return elem[1]
cantidades.sort(key=segundo,reverse=True)
sin_repetir = []

for elem in cantidades:
    if elem not in sin_repetir and elem[0] != '' and len(sin_repetir) < 5:
        sin_repetir.append(elem)
print('-'*30)
print(f'{"Pais":<20}{"Peliculas":>10}')
print('-'*30)
for elem in sin_repetir:
    print(f'{elem[0]:<20}{elem[1]:>10}')

print('-'*30)
archivo.close()
archivo_nuevo.close()