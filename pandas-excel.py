import pandas as pd

try:
    # Leer archivo Excel
    df = pd.read_excel('datos.xlsx')

    # Filtrar y ordenar los datos
    df = df[df['columna1'] > 5]
    df = df.sort_values('columna2')

    # Agrupar los datos por una columna y calcular
    df_agrupado = df.groupby('columna3').agg({'columna4': 'sum', 'columna5': 'mean'})

    # Crear una tabla dinámica a partir de los datos
    tabla_dinamica = pd.pivot_table(df_agrupado, index='columna3', values=['columna4', 'columna5'], aggfunc=[sum, len])

    # Escribir los datos en un nuevo archivo Excel
    with pd.ExcelWriter('resultados.xlsx') as writer:
        df.to_excel(writer, sheet_name='Datos filtrados', index=False)
        df_agrupado.to_excel(writer, sheet_name='Datos agrupados')
        tabla_dinamica.to_excel(writer, sheet_name='Tabla dinámica')

except FileNotFoundError:
    print('El archivo no se pudo encontrar. Verifica la ruta y el nombre del archivo.')

"""
primero importamos la librería Pandas con import pandas as pd. Luego, utilizamos la función read_excel para leer un archivo Excel llamado datos.xlsx y almacenamos los datos en un DataFrame llamado df.

A continuación, realizamos varias operaciones en los datos del archivo, como filtrar y ordenar los datos. Luego, utilizamos la función groupby para agrupar los datos por la columna 'columna3' y calcular la suma de la columna 'columna4' y el promedio de la columna 'columna5'.

Después, utilizamos la función pivot_table para crear una tabla dinámica a partir de los datos agrupados y la guardamos en una variable llamada tabla_dinamica.

Finalmente, utilizamos la función ExcelWriter para escribir los datos del DataFrame original, los datos agrupados y la tabla dinámica en un nuevo archivo Excel llamado resultados.xlsx, con cada conjunto de datos en una hoja diferente dentro del archivo.

"""