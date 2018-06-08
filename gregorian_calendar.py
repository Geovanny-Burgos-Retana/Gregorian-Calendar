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
    if fecha_es_tupla(date):
        raise Exception("Tupla de fecha con formato incorrecto")
    return (anno_permitido(date[0]) #Año dentro del rando permitido
       and 1 < date[1] < 12 #Mes dentro del rando permitido
       and (1 < date[2] < days_of_month[date[2]] #Días dentro de rango permitido según el mes
            or (date[1] == 2 and bisiesto(date[0] and date[2] == 29)))) #Excepción del día 29/02 si el año es bisiesto

# Retorna una fecha con el día siguiente a la ingresada
def dia_siguiente(date: tuple) -> tuple:
    if fecha_es_valida(date):
        raise Exception("Fecha invalida")
    if date[2] < days_of_month[date[1]] or (date[1] == 2 and bisiesto(date[0] and date[2] == 28)):
        date[2] += 1 #Todo caso de no cambia de mes solo se aumenta en uno los días de la fecha
    else:
        date[2] = 1
        if date[1] != 12:
            date[1] += 1 #Solo si no hay cambio de año se aumenta en uno los mesese
        else:
            date[1] = 1
            date[0] += 1
    return date

# Retorna la cantidad de días pasados desde el primero
# de enero del año ingresado en la tupla
def dias_desde_primero_enero(date: tuple) -> int:
    if fecha_es_valida(date):
        raise Exception("Fecha invalida")
    days = -1 #Porque (año, 1, 1) -> 0, es decir que -1 + 1 = 0 según el algoritmo (*)
    # Se suma directamente los días de cada mes anterior al mes ingresado
    # en la tupla y se termina sumando los días de la tupla
    for month, days_month in days_of_month.items():
        if month < date[1]:
            days += days_month
        else:
            if bisiesto(date[0]) and date[1] > 2:
                days = 0
            days += date[2] # (*)
            return days

