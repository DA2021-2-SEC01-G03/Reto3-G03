
from DISClib.DataStructures.arraylist import newList
from DISClib.DataStructures.bst import contains, deleteMax
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
from DISClib.Algorithms.Sorting import mergesort as ms
import datetime
assert config

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'ufos': None,
                'ciudades': None,
                'horas': None,
                'fechas': None
                }

    analyzer['ufos'] = om.newMap(omaptype ='RBT' , comparefunction = compareDatetimes)
    analyzer['ciudades'] = m.newMap(maptype='PROBING')
    analyzer['horas'] = m.newMap(maptype='PROBING')
    analyzer['fechas'] = m.newMap(maptype='PROBING')

    return analyzer


# Funciones para agregar informacion al catalogo


def addUfo(analyzer, ufo):

    om.put(analyzer['ufos'], ufo['datetime'], ufo)

    return analyzer

def llenarCiudades(analyzer, ufo):
    mapCiudades = analyzer['ciudades']
    ciudad = ufo['city']
    fecha = ufo['datetime']
    if m.contains(mapCiudades, ciudad):
        dict = m.get(mapCiudades, ciudad)['value']
        dict['cantidad'] += 1   
        m.put(mapCiudades, ciudad, dict)
    else:
        m.put(mapCiudades, ciudad, {'ciudad': ciudad, 'cantidad': 1})
   

def llenarHoras(analyzer, ufo):
    horas = analyzer['horas']
    hora = str( str(ufo['datetime'][11]) + str(ufo['datetime'][12]) + str(ufo['datetime'][13]) + str(ufo['datetime'][14]) 
    + str(ufo['datetime'][15]) + str(ufo['datetime'][16]) + str(ufo['datetime'][17]) + str(ufo['datetime'][18])  )
    if m.contains(horas, hora):
        contador = m.get(horas, hora)['value'] 
        contador += 1
        m.put(horas, hora, contador)
    else:
        m.put(horas, hora, 1)

def llenarFechas(analyzer, ufo):
    fechas = analyzer['fechas']
    fecha = str( str(ufo['datetime'][0]) + str(ufo['datetime'][1]) + str(ufo['datetime'][2]) + str(ufo['datetime'][3]) 
    + str(ufo['datetime'][4]) + str(ufo['datetime'][5]) + str(ufo['datetime'][6]) + str(ufo['datetime'][7]) +
    str(ufo['datetime'][8]) + str(ufo['datetime'][9]) )
    if m.contains(fechas, fecha):
        contador = m.get(fechas, fecha)['value'] 
        contador += 1
        m.put(fechas, fecha, contador)
    else:
        m.put(fechas, fecha, 1)

# ==============================
# Funciones de Consulta
# ==============================

def cantidadUfosCiudades(analyzer):
    ciudades = analyzer['ciudades']
    ciudadesList = m.valueSet(ciudades)
    finalList = lt.newList('ARRAY_LIST')

    for ciudad in lt.iterator(ciudadesList):
        lt.addLast(finalList, ciudad)
   
    return finalList


def ufosCiudad(analyzer, ciudad):
    ufos = analyzer['ufos']
    llavesUfos = om.keySet(ufos)
    tree = om.newMap(omaptype ='RBT' , comparefunction = compareDatetimes)
    for datetime in lt.iterator(llavesUfos):
        ufo = om.get(ufos, datetime)['value']
        city = ufo['city']
        if city == ciudad:
            om.put(tree, ufo['datetime'], ufo)

    tam = om.size(tree)-1
    lista = lt.newList()
    i = 0
    while i < 3:
       llaveMinima = om.select(tree, i) 
       minima = om.get(tree, llaveMinima)['value']
       lt.addLast(lista, minima)
       i += 1

    j = tam-3
    while j < tam:
       llaveMaxima = om.select(tree, j) 
       maxima = om.get(tree, llaveMaxima)['value']
       lt.addLast(lista, maxima)
       j += 1 


    return lista, tam-1           



def ufosPorHoraMinutos(analyzer):
    horas = analyzer['horas']
    llavesHoras = m.keySet(horas)
    finalList = lt.newList('ARRAY_LIST')

    for hora in lt.iterator(llavesHoras):
        cantidad = m.get(horas, hora)['value']
        contador = {'hora': hora, 'contador': cantidad}
        lt.addLast(finalList, contador)


    return finalList


def ufosRangoHoras(analyzer, hora1, hora2):
    ufos = analyzer['ufos']
    valuesUfos = om.valueSet(ufos)
    tree = om.newMap(omaptype ='RBT' , comparefunction = compareDatetimes)

    for ufo in lt.iterator(valuesUfos):
        hora = str( str(ufo['datetime'][11]) + str(ufo['datetime'][12]) + str(ufo['datetime'][13]) + str(ufo['datetime'][14]) 
              + str(ufo['datetime'][15]) + str(ufo['datetime'][16]) + str(ufo['datetime'][17]) + str(ufo['datetime'][18])  )
        if hora >= hora1 and hora <= hora2:
            om.put(tree, ufo['datetime'], ufo)

    tam = om.size(tree)-1
    lista = lt.newList()
    i = 0
    while i < 3:
       llaveMinima = om.select(tree, i) 
       minima = om.get(tree, llaveMinima)['value']
       lt.addLast(lista, minima)
       i += 1

    j = tam-3
    while j < tam:
       llaveMaxima = om.select(tree, j) 
       maxima = om.get(tree, llaveMaxima)['value']
       lt.addLast(lista, maxima)
       j += 1 

    return lista, tam+1 
       

def ufosPorFechas(analyzer):
    fechas = analyzer['fechas']
    llavesfechas = m.keySet(fechas)
    finalList = lt.newList('ARRAY_LIST')

    for fecha in lt.iterator(llavesfechas):
        cantidad = m.get(fechas, fecha)['value']
        contador = {'fecha': fecha, 'contador': cantidad}
        lt.addLast(finalList, contador)

    return finalList


def ufosRangoFechas(analyzer, fecha1, fecha2):
    ufos = analyzer['ufos']
    valuesUfos = om.valueSet(ufos)
    tree = om.newMap(omaptype ='RBT' , comparefunction = compareDatetimes)

    for ufo in lt.iterator(valuesUfos):
        fecha = int( str(ufo['datetime'][0]) + str(ufo['datetime'][1]) + str(ufo['datetime'][2]) + str(ufo['datetime'][3]) 
              + str(ufo['datetime'][5]) + str(ufo['datetime'][6]) + str(ufo['datetime'][8]) + str(ufo['datetime'][9])  )

        if fecha >= int(fecha1) and fecha <= int(fecha2):
            om.put(tree, ufo['datetime'], ufo)

    tam = om.size(tree)-1
    lista = lt.newList()
    i = 0
    while i < 3:
       llaveMinima = om.select(tree, i) 
       minima = om.get(tree, llaveMinima)['value']
       lt.addLast(lista, minima)
       i += 1

    j = tam-3
    while j < tam:
       llaveMaxima = om.select(tree, j) 
       maxima = om.get(tree, llaveMaxima)['value']
       lt.addLast(lista, maxima)
       j += 1 

    return lista, tam+1 


def ufosZonaGeografica(analyzer, latitudInferior, latitudSuperior, longitudInferior, longitudSuperior):
    ufos = analyzer['ufos']
    llavesUfos = om.keySet(ufos)
    tree = om.newMap(omaptype ='RBT' , comparefunction = compareDatetimes)

    for llaveUfo in lt.iterator(llavesUfos):
        ufo = om.get(ufos, llaveUfo)['value']
        latitud = float(ufo['latitude'])
        longitud = float(ufo['longitude'])

        if latitud > latitudInferior and latitud < latitudSuperior and abs(longitud) > abs(longitudInferior) and abs(longitud) < abs(longitudSuperior):
           om.put(tree, ufo['datetime'], ufo)

    tam = om.size(tree)-1
    lista = lt.newList()
    i = 0
    while i < 3:
       llaveMinima = om.select(tree, i) 
       minima = om.get(tree, llaveMinima)['value']
       lt.addLast(lista, minima)
       i += 1

    j = tam-3
    while j < tam:
       llaveMaxima = om.select(tree, j) 
       maxima = om.get(tree, llaveMaxima)['value']
       lt.addLast(lista, maxima)
       j += 1 

    return lista, tam+1          




# ==============================
# Funciones de ordenamiento
# ==========

def sortUfosByCities(list):
    ms.sort(list, compareSize)

def sortHours(list):
    ms.sort(list, compareHours)  

def sortDates(list):
    ms.sort(list, compareDates)      

# ==============================
# Funciones de Comparacion
# ==============================

def compareDatetimes(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareHours(hour1, hour2):
    return hour1['hora'] > hour2['hora']      

def compareSize(size1, size2):
    return  size1['cantidad'] > size2['cantidad'] 

def compareDates(date1, date2):

    firstDate = int( str(date1['fecha'][0]) + str(date1['fecha'][1]) + str(date1['fecha'][2]) + str(date1['fecha'][3]) 
              + str(date1['fecha'][5]) + str(date1['fecha'][6]) + str(date1['fecha'][8]) + str(date1['fecha'][9])  )

    secondDate = int( str(date2['fecha'][0]) + str(date2['fecha'][1]) + str(date2['fecha'][2]) + str(date2['fecha'][3]) 
              + str(date2['fecha'][5]) + str(date2['fecha'][6]) + str(date2['fecha'][8]) + str(date2['fecha'][9])  )           

    return secondDate > firstDate


