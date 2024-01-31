# Pasos para Analizar Datos
# 1. Importar el paquete  p paquetes con los que voy a analizar la información

import pandas as pd
from helpers.creacionTabla import crearTabla

def analizarSiembraBasica():
    # 2. Sin importar la fuente (sql, xls, JSON, csv...)
    # Crear una tabla tabulada que se llama DATAFRAME

    tabla=pd.read_csv('./data/Siembras.csv')

    crearTabla(tabla,"siembrabasica")

    #print(tabla)

    # 3. Aplico filtros para limpiar o seleccionar datos

    #print(tabla.head()) # .head muestra los primeros 5 datos

    #print(tabla.head(20)) # imprime los primeros N registros

    #print(tabla.tail()) # imprime los ultimos 5 registros

    #print(tabla.describe()) # Informacion basica descriptiva de todos los datos

    #Arboles sembrados en Medellin con(arboles sembrados) mayores a 200
    filtroArbol=tabla.query("(Ciudad=='Medellín') and (Arboles > 200)")
    crearTabla(filtroArbol,'filtroarbol')
    
    #Santa fe de Antioquia veredas paso real y Tonusco Arriba
    filtroVereda=tabla.query("(Ciudad=='Santa Fe de Antioquia') and(Vereda=='Paso Real')and (Vereda=='Tonusco Arriba')")
    crearTabla(filtroVereda,'filtrovereda')

    #Siembra en el Bagre mayores a 60 arboles
    #filtroBagre=tabla.query("(Ciudad=='Bagre') and (Arboles >60)")
    #crearTabla(filtroBagre,'filtrobagre')

    #Santa Rosa de osos las 
    