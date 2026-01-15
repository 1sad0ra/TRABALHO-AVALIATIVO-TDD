from CalculadoraService import adicao

#soma errada
def test_adicao_numeros_positivos():
    resultado = adicao(3, 7)
    assert resultado == 10

#soma errada
def test_adicao_positivo_negativo():
    resultado = adicao(5, -2)
    assert resultado == 3

#adição dos zeros errada
def test_adicao_zeros():
    resultado = adicao(0, 0)
    assert resultado == 0

#numero interio somado com float
def test_adicao_aceitar_floats():
    resultado = adicao(2, 3.5)
    assert resultado == 6

#soma com string
def test_adicao_strings():
    resultado = adicao("a", 5)
    assert resultado == "Erro: Entrada inválida"
    
#----------Testes para o método adicao(a, b)----------#
# Deve retornar a soma de dois números positivos;
# Deve retornar a soma de um número positivo e um negativo;
# Deve retornar zero ao somar dois zeros.
# Deve aceitar números float na soma;
# Deve retornar erro ao somar strings.