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


