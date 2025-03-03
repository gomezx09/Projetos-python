# 📝 Calculadora de Média Escolar
# Este programa recebe quatro notas do aluno, calcula a média e exibe a situação final.

# Solicita as quatro notas do aluno
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

# Calcula a média das notas
media = (n1 + n2 + n3 + n4) / 4

# Exibe as notas e a média formatada com duas casas decimais
print(f'\n📊 Notas: {n1}, {n2}, {n3}, {n4}')
print(f'🎯 Média final: {media:.2f}\n')

# Verifica a situação do aluno
if media < 5:
    print('❌ O aluno está REPROVADO.')
elif media < 7:
    print('⚠️ O aluno está em RECUPERAÇÃO.')
else:
    print('✅ O aluno está APROVADO.')

# Mensagem final
print('\n🎓 Estude sempre para melhorar seu desempenho! 🚀')
