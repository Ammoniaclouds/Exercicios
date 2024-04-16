
while True:
    try:
        numero = int(input("Digite um numero de 1 a 10: "))
        if numero <=10 and numero >=1:
            for i in range (1,11):
                resultado = numero*i
                print(f"numero {numero} * {i} = {resultado}")
        else:
            print("numero invalido, tente novamente")
    except ValueError:
        print("Entrada invalida, tente novamente")
