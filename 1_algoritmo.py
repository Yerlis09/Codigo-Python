# Construir una función que reciba como parametro un entero y retorne su ultimo digito
def retornar_ultimo_digito(numero):
    ultimo_digito = numero %  10
    return ultimo_digito

resultado = retornar_ultimo_digito(18)
print('El ultimo digito es: %i' %resultado)

# Construir un funcion que reciba como parametro un entero y retorne sus dos ultimos digitos

def retornar_ultimo_dos_digitos(numero):
    if(numero == None):
        return 'Ingrese un valor valido, por favor'
    elif(numero == ""): 
        return 'ingrese un valor por favor'
    elif (numero > -100) and (numero < 100):
        return 'Ingrese un valor menor a -100 y mayor a 100'
    else:
        dos_ultimos_digitos = str(numero)[-2:]
        return dos_ultimos_digitos

resultado = retornar_ultimo_dos_digitos(1550)
print( resultado)

# Construir una funcion que reciba como parametro un entero y retorne la cantidad de digitos

def retornar_cantidad_de_digitos(numero):
    if (numero == None):
        return 'Ingrese un valor valido'
    elif (numero == ''):
        return 'Ingrese un valor, por favor'
    elif (numero < 0):
        longitud = len(str(numero))-1
        return longitud
    else:
        longitud = len(str(numero))
        return longitud
resultado = retornar_cantidad_de_digitos(-325)
print(resultado)

# construir una funcion que reciba como parametro un entero y retorne la cantidad de digitos pares

def retornar_cantidad_de_digitos_pares(numero):
    if (numero == None):
        return 'Ingrese un valor valido'
    elif (numero == ''):
        return 'Ingrese un valor' 
    elif (numero < 0):
        return 'Ingrese un numero entero positivo'
    elif (numero == 1):
        return 0
    else:
        cont = 0
        for i in range(2,numero):
            if (i % 2 == 0):
                cont +=1
        return cont

resultado = retornar_cantidad_de_digitos_pares(10)
print(resultado)

# Construir una funcion que reciba como parametro un entero y retorne la cantidad de digitos primos

def retornar_si_es_primo(numero): # Funcion que permite verificar si el número ingresado es primo o no
    if (numero > 1):
        for i in range(2,numero):
            if( numero % i == 0):
                return False      
        return True

def retornar_cantidad_digitos_primos(numero): # Funcion que permite hallar la cantidad de números primo
    if (numero == None):
        return 'Ingrese un valor valido'
    elif (numero == ''):
        return 'Ingrese un valor' 
    elif (numero < 0):
        return 'Ingrese un numero entero positivo'
    elif (numero == 1) :
        return 0
    if (numero == 2):
        return 1
    count = 0
    for i in range(2, (numero + 1)):
        if (retornar_si_es_primo(i)):
            count += 1
    return count

resultado = retornar_cantidad_digitos_primos(None)
print(resultado)

# Construir una funcion que reciba como parametro un entero y retorne el codigo ASCII asociado a el

def retornar_codigo_ascii_del_entero(entero):
    if (entero == None):
        return('Ingrese un valor valido, por favor')
    elif (entero == ''):
        return 'Ingrese un valor, por favor'
    elif (type(entero) == str):
        return 'Ingrese un entero positivo, por favor'
    elif (entero < 0):
        return 'Ingrese un valor superior a -1, por favor'
    else:
        codigo_ascii = chr(entero)
        return codigo_ascii

resultado = retornar_codigo_ascii_del_entero(36)
print(resultado)

def obtener_catidad_digitos(numero = 0): 
    if isinstance(numero, str):
        return 'Solo se aceptan numeros.'

    cantidad_digitos = 0
    while numero > 0:
        cantidad_digitos += 1
        numero = int(numero / 10)
    return cantidad_digitos

print(obtener_catidad_digitos(25))
print(obtener_catidad_digitos('Yerlis'))
print(obtener_catidad_digitos(False))

#leer dos numeros enteros y determinar cual es el mayor

def determinar_cual_es_el_numero_mayor(numero1, numero2):
    if not numero1 or not numero2:
        return('ingrese valores validos, por favor')
    else:
        return max(numero1, numero2)
resultado = determinar_cual_es_el_numero_mayor(25,89)
print(resultado)


# Leer un numero entero de dos digitos y determinar si los dos digitos son iguales.

def determinar_si_dos_digitos_son_iguales(numero = 0):
    if (numero == None):
        return('ingrese valores validos, por favor')
    elif (numero == ''):
        return 'ingrese un valor, por favor'
    elif isinstance(numero, str):
        return 'No se permite este tipo de dato'
    elif (numero < 10):
        return 'Ingrese un numero entero mayor a 9'
    else:
        str_numero = (str(numero))
        if (str_numero[0] == str_numero[1]):
            return 'Son iguales'
        else:
            return 'No son iguales'

resultado = determinar_si_dos_digitos_son_iguales(33)
print(resultado)

# Leer dos numeros enteros de dos digitos y determinar si la suma de los dos numeros origina un numero par

def determinar_si_la_suma_origina_un_numero_par(numero1 = 0, numero2 = 0):
    if not numero1 or not numero2:
        return('ingrese valores validos, por favor')
    elif numero1 < 10 or numero2 < 10:
            return 'Ingrese un valor de dos digitos, por favor'
    else: 
        resultado_suma = numero1 + numero2
        if (resultado_suma % 2 == 0):
            return 'Es par'
        else: 
            return 'No es par'

resultado = determinar_si_la_suma_origina_un_numero_par(10,20)
print(resultado)

# Leer dos numeros enteros de dos digitos y determinar a cuanto es igual la suma de todos los digitos

def suma_digitos(numero):
    if(numero < 0):
        return sum([int(x) for x in str(numero)[1:]])
    else:
        return sum([int(x) for x in str(numero)])

def determinar_la_suma_de_todos_los_digitos(numero1 = 0, numero2 = 0):
    if not numero1 or not numero2:
        return('ingrese valores validos, por favor')
    else:
        suma_digitos_1 = suma_digitos(numero1)
        suma_digitos_2 = suma_digitos(numero2)

    return suma_digitos_1, suma_digitos_2, suma_digitos_1 + suma_digitos_2

resultado = determinar_la_suma_de_todos_los_digitos(-1,28)
print(resultado)

# Leer un numero enteros de tres digitos y determina a cuanto es igual la suma de todos los digitos

def suma_digitos_1(numero):
    if(numero < 0):
        return sum([int(x) for x in str(numero)[1:]])
    else:
        return sum([int(x) for x in str(numero)])

# Leer un numero entero de tres digitos y determinar a cuanto es igual la suma de todos sus digitos 

def determinar_sum_de_todos_los_digitos_de_un_numero(numero_1 = 0):
    if not numero_1:
        return('ingrese valores validos, por favor')
    elif (-100 < numero_1 < 100):
        return('ingrese valores superiores a 3 digitos, por favor')
    else:
        suma_digitos = suma_digitos_1(numero_1)

    return suma_digitos

resultado = determinar_sum_de_todos_los_digitos_de_un_numero(99)
print(resultado)

# Leer 3 numeros enteros y determinar cual es el mayor.

def retornar_numero_mayor_de_tres(numero1 = 0, numero2 = 0, numero3 = 0):
    if not numero1 or not numero2 or not numero3:
        return('ingrese valores validos, por favor')
    else:
        numero_mayor = max(numero1, numero2, numero3)
        return(numero_mayor)

resultado = retornar_numero_mayor_de_tres(-1, -5, -10)
print(resultado)