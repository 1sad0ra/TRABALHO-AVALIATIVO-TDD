from operacoes.multiplicacao import multiplicar
from operacoes.subtracao import subtrair

class Calculadora:

    def multiplicacao(self, a, b):
        return multiplicar(a, b)

    def subtracao(self, a, b):
        return subtrair(a, b)