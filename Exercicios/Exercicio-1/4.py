num1 = float(input(' Digite a nota do 1º bimestre:   '))
num2 = float(input(' Digite a nota do 2º bimestre:   '))
num3 = float(input(' Digite a nota do 3º bimestre:   '))
num4 = float(input(' Digite a nota do 4º bimestre:   '))

soma = (num1 + num2 + num3 + num4) / 4

print(f' A soma deu uma nota Azul de: {soma}') if soma > 60 else print(f' A soma deu uma nota Vermelha de: {soma}')