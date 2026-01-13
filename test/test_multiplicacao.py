from CalculadoraService import multiplicar

def teste_multiplicando_com_sucesso():
    resultado = multiplicar(4, 5)
    assert resultado == 20

#----------Testes para o método multiplicar(a, b)----------#
#          Deve retornar a multiplicação de dois números positivos;
#          Deve retornar zero quando um dos valores for zero;
#          Deve funcionar corretamente com números negativos.