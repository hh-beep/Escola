import random 

a, b = random.randint(-100, 100), random.randint(-100, 100)

print(f'A vale: {a}')
print(f'B vale: {b}')

if (a < 0 and b < 0):
    print('ambos são negativos')
elif(a > 0 and b > 0):
    print('anmbos são positivos')
elif ((a > 0 and b < 0) or (b > 0 and a < 0)):
    print('Um é positivo e outro é negativo')
else: 
    print('ambos são zero')