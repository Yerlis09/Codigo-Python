# Construir una función que reciba como parametro un entero y retorne su ultimo digito
def retornar_ultimo_digito(numero):
    ultimo_digito = numero %  10
    return ultimo_digito

resultado = retornar_ultimo_digito(18)
print('El ultimo digito es: %i' %resultado)

# Construir un funcion que reciba como parametro un entero y retorne sus dos ultimos digitos

def retornar_ultimo_dos_digitos(numero):
    dosUltimosDigitos = str(numero)[-2:]
    return dosUltimosDigitos

resultado = retornar_ultimo_dos_digitos(100)
print('El resultado es: ' + resultado)