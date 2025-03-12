from datetime import date

# 📅 Obtendo o ano atual
atual = date.today().year

# 📝 Solicitar o ano de nascimento
nascimento = int(input('Digite o seu Ano de Nascimento: '))

# 🔢 Calcular a idade do atleta
idade = atual - nascimento

# 🎯 Exibir a idade do atleta
print(f'\nO atleta tem {idade} anos. 🎉')

# 🏅 Classificar o atleta de acordo com a idade
if idade <= 9:
    print('🧸 Este aluno é **MIRIM**. 🧸')
elif idade <= 14:
    print('🧒 Este aluno é **INFANTIL**. 🧒')
elif idade <= 19:
    print('🧑‍🦱 Este aluno é **JUNIOR**. 🏅')
elif idade <= 25:
    print('🧑‍🦰 Este aluno é **SENIOR**. 🏆')
else:
    print('👨‍🦳 Este aluno é **MASTER**. 🏆')

# 🎉 Mensagem final
print('\n🎓 Continue treinando e melhorando! 💪🚀')
