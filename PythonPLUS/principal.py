import ventanas
import funciones
import collections


#fuente: https://ourworldindata.org/life-expectancy
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

# fuente: https://www.kaggle.com/eliasdabbas/emoji-data-descriptions-codepoints
header, emojis = funciones.abrir_archivo('files','emoji_df.csv')

emojis = list(map(lambda y:[y[0],y[1]],filter(lambda x:x[2]=='Smileys & Emotion' 
                                                        and x[3]=='face-smiling',emojis)))
# me quedo solo con los emojis de la categoria Smileys & Emotion y la subcategoria face-smiling 
                                                    
dic_emojis = dict(emojis)
emojis= list(map(lambda x:x[0],emojis))#lista para enviar a ventana, solo quedan emojis.

funciones.crear_json('files','emojis.txt',dic_emojis)

ventanas.ventana_principal(mayor_exp,emojis)
