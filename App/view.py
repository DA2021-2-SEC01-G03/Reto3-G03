
import config as cf
import sys
import controller
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
assert cf


ufosFile = 'UFOS/UFOS-utf8-small.csv'
cont = None


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
        analyzer = controller.init()
        print("Inicializando analizador")
        

    elif int(inputs[0]) == 2:
        print("\nCargando información de ufos ....")
        data = controller.loadData(analyzer, ufosFile)
        print("La altura del rbt es de: " + str(om.height(data['ufos'])))
        print("El número de elementos es de: " + str(om.size(data['ufos'])))   
        
  

    else:
        sys.exit(0)
sys.exit(0)
