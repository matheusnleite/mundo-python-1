x = input('Digite algo: ')

print('O tipo primitivo é: ', type(x))
print('É alfa numérico? ', x.isalnum())
print('É uma letra', x.isalpha())
print('É um caractere ascii? ', x.isascii())
# todos os caracteres da string forem dígitos (0 a 9)
print('É um digito? ', x.isdigit())
print('Todos os caracteres são minusculos? ', x.islower())
print('É um decimal?', x.isdecimal())
print('É um nome valido para uma variável? ', x.isidentifier())
# todos os caracteres da string forem numéricos, incluindo não apenas dígitos, mas também caracteres numéricos em outros sistemas de escrita, como números romanos ou chineses.
print('É um número?', x.isnumeric())
#Ex: \n não é imprimivel
print('Possui apenas caracteres imprimíveis? ', x.isprintable())
print('Só contém espaços em branco? ', x.isspace())
# titulo: se a primeira letra de cada palavra na string é maiúscula e as demais são minúsculas
print('Está em formato de título? ',x.istitle())
print('É tudo maiúsculo? ', x.isupper())
