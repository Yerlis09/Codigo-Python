#Construir una función que reciba como parametro un entero y retorne su ultimo digito
def retornar_ultimo_digito(numero):
    ultimo_digito = numero %  10
    return ultimo_digito

resultado = retornar_ultimo_digito(18)
print('El ultimo digito es: %i' %resultado)

#Construir un funcion que reciba como parametro un entero y retorne sus dos ultimos digitos

# def ultimosDosDigitos(num):
#     if(num>=100):
#         dosUltimos = (num % 100)
#         print(dosUltimos)
#     else:
#         ultimo = (num % 10)
#         print(ultimo)

# ultimosDosDigitos(int(input('Ingrese un numero entero : ')))

# def cantidadDigito(num):
#     longitud = len(str(num))
#     print(int(longitud))
    
# cantidadDigito(input('Ingrese un numero entero : '))


# def pares(num):
#     par = 0
#     if(num == 1):
#         return 0
#     else:
#         for i in range(1, num+1):
#             if(i % 2 == 0):
#                 par+=1
#         return par

# resultado = pares(int(input('Ingrese un numero entero : ')))
# print('La cantidad de numeros pares es: %i'% resultado)
 
# def esPrimo(numero):
#     primo = 0
#     if numero <= 1:
#         return 0
#     elif numero == 2:
#         return 1
#     else:
#         for i in range(2, numero):
#             if i % 2 == 1:
#                 primo+=1
#         return primo

# resultado = esPrimo(int(input('Ingrese un numero entero : ')))
# print('La cantidad de numeros pares es: %i'% resultado)