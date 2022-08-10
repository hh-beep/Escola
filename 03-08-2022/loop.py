import random


randomNum = random.randint(1, 6)

resp = int(input("Digite um numero entre 1 a 6:   "))



while (  resp != randomNum  ):
    resp = int(input("Errou, digite novamente:   "))


print(f"Acertou, o nuemro era: {randomNum}")



