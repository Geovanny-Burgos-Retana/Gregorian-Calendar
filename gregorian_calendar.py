## ----------------------------------
## | Thu Jun 00:51:10 2018          |
## | Version: 1.0.0                 |
## | Autor: Geovanny Burgos Retana  |
## | Email: gretana2@gmail.com      |
## ----------------------------------

days_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Retorna True cuando la fecha sea una tupla
# de tres enteros.
def fecha_es_tupla(date: tuple) -> bool:
    return (isinstance(date, tuple)
       and len(date) == 3
       and isinstance(date[0], int)
       and isinstance(date[1], int)
       and isinstance(date[2], int))

# Retorna True cuando el año sea mayor a 1582
# fecha en que empieza a regir el calendario.
def anno_permitido(year: int) -> bool:
    return year >= 1582

# Ref: https://es.wikibooks.org/wiki/Algoritmo_bisiesto
# Un año es bisiesto en el calendario Gregoriano, si es divisible
# entre 4, excepto aquellos divisibles entre 100 pero no entre 400.
def bisiesto(year: int) -> bool:
    return (year%4 == 0
       and (year%100 != 0 or year%400 == 0))

# Retorna True cuando cumpla con todas las
# validaciones detallas en el algoritmo.
def fecha_es_valida(date: tuple) -> bool:
    if fecha_es_tupla(date[0]):
        raise Exception("Tupla de fecha con formato incorrecto")
    return (anno_permitido(date[0]) #Año dentro del rando permitido
       and 1 < date[1] < 12 #Mes dentro del rando permitido
       and (1 < date[2] < days_of_month[date[2]] #Días dentro de rango permitido según el mes
            or (date[1] == 2 and bisiesto(date[0] and date[2] == 29)))) #Excepción del día 29/02 si el año es bisiesto

