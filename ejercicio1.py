import requests
from bs4 import BeautifulSoup

# URL de la página de noticias
url = 'https://www.losandes.com.pe/'

# Realiza una solicitud GET a la URL
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra el div contenedor que contiene todas las noticias
    div_contenedor = soup.find('div', class_='jeg_wrapper wpb_wrapper')

    # Encuentra los elementos <div> con la clase 'jeg_heroblock_wrapper' dentro del div grande
    divs_noticias = div_contenedor.find_all('div', class_='jeg_posts_wrap')

    # Itera sobre los elementos <div> individuales que contienen las noticias
    for div_noticia in divs_noticias:
        # Encuentra los títulos <h2> dentro del <div> de la noticia
        titulos = div_noticia.find_all('h2')

        # Encuentra las fechas dentro del <div> de la noticia usando la etiqueta <i> y la clase 'fa fa-clock-o'
        fechas = div_noticia.find_all('i', class_='fa fa-clock-o')

        # Itera sobre los títulos y las fechas e imprímelos
        for titulo, fecha in zip(titulos, fechas):
            titulo_texto = titulo.text.strip()
            fecha_texto = fecha.next_sibling.strip()  # Obtener el texto del hermano siguiente del <i>

            print("Título:", titulo_texto)
            print("Fecha:", fecha_texto)
            print()

else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
