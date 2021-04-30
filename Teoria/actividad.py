import ventanas
import funciones
import collections


#fuente https://ourworldindata.org/life-expectancy
header, lista = funciones.abrir_archivo('files','life-expectancy.csv') 

lista = list(map(lambda y:[y[0],float(y[3])],filter(lambda x:x[2]== '2019' 
                                                        and not funciones.continente(x[0]),lista)))

c = collections.Counter
mayor_exp = {}
for elem in lista:
    mayor_exp[elem[0]] = elem[1]
mayor_exp = c(mayor_exp).most_common(20) #los 20 estados que mayor expectativa de vida tienen en 2019

dic_mayor_exp = dict(mayor_exp)
funciones.crear_json('files','expectativa.txt',dic_mayor_exp)

ventanas.ventana_principal(mayor_exp)