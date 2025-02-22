# Programa para converter um número inteiro para diferentes bases numéricas

def main():
    print("=== Conversor de Bases Numéricas ===")
    try:
        num = int(input("Digite um número inteiro: "))
        print("\nEscolha a base de conversão:")
        print("1 - Binário")
        print("2 - Octal")
        print("3 - Hexadecimal")

        opcao = int(input("\nSua opção: "))

        if opcao == 1:
            print(f"O número {num} em binário é {bin(num)[2:]}")
        elif opcao == 2:
            print(f"O número {num} em octal é {oct(num)[2:]}")
        elif opcao == 3:
            print(f"O número {num} em hexadecimal é {hex(num)[2:].upper()}")
        else:
            print("Opção inválida! Escolha entre 1, 2 ou 3.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

if __name__ == "__main__":
    main()