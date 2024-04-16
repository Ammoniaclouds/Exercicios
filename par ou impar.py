def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero > 0:
        if numero % 2 == 0:
            print("O número digitado é par.")
        else:
            print("O número digitado é ímpar.")
    else:
        print("Por favor, digite um número inteiro positivo.")

main()