import pandas as pd
from bs4 import BeautifulSoup

def crearTabla(dataFrame,nombreTabla):

    # Obtener una tabla de HTML desde un DataFrame de python
    archivoHTML=dataFrame.to_html()

    # Definir la ruta donde se va a guardar esa tabla
    rutaArchivo=f"tables/{nombreTabla}.html"

    # Construir un encabezado <head> del archivo generado
    encabezadoHTML=''' 
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>tablas</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            </head>
        </html>
    '''

    # Utilizo BS4 para optimizar mi tabla
    sopa=BeautifulSoup(archivoHTML,'html.parser')

    # Encontrar todas las FILAS 'tr' eliminar un atributo que le pone por defecto python style
    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)

    archivoHTML=str(sopa)

    # Agregar la clase table y table striped de bootstrap
    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')

    # Escribir la tabla y generarla en el proyecto
    with open(rutaArchivo,"w",encoding='utf-8') as archivo:
        archivo.write(f"{encabezadoHTML}\n{archivoHTML}\n</body>\n</html>")

    # Se adiciona encoding='utf-8' en la linea 37 para que reconozca las tildes en la tabla