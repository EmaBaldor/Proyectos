import requests as re
from bs4 import BeautifulSoup
import pandas as pd
from collections import namedtuple

Articulo = namedtuple('Articulo',['nombre','precio'])

lista_articulos=[]

response = re.get('https://listado.mercadolibre.com.ar/notebook#D[A:notebook]')
html = response.text

html_soup = BeautifulSoup(html, 'html.parser')

articulos_mercado = html_soup.find_all('li', class_='ui-search-layout__item shops__layout-item')

for articulo in articulos_mercado:
    nombre = articulo.find('h2', class_='ui-search-item__title shops__item-title').text
    precio = articulo.find('span', class_='andes-money-amount__fraction').text
    lista_articulos.append(Articulo(nombre, precio))

def obtener_precio_float(articulo):
    try:
        return float(articulo.precio.replace('.', '').replace(',', '.'))
    except ValueError:
        return float('inf')  # Valor infinito para manejar casos donde no se puede convertir a número

lista_articulos_ordenados = sorted(lista_articulos, key=obtener_precio_float)

print("Lista de Artículos ordenados por precio:")
for articulo in lista_articulos_ordenados:
    print(f"Nombre: {articulo.nombre}")
    print(f"Precio: {articulo.precio}")
    print()
print(f'Total articulos: {len(lista_articulos_ordenados)}')