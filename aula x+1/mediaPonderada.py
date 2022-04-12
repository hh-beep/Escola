nota1bimestre, nota2bimestre, nota3bimestre, nota4bimestre = int(input('Digite a nota do 1º bimestre (ate 100 pontos)   ')), int(input('Digite a nota do 2º bimestre (ate 100 pontos)   ')), int(input('Digite a nota do 3º bimestre (ate 100 pontos)   ')), int(input('Digite a nota do 4º bimestre (ate 100 pontos)   '))
print('peso do 1b é 1, peso do 2b é 2 etc...')
p1, p2, p3, p4 = 1, 2, 3, 4
calc = ((nota1bimestre * p1) + (nota2bimestre * p2) + (nota3bimestre * p3) + (nota4bimestre * p4)) / (p1 + p2 + p3 + p4) 
print(calc)