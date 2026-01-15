def multiplicar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os valores devem ser números inteiros ou decimais.")

    return a * b


# 7.3 Testes para o método multiplicar(a, b)
#Deve retornar a multiplicação de dois números positivos;
#Deve retornar zero quando um dos valores for zero;
#Deve funcionar corretamente com números negativos.