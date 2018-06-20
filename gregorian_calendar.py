## ----------------------------------
## | Thu Jun 00:51:10 2018          |
## | Version: 1.0.0                 |
## | Autor: Geovanny Burgos Retana  |
## | Email: gretana2@gmail.com      |
## ----------------------------------

days_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# ---------------------- R0 ----------------------
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

# ---------------------- R1 ----------------------
# Ref: https://es.wikibooks.org/wiki/Algoritmo_bisiesto
# Un año es bisiesto en el calendario Gregoriano, si es divisible
# entre 4, excepto aquellos divisibles entre 100 pero no entre 400.
def bisiesto(year: int) -> bool:
    return (year%4 == 0
       and (year%100 != 0 or year%400 == 0))

# ---------------------- R2 ----------------------
# Retorna True cuando cumpla con todas las
# validaciones detallas en el algoritmo.
def fecha_es_valida(date: tuple) -> bool:
    if not fecha_es_tupla(date):
        raise Exception("Tupla de fecha con formato incorrecto")
    return (anno_permitido(date[0]) #Año dentro del rando permitido
       and 1 <= date[1] <= 12 #Mes dentro del rando permitido
       and (1 <= date[2] <= days_of_month[date[1]] #Días dentro de rango permitido según el mes
            or (date[1] == 2 and bisiesto(date[0]) and date[2] == 29))) #Excepción del día 29/02 si el año es bisiesto

# ---------------------- R3 ---------------------- V1
# Retorna una fecha con el día siguiente a la ingresada
def dia_siguiente(date: tuple) -> tuple:
    if not fecha_es_valida(date):
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

# ---------------------- R3 ---------------------- V2
# Versión mas resumida pero debo comparar cual es mas rápida
def dia_siguiente(date: tuple) -> tuple:
    if not fecha_es_valida(date):
        raise Exception("Fecha invalida")
    return int_parse_date(date_parse_int(date[0], date[1], date[2]) + 1)

# ---------------------- R4 ----------------------
# Retorna la cantidad de días pasados desde el primero
# de enero del año ingresado en la tupla
def dias_desde_primero_enero(date: tuple) -> int:
    if not fecha_es_valida(date):
        raise Exception("Fecha invalida")
    days = -1 #Porque (año, 1, 1) -> 0, es decir que -1 + 1 = 0 según el algoritmo (*)
    # Se suma directamente los días de cada mes anterior al mes ingresado
    # en la tupla y se termina sumando los días de la tupla
    for month, days_month in days_of_month.items():
        if month < date[1]:
            days += days_month
        else:
            if bisiesto(date[0]) and date[1] > 2:
                days += 1
            days += date[2] # (*)
            return days

# ---------------------- R5 ----------------------
# Retorna el día de la semana del primero de enero del año ingresado
def dia_primero_enero(year):
    return dia_semana((year, 1, 1))

# ---------------------- R9 ----------------------
# Ref: https://es.wikipedia.org/wiki/Congruencia_de_Zeller
# Retorna un entero que significa el día de la semana de la
# fecha ingresada (0 = Domingo, 1 = Lunes, así sucesivamente)
def dia_semana(date: tuple) -> int:
    if not fecha_es_valida(date):
        raise Exception("Fecha invalida")
    q = date[2]
    m = date[1]
    annio = date[0]
    if(m == 1 or m == 2):
        m += 12
        annio -= 1
    k = annio%100
    j = annio//100
    h = (q+(((m+1)*26)//10)+k+(k//4)+(j//4)-2*j)
    return (h-1)%7

# ---------------------- R7 ----------------------
# Retorna una fecha n días despues de la ingresada
def fecha_futura(date: tuple, days: int) -> tuple:
    if not fecha_es_valida(date):
        raise Exception("Fecha invalida")
    return int_parse_date((date_parse_int(date[0], date[1], date[2]) + days))

# Ref: https://alcor.concordia.ca//~gpkatch/gdate-algorithm.html
# Calcula el numero entero para una fecha dada, luego se puede
# hacer ingeniería inversa con la siguiente función
def date_parse_int(y: int, m: int, d: int):
    m = (m + 9) % 12
    y = y - m//10
    return 365*y + y//4 - y//100 + y//400 + (m*306 + 5)//10 + ( d - 1 )

# Ref: https://alcor.concordia.ca//~gpkatch/gdate-algorithm.html
# Ingeniería inversa de la función anterior
def int_parse_date(g: int):
    y = (10000*g + 14780)//3652425    
    ddd = g - (365*y + y//4 - y//100 + y//400)
    if (ddd < 0):
        y = y - 1
        ddd = g - (365*y + y//4 - y//100 + y//400)
    mi = (100*ddd + 52)//3060
    mm = (mi + 2)%12 + 1
    y = y + (mi + 2)//12
    dd = ddd - (mi*306 + 5)//10 + 1
    return (y, mm, dd)

# ---------------------- R8 ----------------------
# Retorna la cantidad de días entre dos fechas
def dias_entre(date1: tuple, date2: tuple) -> int:
    if not (fecha_es_valida(date1) and (fecha_es_valida(date2))):
        raise Exception("Fecha invalida")
    return abs(date_parse_int(date2[0], date2[1], date2[2]) - date_parse_int(date1[0], date1[1], date1[2]))

    
