from operacoes.multiplicacao import multiplicar
from operacoes.subtracao import subtrair
from operacoes.adicao import adicao

class Calculadora:

    def multiplicacao(self, a, b):
        return multiplicar(a, b)

    def subtracao(self, a, b):
        return subtrair(a, b)
    
    def adicao(self, a, b):
        return adicao(a, b)
    
    