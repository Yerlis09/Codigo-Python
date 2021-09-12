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

resultado = retornar_ultimo_dos_digitos('')
print( resultado)

# Construir una funcion que reciba como parametro un entero y retorne la cantidad de digitos

def retornar_cantidad_de_digitos(numero):
    if (numero == None):
        return 'Ingrese un valor valido'
    elif (numero == ''):
        return 'Ingrese un valor, por favor'
    elif (numero < 0):
        longitud = int(len(str(numero))-1)
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
    elif (numero == '') and (numero < 0):
        return 'Ingrese un valor o un numero entero positivo'
    elif (numero == 1):
        return 0
    else:
        cont = 0
        for i in range(numero):
            if (i % 2 == 0):
                cont +=1
        return cont

resultado = retornar_cantidad_de_digitos_pares(2)
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
    elif (numero == '') and (numero < 0):
        return 'Ingrese un numero o un numero entero positivo'
    elif (numero == 1) and (numero == 0):
        return 0
    elif (numero == 2):
        return 1
    count = 0
    for i in range(2, (numero + 1)):
        if (retornar_si_es_primo(i) == True):
            count += 1
    return count

resultado = retornar_cantidad_digitos_primos(5)
print(resultado)