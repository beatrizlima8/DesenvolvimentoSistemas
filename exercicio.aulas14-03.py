#DATA: 14/03/2025

#Exercicio1:

idade = int (input('Digite uma idade:'))

if idade < 12 :
     print ('Essa pessoa é uma criança.')
if idade >= 12 and idade <= 17 :
     print ('Essa pessoa é um adolescente.')
elif idade >= 18 :
     print ('Essa pessoa é um adulto.')

#Exerciocio2:

numero1 = int (input('Digite o primeiro número:'))
numero2 = int (input('Digite o segundo número:'))

if numero1 > numero2 :
    print (f'{numero1} é o maior número.' )
if numero2 > numero1 :
    print (f'{numero2} é o maior número.')
if numero1 == numero2 :
    print ('Os dois números são iguais.')
  
#Exercicio3:

letra = input('Digite uma letra:')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
     print ('Essa letra é uma vogal.')
else:
     print('Essa letra é uma consoante.')

#Exercicio4:

senha = input('Digite uma senha:')
senha2 = input('Confirme a senha:')

if senha == senha2 :
  print('Acesso permitido.')
else:
  print('As senhas não coincidem.')

#Exercicio5:

nota1 = int (input('Qual a primeira nota?'))
nota2 = int (input('Qual a segunda nota?'))
nota3 = int (input('Qual a terceira nota?'))

soma = nota1 + nota2 + nota3
media = soma/3

if media >= 7 :
     print (f'{media} foi sua média, você foi aprovado!')
else:
     print (f'{media} foi sua média, você foi reprovado!')
