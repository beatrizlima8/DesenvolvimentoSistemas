#Exercicio 1

def primos_no_intervalo(a, b):
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [x for x in range(a, b + 1) if eh_primo(x)]
  
#Exercicio 2

def ordenar_sem_repeticao(lista):
    return sorted(set(lista))

#Exercicio 3

def soma_digitos(n):
    return sum(int(d) for d in str(abs(n)))

#Exercicio 4

def eh_palindromo(texto):
    t = ''.join(texto.lower().split())
    return t == t[::-1]

#Exercicio 5

def frequencia_palavras(texto):
    palavras = texto.lower().split()
    freq = {}
    for p in palavras:
        freq[p] = freq.get(p, 0) + 1
    return freq

#Exercicio 6

def media_lista(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)
    
