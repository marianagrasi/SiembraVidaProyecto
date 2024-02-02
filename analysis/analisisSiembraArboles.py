# Pasos para Analizar Datos
# 1. Importar el paquete  p paquetes con los que voy a analizar la información

import pandas as pd
from helpers.creacionTabla import crearTabla
from helpers.creacionGrafica import generarGrafica
from helpers.creacionGraficaDos import generarGraficaSum
from helpers.creacionGraficaTres import generarGraficaSuma

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
    filtroVereda=tabla.query("(Ciudad=='Santa Fe de Antioquia') and(Vereda=='Paso Real') or (Ciudad=='Santa Fe de Antioquia') and (Vereda=='Tonusco Arriba')")
    crearTabla(filtroVereda,'filtrovereda')

    #Siembra en el Bagre mayores a 60 arboles
    filtroBagre=tabla.query("(Ciudad=='El Bagre') and (Arboles >60)")
    crearTabla(filtroBagre,'filtrobagre')

    #Santa rosa de osos vereda las cruces y mina vieja
    filtroSantaRosa=tabla.query("(Ciudad=='Santa Rosa de Osos') and (Vereda=='Mina Vieja') or(Ciudad=='Santa Rosa de Osos') and (Vereda=='Las Cruces')")
    crearTabla(filtroSantaRosa,'filtrosantarosa')

    #Filtrat todo lo de Yondó
    filtroYondo=tabla.query("(Ciudad=='Yondó')")
    crearTabla(filtroYondo,'filtroYondo')
    






    filtroArboles=tabla.query("(Ciudad=='Medellín') and (Arboles>0) or (Ciudad=='Santa Fe de Antioquia') and (Arboles>0) or (Ciudad=='El Bagre') and (Arboles>0) or (Ciudad=='Santa Rosa de Osos') and (Arboles>0) or (Ciudad=='Yondó') and (Arboles>0) ")
    generarGrafica(filtroArboles)

    filtroCantidadArboles=tabla.query("(Ciudad=='Andes') and (Arboles>0) or (Ciudad=='Medellín') and (Arboles>0)")
    generarGraficaSum(filtroCantidadArboles)

    filtroEspecieArboles=tabla.query("(Ciudad=='Barbosa') and (Hectareas > 0) or (Ciudad=='Medellín') and (Hectareas > 0) or (Ciudad=='Bello') and (Hectareas > 0)  ")
    generarGraficaSuma(filtroEspecieArboles)




