#Deve retornar a soma de dois números positivos;
#Deve retornar a soma de um número positivo e um negativo;
#Deve retornar zero ao somar dois zeros.

#GREEN

def adicao(a, b):
    try:
        a = int(a) if str(a).isdigit() else float(a)
        b = int(b) if str(b).isdigit() else float(b)
    except (ValueError, TypeError):
        return "Erro: Entrada inválida"

    return a + b
