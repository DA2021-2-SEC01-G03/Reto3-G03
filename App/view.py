
import config as cf
import sys
import controller
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
assert cf


ufosFile = 'UFOS/UFOS-utf8-large.csv'
cont = None


def initAnalyzer():
    analyzer = controller.init()

    return analyzer


def loadData(analyzer, ufosFile):
    data = controller.loadData(analyzer, ufosFile)

    return data


def ufosCiudad(analyzer, ciudad):
    listaCiudades = controller.cantidadUfosCiudades(analyzer)
    controller.sortUfosByCities(listaCiudades)
    top5 = lt.subList(listaCiudades, 1, 5)
    print("There are " + str(lt.size(listaCiudades)) + " different cities with ufo sightings...")
    print("The top 5 cities with most ufo sghtings are: ")
    for city in lt.iterator(top5):
        print(city['ciudad'] + ": " + str(city['cantidad']))

    amountUfosCiudad = controller.ufosCiudad(analyzer, ciudad)[1]
    lista = controller.ufosCiudad(analyzer, ciudad)[0] 

    print("")
    print("There are " + str(amountUfosCiudad) + " sightings at " + str(ciudad) + " city.")
    print("The first 3 and last 3 UFO sightings are:") 
    
    for ufo in lt.iterator(lista):
        print( 'datetime: ' + str(ufo['datetime']) + ', city: ' + str(ufo['city']) + ', state:'+ str(ufo['state'] 
        + ', country:' + str(ufo['country']) + ', shape:' + str(ufo['shape']) + ', duration (seconds):' + 
        str(ufo['duration (seconds)'])) )

    
def ufosPorHoraMinutos(analyzer, limiteInferior, limiteSuperior):
    lista = controller.ufosPorHoraMinutos(analyzer)
    controller.sortByHours(lista)
    print("There are " + str(lt.size(lista)) + " different UFO sightings times [hh:mm:ss]..." )  
    print("The 5 latest times for UFO sightings are:")
    if lt.size(lista) > 4:
      top5 = lt.subList(lista, 1, 5)
      for hour in lt.iterator(top5):
        print( str(hour['hora']) + ": " + str(hour['contador']))
    else:
      for hour in lt.iterator(lista):
        print( str(hour['hora']) + ": " + str(hour['contador']))

    print("")
    listaRangoHoras = controller.ufosPorRangoHoras(analyzer, limiteInferior, limiteSuperior)[0]
    amountHoras = controller.ufosPorRangoHoras(analyzer, limiteInferior, limiteSuperior)[1]
    print("There are " + str(amountHoras) + " sightings between " + str(limiteInferior) + " and " + str(limiteSuperior) )
    print("The first 3 and last 3 UFO sightings in this time are:")
    for ufo in lt.iterator(listaRangoHoras):
        print( 'datetime: ' + str(ufo['datetime']) + ', city: ' + str(ufo['city']) + ', state:'+ str(ufo['state'] 
        + ', country:' + str(ufo['country']) + ', shape:' + str(ufo['shape']) + ', duration (seconds):' + 
        str(ufo['duration (seconds)'])) )






def ufosPorFechas(analyzer, limiteInferior, limiteSuperior):
    lista = controller.ufosPorFechas(analyzer)
    controller.sortByDates(lista)
    print("There are " + str(lt.size(lista)) + " different UFO sightings dates [YYYY-MM-DD]..." )  
    print("The oldest 5 dates for UFO sightings are:")
    if lt.size(lista) > 4:
      top5 = lt.subList(lista, 1, 5)
      for hour in lt.iterator(top5):
        print( str(hour['fecha']) + ": " + str(hour['contador']))
    else:
      for hour in lt.iterator(lista):
        print( str(hour['fecha']) + ": " + str(hour['contador']))

    print("")
    listaRangoFechas = controller.ufosRangoFechas(analyzer, limiteInferior, limiteSuperior)[0]
    amountFechas = controller.ufosRangoFechas(analyzer, limiteInferior, limiteSuperior)[1]
    print("There are " + str(amountFechas) + " sightings between " + str(limiteInferior) + " and " + str(limiteSuperior) )
    print("The first 3 and last 3 UFO sightings in this time are:")
    for ufo in lt.iterator(listaRangoFechas):
        print( 'datetime: ' + str(ufo['datetime']) + ', city: ' + str(ufo['city']) + ', state:'+ str(ufo['state'] 
        + ', country:' + str(ufo['country']) + ', shape:' + str(ufo['shape']) + ', duration (seconds):' + 
        str(ufo['duration (seconds)'])) )


def ufosZonaGeografica(analyzer, latitudInferior, latitudSuperior, longitudInferior, longitudSuperior):
    lista = controller.ufosZonaGeografica(analyzer, latitudInferior, latitudSuperior, longitudInferior, longitudSuperior)[0]
    amountUfos = controller.ufosZonaGeografica(analyzer, latitudInferior, latitudSuperior, longitudInferior, longitudSuperior)[1]

    print("There are " + str(amountUfos) + " UFO sightings in the current area")
    print("")
    print("The first 3 and last 3 ufo sightings in this zone are:")
    for ufo in lt.iterator(lista):
        print( 'datetime: ' + str(ufo['datetime']) + ', city: ' + str(ufo['city']) + ', state:'+ str(ufo['state'] 
        + ', country:' + str(ufo['country']) + ', shape:' + str(ufo['shape']) + ', duration (seconds):' + 
        str(ufo['duration (seconds)'])) + ', latitude: ' + str(ufo['latitude']) + ', longitude: ' +
        str(ufo['longitude']) )

def ufosAvistamientosDur(analyzer, limiteMin, limiteMax):

    maxDuracion = controller.ufosMaximadur(analyzer)
    avistamientosEnRango = controller.avistamientosRango(analyzer, limiteMin, limiteMax)
    controller.sortByDurationAv(avistamientosEnRango)

    top3 = lt.subList(avistamientosEnRango, 0, 3)
    bottom3 = lt.subList(avistamientosEnRango, lt.size(avistamientosEnRango)-3,3)
    print( 'There are ' + str(om.size(analyzer['ufos'])) + ' different durations of ufo sightings') 
    print( 'The longest ufo sightings are: ')
    print('duration(seconds) - count')
    print(str(maxDuracion[0]) + ' | ' + str(maxDuracion[1]))
    print("There are " + str(lt.size(avistamientosEnRango)) + " UFO sightings between " + str(limiteMin) + ' and ' + str(limiteMax) + ' duration')
    print("The first 3 and last 3 ufo sightings in the duration time are:")
    for ufo in lt.iterator(top3):
        print( 'datetime: ' + str(ufo['datetime']) + ', city: ' + str(ufo['city']) + ', state:'+ str(ufo['state'] 
        + ', country:' + str(ufo['country']) + ', shape:' + str(ufo['shape']) + ', duration (seconds):' + 
        str(ufo['duration (seconds)'])) + ', latitude: ' + str(ufo['latitude']) + ', longitude: ' +
        str(ufo['longitude']) )
    
    for ufo in lt.iterator(bottom3):
        print( 'datetime: ' + str(ufo['datetime']) + ', city: ' + str(ufo['city']) + ', state:'+ str(ufo['state'] 
        + ', country:' + str(ufo['country']) + ', shape:' + str(ufo['shape']) + ', duration (seconds):' + 
        str(ufo['duration (seconds)'])) + ', latitude: ' + str(ufo['latitude']) + ', longitude: ' +
        str(ufo['longitude']) )



def printMenu():
    print("Bienvenido")
    print("1- Inicializar analizador")
    print("2- Cargar información de avistamientos")
    print("3- Contar los avistamientos en una ciudad")
    print("4- Contar los avistamientos por duración")
    print("5- Contar avistamientos por Hora/Minutos del día")
    print("6- Contar los avistamientos en un rango de fechas")
    print("7- Contar los avistamientos de una Zona Geográfica")
    print("8- Visualizar los avistamientos de una zona geográfica.")
    

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando analizador")
        analyzer = initAnalyzer()
        

    elif int(inputs[0]) == 2:
        data = loadData(analyzer, ufosFile)
        print("La altura del rbt es de: " + str(om.height(data['ufos'])))
        print("El número de elementos es de: " + str(om.size(data['ufos'])))  
        
    elif int(inputs[0]) == 3:
        ciudad = input("Ingrese la ciudad a buscar ")
        ufosCiudad(analyzer, ciudad)

    elif int(inputs[0]) == 4:
        limiteInferior = input("Ingrese limite de duración inferior ")
        limiteSuperior = input("Ingrese limite de duración superior ")
        ufosAvistamientosDur(analyzer,limiteInferior,limiteSuperior)
        
    elif int(inputs[0]) == 5:
        limiteInferior = input("Ingrese limite de hora inferior ")
        limiteSuperior = input("Ingrese limite de hora superior ")
        ufosPorHoraMinutos(analyzer, limiteInferior, limiteSuperior)


    elif int(inputs[0]) == 6:
        limiteInferior = input("Ingrese limite de fecha inferior (YYYYMMDD) ")
        limiteSuperior = input("Ingrese limite de fecha superior (YYYYMMDD) ")
        ufosPorFechas(analyzer, limiteInferior, limiteSuperior)    

    elif int(inputs[0]) == 7:
        latitudInferior = float(input("Ingrese limite inferior de latitud "))
        latitudSuperior = float(input("Ingrese el limite superior de latitud "))
        longitudInferior = float(input("Ingrese el limite inferior de longitud "))
        longitudSuperior = float(input("Ingrese el limite superior de longitud "))
        ufosZonaGeografica(analyzer, latitudInferior, latitudSuperior, longitudInferior, longitudSuperior)




        
    else:
        sys.exit(0)

