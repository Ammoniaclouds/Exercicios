def main():
    letra = input("Digite uma letra: ").lower()
    if letra in 'aeiou':
        print("A letra digitada é uma vogal.")
    elif 'a' <= letra <= 'z':
        print("A letra digitada é uma consoante.")
    else:
        print("Por favor, digite uma letra do alfabeto.")

main()