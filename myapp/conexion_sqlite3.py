import sqlite3
import requests
import json

#Aca cree la conexion a db sqlite3 y luego cree la tabla e inserte los datos de la pokeapi correspondientes para cumplir con lo pedido por el profesor OAK.

def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida


try:
    mi_conexion=sqlite3.connect("db.sqlite3")
    cursor = mi_conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS myapp_pokemon (ID INTEGER, nombre VARCHAR(50), tipo1 VARCHAR(50), tipo2 VARCHAR (50), altura INTEGER, peso INTEGER, inv VARCHAR(50))")
except Exception as ex:
    print(ex)
#se establece conexion y se crea la tabla.

i=0
y=1
#Basicamente se crearan variables para rellenar la tabla de buena manera.
while i < 50:
    mi_conexion=sqlite3.connect("db.sqlite3")
    c = mi_conexion.cursor()
    url = "https://pokeapi.co/api/v2/pokemon/" + str(y)
    r = requests.get(url)
    j = r.json()
    jn = j['name']
    jt = j['types']
    ja = j['height']
    jp = j['weight']

    jt1 = jt[0]
    jt11 = jt1['type']
    jt111 = jt11['name']

#caso del segundo tipo
    if(len(jt)==2):
        jt2 = jt[1]
        jt21 = jt2['type']
        jt211 = jt21['name']
    else:
        jt211 = "no posee"
    
#caso de invertir el nombre
    inv= invertir_cadena_manual(jn)
    
    c.execute("INSERT INTO myapp_pokemon VALUES(?,?,?,?,?,?,?)", (y, jn, jt111, jt211, ja, jp, inv))
    mi_conexion.commit()
    i=i+1
    y=y+1
#Se rellena la tabla con la informacion que nos sera util.



mi_conexion.close()
