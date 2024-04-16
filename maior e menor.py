# Função principal
def main():
    # Solicita que o usuário insira três números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))''
    num3 = float(input("Digite o terceiro número: "))

    # Encontra o maior número usando a função max() e o menor número usando a função min()
    maior_numero = max(num1, num2, num3)
    menor_numero = min(num1, num2, num3)

    # Mostra o maior e o menor número
    print("O maior número é:", maior_numero)
    print("O menor número é:", menor_numero)

# Chama a função principal
if __name__ == "__main__":
    main()
