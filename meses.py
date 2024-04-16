def main():
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = int(input("Digite o número do mês (1 a 12): "))
    if 1 <= mes <= 12:
        print(f"O mês {mes} tem {meses[mes - 1]} dias.")
    else:
        print("Por favor, digite um número de mês válido.")

main()