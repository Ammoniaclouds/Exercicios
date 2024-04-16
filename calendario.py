def main():
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    numero = int(input("Digite um número entre 1 e 12: "))
    
    if 1 <= numero <= 12:
        print(meses[numero - 1])
    else:
        print("Não existe mês com este número")

main()