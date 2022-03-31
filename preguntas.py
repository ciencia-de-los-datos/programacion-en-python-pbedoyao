"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv
from collections import Counter
from operator import itemgetter

def leerarchivo():
    with open("data.csv", "r") as file:
        datos = csv.reader(file, delimiter='\t', quotechar='"')
        columnas = list(datos)
       
    return columnas


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    
    datos = leerarchivo()
    sumarcolumnados = 0
    for leersegundacolum in datos:
        sumarcolumnados = sumarcolumnados+int((leersegundacolum[1]))

    return sumarcolumnados


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    
    datos = leerarchivo()
    lisprimeracolumna = []
    for leerprimeracolum in datos:
        lisprimeracolumna.append(leerprimeracolum[0])
    
    tupletras = Counter(lisprimeracolumna).most_common(5)
    tupletras.sort(key=itemgetter(0), reverse=False)
    return tupletras


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    
    datos = leerarchivo()
    lisprimeracolumna = []
    lissegundacolumna = []
    for leercolum in datos:
        lisprimeracolumna.append(leercolum[0])
        lissegundacolumna.append(int(leercolum[1]))
    
    lisdatos = list(zip(lisprimeracolumna, lissegundacolumna))
    result={}
 
    for i in lisdatos:
        if i[0] in result:
            result[i[0]]+=i[1]
        else:
            result[i[0]]=i[1]
            
    lisresult = list(result.items())
    lisresult.sort(key=itemgetter(0), reverse=False)
    return lisresult
        

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    
    datos = leerarchivo()
    listercolumna = []
    for leercolum in datos:
        listercolumna.append(leercolum[2])
        
    listfecha = [z[0:].split("-") for z in listercolumna[0:]]    
    listmes = [z[1] for z in listfecha[0:]]
    
    tupmes = Counter(listmes).most_common(12)
    tupmes.sort(key=itemgetter(0), reverse=False)    
    
    return tupmes

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos = leerarchivo()
    lisprimeracolumna = []
    lissegundacolumna = []
    for leercolum in datos:
        lisprimeracolumna.append(leercolum[0])
        lissegundacolumna.append(int(leercolum[1]))
    
    lisdatos = list(zip(lisprimeracolumna, lissegundacolumna))
    lisResultado = []
    lisResultadoFinal = []

    for i in lisdatos:
        if i[0] not in lisResultado:
            lisResultado.append(i[0])

    for i in lisResultado:
        menor=0
        mayor=0
        lisResultadoFin= []
        for j in lisdatos:
            if [i][0]==[j][0][0]:
                lisResultadoFin.append([j][0][1])           
        menor = min(lisResultadoFin)
        mayor = max(lisResultadoFin)
        lisResultadoFinal.append(([i][0],mayor, menor))
        lisResultadoFinal.sort(key=itemgetter(0), reverse=False)
        
    return lisResultadoFinal

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    datos = leerarchivo()
    lisQuintaColumna = []
    for leercolum in datos:
        lisQuintaColumna.append(leercolum[4])

    listatotal = []
    lisResultado = []
    lisResultadoFinal = []
    
    for i in lisQuintaColumna:
        columnas = [] 
        columnas = str(i).split(',')
        for i in columnas:
            key = i[:3]
            value = i[4:len(i)]
            listatotal.append([key,int(value)])
    
    for i in listatotal:
         if i[0] not in lisResultado:
             lisResultado.append(i[0])
    
    for i in lisResultado:
        menor=0
        mayor=0
        lisResultadoFin= []
        for j in listatotal:
            if [i][0]==[j][0][0]:
                lisResultadoFin.append([j][0][1])           
        menor = min(lisResultadoFin)
        mayor = max(lisResultadoFin)
        lisResultadoFinal.append(([i][0], menor, mayor))
        lisResultadoFinal.sort(key=itemgetter(0), reverse=False) 

    return lisResultadoFinal

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    datos = leerarchivo()
    lisSegundacolumna = []
    lisPrimeracolumna = []
    lisdatos = []
    for leercolum in datos:
        lisSegundacolumna.append(leercolum[1])
        lisPrimeracolumna.append(leercolum[0])
    
    lisdatos = list(zip(lisSegundacolumna,lisPrimeracolumna ))
    listatotal = []
    for i in lisSegundacolumna:
         if i[0] not in listatotal:
             listatotal.append(i[0])
    
    listatotal.sort(key=itemgetter(0), reverse=False) 
             
    lisResultado = []
    for i in listatotal:
        lisletra = []
        for j in lisdatos:
            if i==j[0]:
                lisletra.append(j[1])
                      
        lisResultado.append((i,lisletra))
    
    return lisResultado

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    datos = leerarchivo()
    lisSegundacolumna = []
    lisPrimeracolumna = []
    lisdatos = []
    for leercolum in datos:
        lisSegundacolumna.append(leercolum[1])
        lisPrimeracolumna.append(leercolum[0])
    
    lisdatos = list(zip(lisSegundacolumna,lisPrimeracolumna ))
    listatotal = []
    for i in lisSegundacolumna:
         if i[0] not in listatotal:
             listatotal.append(i[0])
    
    listatotal.sort(key=itemgetter(0), reverse=False) 
             
    lisResultado = []
    for i in listatotal:
        lisletra = []
        for j in lisdatos:
            if i==j[0] and j[1] not in lisletra:
                lisletra.append(j[1])
                
        lisletra.sort(key=itemgetter(0), reverse=False)         
        lisResultado.append((i,lisletra))

    return lisResultado

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    datos = leerarchivo()
    lisQuintaColumna = []
    for leercolum in datos:
        lisQuintaColumna.append(leercolum[4])

    listatotal = []
    lisResultado = []
    lisResultadoTotal = []
    
    for i in lisQuintaColumna:
        columnas = [] 
        columnas = str(i).split(',')
        for i in columnas:
            key = i[:3]
            value = i[4:len(i)]
            listatotal.append([key,int(value)])
    
    for i in listatotal:
        if i[0] not in lisResultado:
            lisResultado.append(i[0])
    
    for i in lisResultado:
        repeticiones = 0
        for j in listatotal:
            if [i][0]==[j][0][0]:
                repeticiones = repeticiones+1
        lisResultadoTotal.append(([i][0],repeticiones))
        lisResultadoTotal.sort(key=itemgetter(0), reverse=False) 
    
    dicFibnal = dict(lisResultadoTotal)
    return dicFibnal

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    datos = leerarchivo()
    lisQuintaColumna = []
    lisUnacolumna = []
    lisCuartaColumna = []
    for leercolum in datos:
        lisUnacolumna.append(leercolum[0])
        lisCuartaColumna.append(leercolum[3])
        lisQuintaColumna.append(leercolum[4])
    
    lisdatos = list(zip(lisUnacolumna, lisCuartaColumna, lisQuintaColumna))
    
    listatotal = []
    
    for i in lisdatos:
            listatotal.append((i[0],int(i[1].count(','))+1,int(i[2].count(','))+1))
    
    return listatotal

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    
    datos = leerarchivo()
    lisFinal = []
    for leercolum in datos:
        valornum = int(leercolum[1])
        liscuart = []
        liscuart.append(leercolum[3].split(','))

        for t in liscuart:
            for i in t:
                lisFinal.append([i, valornum])

    resultado={}
 
    for i in lisFinal:
        if i[0] in resultado:
            resultado[i[0]]+=i[1]
        else:
            resultado[i[0]]=i[1]
            
    resul= []
    resul = list(resultado.items())
    resul.sort(key=itemgetter(0), reverse=False)
    resultado = dict(resul)
    
    return resultado

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    datos = leerarchivo()
    lisFinal = []
    lisUno = []
    lisResultado = []
    for leercolum in datos:
        valornum = leercolum[0]
        liscuart = []
        liscuart.append(leercolum[4].split(','))
        lisUno.append(leercolum[0])
        for t in liscuart:
            for i in t:
                lisFinal.append([i, valornum])
    
    for i in lisUno:
         if i[0] not in lisResultado:
             lisResultado.append(i[0])
             
    lisResultadoFinal = {}         
    for leervalor in lisResultado:
        for i in lisFinal:
            if leervalor == i[1]:
                if i[1] not in lisResultadoFinal:
                    lisResultadoFinal.update({i[1]:int(i[0][4:len(i[0])])})
                else:
                    value = int(i[0][4:len(i[0])])
                    lisResultadoFinal.update({i[1]:lisResultadoFinal[i[1]]+value})
    
    resul= []
    resul = list(lisResultadoFinal.items())
    resul.sort(key=itemgetter(0), reverse=False)
    lisResultadoFinal = dict(resul)
    
    return lisResultadoFinal

