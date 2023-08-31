#Extraccion de datos de la url: https://es.wikipedia.org/wiki/Am%C3%A9rica
import requests
from bs4 import BeautifulSoup
import csv
import codecs

url = 'https://es.wikipedia.org/wiki/Am%C3%A9rica'

#Realizae una solicitud get a la url
responce = requests.get(url)

#Verificar si la solicitud fue exitosa (Codigo de estado 200)
if responce.status_code == 200:
    #Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(responce.content, 'html.parser')

    #Encontrar la tabla de paises y poblacion 
    table = soup.find('table', {'class': 'wikitable'})

    #Crear archivo csv llamado "paises.csv" en modo escritura
    #with open('paises.csv', 'w', newline='', encoding='utf-8') as csvfile:
    with codecs.open('paises2.csv', 'w', 'utf-8-sig') as csvfile:   
        archivo = csv.writer(csvfile)

        #Escribir encabezados
        archivo.writerow(['Pais', 'Poblacion','Independencia', 'Capital'])

        #Iterar sobre las filas de la tabla 
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')

            pais = columns[2].text.strip()
            poblacion = columns[5].text.strip()
            fecha_independencia = columns[3].text.strip()
            if(len(columns)>7):
                capital = columns[7].text.strip()
            else: 
                capital=0

            print("Pais:" , pais, "Poblacion:", poblacion,"Independencia:", fecha_independencia, "Capital:", capital)
            archivo.writerow([pais,poblacion,fecha_independencia,capital])
    
        print("El archivo fue creado correctamente.")


else:
    print(f"Error al acceder a la pagina. Codigo de estado: {responce.status_code}")