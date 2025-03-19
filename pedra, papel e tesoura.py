import random
from time import sleep

def main():
    print('''\033[4;35mVamos jogar Jokenpô!!!
\033[35m[1] PEDRA
[2] PAPEL
[3] TESOURA\033[m''')

    # Obtém a escolha do usuário
    option = int(input('\033[34mQual sua opção? \033[m'))

    print('\033[33mJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!\033[m')
    sleep(0.5)

    # Escolha do computador
    choices = ['PEDRA', 'PAPEL', 'TESOURA']
    pc = random.choice(choices)
    print(f'\033[36mPC escolheu {pc}!!!\033[m')

    # Determina o vencedor
    if option == 1:  # Usuário escolheu PEDRA
        if pc == 'PEDRA':
            print('\033[31mEMPATE!!! Tente novamente\033[m')
        elif pc == 'PAPEL':
            print('\033[32mPapel cobre a pedra, PC GANHOU!!!\033[m')
        else:  # pc == 'TESOURA'
            print('\033[32mPedra quebra tesoura, VOCÊ GANHOU!!!\033[m')

    elif option == 2:  # Usuário escolheu PAPEL
        if pc == 'PEDRA':
            print('\033[32mPapel cobre a pedra, VOCÊ GANHOU!!!\033[m')
        elif pc == 'PAPEL':
            print('\033[31mEMPATE!!! Tente novamente\033[m')
        else:  # pc == 'TESOURA'
            print('\033[32mTesoura corta o papel, PC GANHOU!!!\033[m')

    elif option == 3:  # Usuário escolheu TESOURA
        if pc == 'PEDRA':
            print('\033[32mPedra quebra a tesoura, PC GANHOU!!!\033[m')
        elif pc == 'PAPEL':
            print('\033[32mTesoura corta o papel, VOCÊ GANHOU!!!\033[m')
        else:  # pc == 'TESOURA'
            print('\033[31mEMPATE!!! Tente novamente\033[m')

    else:  # Caso o usuário insira uma opção inválida
        print('\033[31mSua opção é inválida.\033[m')

if __name__ == "__main__":
    main()