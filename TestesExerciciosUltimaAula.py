
#Teste 01
import unittest

class TestFuncoes(unittest.TestCase):
    def test_primos_no_intervalo(self):
        self.assertEqual(primos_no_intervalo(1, 10), [2, 3, 5, 7])
        self.assertEqual(primos_no_intervalo(10, 15), [11, 13])
        self.assertEqual(primos_no_intervalo(20, 22), [])

  if __name__ == '__main__':
    unittest.main()

#Teste 02

    def test_ordenar_sem_repeticao(self):
        self.assertEqual(ordenar_sem_repeticao([3, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(ordenar_sem_repeticao([]), [])
        self.assertEqual(ordenar_sem_repeticao([5, 5, 5]), [5])

    if __name__ == '__main__':
    unittest.main()

#Teste 03

    def test_soma_digitos(self):
        self.assertEqual(soma_digitos(123), 6)
        self.assertEqual(soma_digitos(0), 0)
        self.assertEqual(soma_digitos(-456), 15)
      
if __name__ == '__main__':
    unittest.main()

#Teste 04
  
    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("arara"))
        self.assertTrue(eh_palindromo("A man a plan a canal Panama"))
        self.assertFalse(eh_palindromo("Python"))
      
if __name__ == '__main__':
    unittest.main()

#Teste 05

    def test_frequencia_palavras(self):
        self.assertEqual(frequencia_palavras("Oi oi tudo bem"), {'oi': 2, 'tudo': 1, 'bem': 1})
        self.assertEqual(frequencia_palavras(""), {})

  if __name__ == '__main__':
    unittest.main()

#Teste 06

    def test_media_lista(self):
        self.assertEqual(media_lista([1, 2, 3, 4]), 2.5)
        self.assertEqual(media_lista([]), None)
        self.assertEqual(media_lista([10]), 10)

if __name__ == '__main__':
    unittest.main()
