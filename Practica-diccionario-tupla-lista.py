lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]


def ordenar(lista_personas):
    """ El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    return sorted(lista_personas, reverse=False,key=lambda edad : edad[3])


def convertir_a_diccionario(lista_personas):
    """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad"""

    clave = []
    valores = []

    for l in lista_personas:
        clave.append(l[0])
        valores.append(l[1:4])

    dic = dict(zip(clave,valores)) 

    return dic

 

def devolver_edad(lista_personas, dni):
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""

    dic = convertir_a_diccionario(lista_personas)
    valores = list(dic[dni])

    return valores[2]


def eliminar_repetidos(lista_personas):
    """ El metodo debe devolver los elementos unicos """

    sin_repetidos = set(lista_personas)

    return sin_repetidos


def separar_por_edad(lista_personas):
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    mayor = []
    menor = []

    for l in lista_personas:

        if l[3] >= 25:
            mayor.append(l)
        else:
            menor.append(l)

    return mayor, menor


def obtener_promedio(lista):
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    edades = []

    for l in lista:
        edades.append(l[3])
    try:
        prom = sum(edades)/len(edades)
        return prom
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
   

def main():
    """Este metodo no debe modificarse y es solo a fines de probar el codigo""" 
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))
    
if __name__ == "__main__":
    main()

