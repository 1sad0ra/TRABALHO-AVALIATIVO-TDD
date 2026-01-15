from CalculadoraService import multiplicar

def teste_multiplicando_com_sucesso():
    resultado = multiplicar(4, 5)
    assert resultado == 20

def teste_multiplicando_com_zero():
    resultado = multiplicar(0, 10)
    assert resultado == 0

def teste_multiplicando_numeros_negativos():
    resultado = multiplicar(-3, 6)
    assert resultado == -18

def teste_multiplicando_com_string():
    resultado = multiplicar("3", 5)
    assert resultado is None

#----------Testes para o método multiplicar(a, b)----------#
#          Deve retornar a multiplicação de dois números positivos;
#          Deve retornar zero quando um dos valores for zero;
#          Deve funcionar corretamente com números negativos.
#          Não deve aceitar strings como entrada.
