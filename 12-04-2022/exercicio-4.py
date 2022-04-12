def formataTexto(texto):
    print('')
    print('-' * 75)
    print('|')
    print(f'| Media anual: {texto}')
    print('|')
    print('-' * 75)
    print('')

def validaNota(nota):
    if (nota < 0 or nota > 100):
        nota = int(input('\033[0;31;40mDefina a nota novamente:   \033[m'))
    else:
        return nota

nota1 = int(input('Digite a nota do 1º Bimestre:   '))
valorn1 = validaNota(nota1)
nota2 = int(input('Digite a nota do 2º Bimestre:   '))
valorn2 = validaNota(nota2)
nota3 = int(input('Digite a nota do 3º Bimestre:   '))
valorn3 = validaNota(nota3)
nota4 = int(input('Digite a nota do 4º Bimestre:   '))
valorn4 = validaNota(nota4)

media = (valorn1 + valorn2 + valorn3 + valorn4) / 4

formataTexto(media)