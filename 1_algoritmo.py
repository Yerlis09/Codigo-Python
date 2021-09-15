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
    if (numero1 == None) and (numero2 == None):
        return('ingrese valores validos, por favor')
    elif (numero2 == '') and (numero1 == ''):
        return 'ingrese un valor, por favor'
    elif (numero1 == '') and (numero2 == ''):
        return 'No se permite caracteres'
    else:
        list = [numero1, numero2]
        numero_mayor = max(list)
        return numero_mayor

resultado = determinar_cual_es_el_numero_mayor(33,8)
print(resultado)