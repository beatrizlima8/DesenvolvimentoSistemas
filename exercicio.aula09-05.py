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

palavra = input('Digite uma palavra: ')
vogais = ["a", "e", "i", "o", "u"]
contador = 0

for letra in palavra:
    for vogal in vogais:
        if(vogal == letra):
            contador += 1
print(f"A palavra {palavra} tem {contador} vogais")

#Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados:

numero1 = int (input('Digite o primeiro número: '))
numero2 = int (input('Digite o segundo número: '))
numero3 = int (input('Digite o terceiro número: '))
numero4 = int (input('Digite o quarto número: '))
numero5 = int (input('Digite o quinto número: '))
numero6 = int (input('Digite o sexto número: '))

ListaNumeros = [numero1, numero2, numero3, numero4, numero5, numero6]
contador = 0
for numero in ListaNumeros:
   if (numero %2 == 0):
    contador += 1
print(f"Entre os números digitados, {contador} deles são pares")

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

numeroDigitado = int (input('Digite um número para mostrar todos os números de 1 até o número digitado: '))

for numero in range(1, numeroDigitado + 1):
    print (f'{numero}')

#Peça ao usuário uma palavra e mostre ela ao contrário:

palavraDigitada = input ('Digite uma palavra para que ela seja mostrada ao contrário: ')
palavraReversa = palavraDigitada [::-1]
print (f'O contrário da palavra {palavraDigitada} é: {palavraReversa}!')

#Peça um número ao usuário e diga se ele é múltiplo de 3:

numeroDigitado = int (input('Digite um número para saber se ele é múltiplo de 3: '))

if numeroDigitado % 3 == 0: 
    print (f'O número {numeroDigitado} é múltiplo de 3.')
else:
    print (f'O número {numeroDigitado} não é múltiplo de 3.')

#Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética:

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')

listaDeNomes = [nome1,nome2,nome3]
listaDeNomes.sort(reverse=False)

print(f'Os nomes em ordem alfabética são: {listaDeNomes}')
