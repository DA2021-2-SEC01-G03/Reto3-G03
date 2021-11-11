

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, ufosFile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    ufosFile = cf.data_dir + ufosFile
    input_file = csv.DictReader(open(ufosFile, encoding="utf-8"),
                                delimiter=",")
    for ufo in input_file:
        model.addUfo(analyzer, ufo)
        model.llenarCiudades(analyzer, ufo)
        model.llenarHoras(analyzer, ufo)
        model.llenarFechas(analyzer, ufo)
    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def cantidadUfosCiudades(analyzer):
    return model.cantidadUfosCiudades(analyzer)

def ufosCiudad(analyzer, ciudad):
    return model.ufosCiudad(analyzer, ciudad)  

def ufosPorHoraMinutos(analyzer):
    return model.ufosPorHoraMinutos(analyzer)  

def ufosPorRangoHoras(analyzer, hora1, hora2):
    return model.ufosRangoHoras(analyzer, hora1, hora2)

def ufosPorFechas(analyzer):
    return model.ufosPorFechas(analyzer)

def ufosRangoFechas(analyzer, fecha1, fecha2):
    return model.ufosRangoFechas(analyzer, fecha1, fecha2)

def ufosZonaGeografica(analyzer, latitudInferior, latitudSuperior, longitudInferior, longitudSuperior):
    return model.ufosZonaGeografica(analyzer, latitudInferior, latitudSuperior, longitudInferior, longitudSuperior)    



# ___________________________________________________
#  Funciones de ordenamiento
# ___________________________________________________

def sortUfosByCities(list):
    return model.sortUfosByCities(list)

def sortByHours(list):
    return model.sortHours(list)   

def sortByDates(list):
    return model.sortDates(list)   
