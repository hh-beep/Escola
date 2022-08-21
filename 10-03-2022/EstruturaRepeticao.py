print("")
num = int( input("Diga um numero entre 0 a 10:   "))
print("")
print("")



while (  num < 0 or num > 10  ):
    if (  num < 0  ):
        print("")
        print("\033[1;33;40m Numero Negativo \033[m")
        print("")
    if (  num > 10  ):
        print("")
        print("\033[1;33;40m Numero maior que 10 \033[m")
        print("")

    print("")
    num = int(input("Digite novamente:   "))
    print("")

print(f"O numero digitado é {num}")
print("")



