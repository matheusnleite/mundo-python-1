salario_atual=float(input('Salario atual: '))

novo_salario = salario_atual + ((15/100) * salario_atual)

print('Seu novo salario é: R${:.2f}'.format(novo_salario))