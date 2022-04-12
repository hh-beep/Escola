import random

a, b = random.randint(0, 100), random.randint(0, 100)

print(f'A vale: {a}')
print(f'B vale: {b}')

if (a < b):
    print('B é maior do que A')
elif (b < a):
    print('A é maior do que B')
else:
    print('A é igual a B')