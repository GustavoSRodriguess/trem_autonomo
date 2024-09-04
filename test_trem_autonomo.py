import unittest
from trem_autonomo import TremAutonomo

class TestTremAutonomo(unittest.TestCase):
    
    def setUp(self):
        self.trem = TremAutonomo()

    def test_comandos_validos(self):
        comandos = ['DIREITA', 'DIREITA']
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Posição Final: 2")

        self.trem = TremAutonomo()
        comandos = ['ESQUERDA']
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Posição Final: -1")

        self.trem = TremAutonomo()
        comandos = ['ESQUERDA', 'DIREITA', 'DIREITA', 'DIREITA', 'DIREITA', 'ESQUERDA']
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Posição Final: 2")

    def test_movimentos_consecutivos(self):
        comandos = ['DIREITA'] * 21
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Erro: Mais de 20 movimentos consecutivos na mesma direção.")

        comandos = ['ESQUERDA'] * 21
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Erro: Mais de 20 movimentos consecutivos na mesma direção.")

    def test_distancia_maxima(self):
        comandos = ['DIREITA'] * 21 
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Erro: Mais de 20 movimentos consecutivos na mesma direção.")

    def test_comando_invalido(self):
        comandos = ['DIREITA', 'ESQUERDA', 'PARAR']
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Erro: Comando inválido. Use 'ESQUERDA' ou 'DIREITA'.")

    def test_comandos_ambos_validos_e_invalidos(self):
        comandos = ['DIREITA', 'ESQUERDA', 'DIREITA', 'INDEFINIDO']
        resultado = self.trem.processar_comandos(comandos)
        self.assertEqual(resultado, "Erro: Comando inválido. Use 'ESQUERDA' ou 'DIREITA'.")

if __name__ == '__main__':
    unittest.main()
