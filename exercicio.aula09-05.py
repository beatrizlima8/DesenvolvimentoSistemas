#DATA: 09/05/2025

#Exercícios de treinamento em Python

#Peça ao usuário para digitar 5 números e mostre a soma deles ao final:

num1 = int (input('Digite o primeiro número:'))
num2 = int (input('Digite o segundo número:'))
num3 = int (input('Digite o terceiro número:'))
num4 = int (input('Digite o quarto número:'))
num5 = int (input('Digite o quinto número:'))

soma = num1 + num2 + num3 + num4 + num5

print(f'A soma dos números é ' f'{soma}!')

#Peça ao usuário para digitar 4 números e mostre qual é o maior e qual é o menor:

num1 = int (input('Digite o primeiro número:'))
num2 = int (input('Digite o segundo número:'))
num3 = int (input('Digite o terceiro número:'))
num4 = int (input('Digite o quarto número:'))

listaNumeros = [num1, num2, num3, num4]
listaNumeros.sort(reverse=False)

print (f'O maior número é {listaNumeros[-1]} e o menor número é {listaNumeros[0]}.')

#Peça ao usuário uma palavra e mostre quantas vogais ela tem:

#Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados:

#Solicite as notas de 4 provas e mostre a média:

nota1 = int (input('Digite a primeira nota:'))
nota2 = int (input('Digite a segunda nota:'))
nota3 = int (input('Digite a terceira nota:'))
nota4 = int (input('Digite a quarta nota:'))

soma = nota1 + nota2 + nota3 + nota4
media = soma/4

print(f'A média das notas é {media}!')

#Peça ao usuário um número e mostre a tabuada desse número de 1 a 10:

#Peça um número N ao usuário e mostre todos os números de 1 até N:

#Peça ao usuário uma palavra e mostre ela ao contrário:

#Peça um número ao usuário e diga se ele é múltiplo de 3:

#Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética:
