import math

def calcular_raiz_quadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "Número inválido"

def main():
    numero = float(input("Digite um número: "))
    print ('A raiz quadrada é ')
    print (calcular_raiz_quadrada(numero))
    
main()