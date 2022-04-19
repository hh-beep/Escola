def printa(calc, state):
    print('')
    print('~' * 75)
    print('|')
    print(f'| o seu IMC é: {calc}, {state}')
    print('|')
    print('~' * 75)
    print('')

def verificaEstado(state):
    if (calculo <= 18.5):
        state = 'Muito magro'
        return state
    elif (calculo > 18.5 and calculo <= 24.9):
        state = 'Saudavel'
        return state
    elif (calculo > 24.9 and calculo <= 29.9):
        state = 'Sobrepeso'
        return state
    elif (calculo > 29.9 and calculo <= 34.9):
        state = 'Obesidade'
        return state
    elif (calculo > 34.9 and calculo <= 39.9):
        state = 'Obesidade severa'
        return state
    elif (calculo > 39.9):
        state = 'Obesidade morbida'
        return state

print('')
altura = float(input("Digite sua altura: (Ex: 1.85 metros)     "))
print('')
peso = float(input("Digite seu peso: (Ex: 75.5 KG)     "))
print('')

calculo = peso / (altura ** 2)

estado = ''
valorEstado = verificaEstado(estado)

printa(calculo, valorEstado)


