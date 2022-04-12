nota1bimestre, nota2bimestre, nota3bimestre, nota4bimestre = int(input('Digite a nota do 1º bimestre (ate 100 pontos)   ')), int(input('Digite a nota do 2º bimestre (ate 100 pontos)   ')), int(input('Digite a nota do 3º bimestre (ate 100 pontos)   ')), int(input('Digite a nota do 4º bimestre (ate 100 pontos)    '))
def validaValor(value):
    if(value >= 0 and value <= 100):
        return value
    else:
        value = int(input('Digite novamente o valor (ate 100 pontos)    '))
        validaValor(value)
v1b, v2b, v3b, v4b = validaValor(nota1bimestre), validaValor(nota2bimestre), validaValor(nota3bimestre), validaValor(nota4bimestre)
valores = [ v1b, v2b, v3b, v4b ]
valorTotal = 0
for element in valores:
    valorTotal += element
calculo = valorTotal / len(valores)
print(calculo)
