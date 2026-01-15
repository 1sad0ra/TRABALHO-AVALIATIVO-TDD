# TRABALHO-AVALIATIVO-TDD
## DESCRIÇÃO DA ATIVIDADE
Os alunos deverão desenvolver um módulo de cálculo e validação de operações básicas, utilizando estritamente a metodologia TDD.

O trabalho será dividido em etapas:
1. Escrita dos testes unitários;
2. Execução dos testes (falha inicial – Red);
3. Implementação mínima do código (Green);
4. Refatoração do código (Refactor).

## FUNCIONALIDADES A SEREM DESENVOLVIDAS
O sistema deverá implementar uma classe chamada CalculadoraService,contendo os seguintes métodos:
- somar(a, b)
- subtrair(a, b)
- multiplicar(a, b)

## Métodos de Teste a serem Criados
Os alunos deverão criar testes unitários antes da implementação dos métodos acima.
1. Testes para o método somar(a, b)
- Deve retornar a soma de dois números positivos;
- Deve retornar a soma de um número positivo e um negativo;
- Deve retornar zero ao somar dois zeros.
2. Testes para o método subtrair(a, b)
- Deve retornar a subtração correta entre dois números;
- Deve permitir resultado negativo;
- Deve retornar zero quando os valores forem iguais.
3. Testes para o método multiplicar(a, b)
- Deve retornar a multiplicação de dois números positivos;
- Deve retornar zero quando um dos valores for zero;
- Deve funcionar corretamente com números negativos.
4. Testes para o método dividir(a, b)
- Deve retornar o quociente correto da divisão;
- Deve lançar exceção ao tentar dividir por zero;
- Deve funcionar com números decimais (se aplicável).
5. Testes para o método isPar(numero)
- Deve retornar verdadeiro para números pares;
- Deve retornar falso para números ímpares;
- Deve funcionar corretamente com zero.
6. Testes para o método validarNumeroPositivo(numero)
- Deve retornar verdadeiro para números positivos;
- Deve retornar falso para números negativos;
- Deve lançar exceção ou retornar falso para zero (definir regra).

# ARQUIVOS IMPORTANTES
[Trabalho.pdf](https://drive.google.com/file/d/19f6J14UOm8lkrRqalN3vjrDumdKwCRD-/view?usp=sharing)

[Relatório](https://docs.google.com/document/d/18BofIW2mRU6gS1CZRF3lSoRskRr3irqqAW7PLEzBYfg/edit?usp=sharing)

## Linguagens:
- Python
## Framework
- pytest

### Data de entrega: 15 de jan., 17:59
