#Deve retornar a soma de dois números positivos;
#Deve retornar a soma de um número positivo e um negativo;
#Deve retornar zero ao somar dois zeros.

#GREEN

def adicao(a, b):

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Erro: Entrada inválida"
    
    
    return a + b
    