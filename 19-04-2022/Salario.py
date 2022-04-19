def printa(impostos, inss, sindicato, money):
    print('')
    print('~' * 75)
    print('|')
    print(f'| O valor de seus impostos é de: R$ {impostos},00')
    print('|')
    print(f'| O valor do INSS é de: R$ {inss},00')
    print('|')
    print(f'| O valor do Sindicato é de: R$ {sindicato},00')
    print('|')
    print('|')
    print(f'| O seu salario liquido é de: R$ {money},00')
    print('|')
    print('|')
    print('~' * 75)
    print('')


horasTotais = int(input("Digite o total de horas que você trabalha por mês:   "))
valorHoras = float(input("Digite o valor em você recebe por hora:   "))

salarioBruto = (horasTotais * valorHoras)

impostos = (salarioBruto / 100) * 11
inss = (salarioBruto / 100) * 8
sindicato = (salarioBruto / 100) * 5

salarioLiquido = salarioBruto - (impostos + inss + sindicato)

printa(impostos, inss, sindicato, salarioLiquido)