# Teste para a função de subtração 

from CalculadoraService import subtrair 

def teste_subtraindo():
    resultado = subtrair(10, 5) 
    assert resultado == 5

def teste_subtracao_com_resultado_negativo():
    resultado = subtrair(4, 10)
    assert resultado == -6


def teste_subtracao_com_valores_iguais():
    resultado = subtrair(5, 5)
    assert resultado == 0
