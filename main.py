import time

print("1. Adição")
print("2. Subtração")
print("3. Divisão")
print("4. Multiplicação")

while True:
    try:
        mathtype = int(input("Insira o número da sua operação: "))
        break
    except ValueError:
        print("Digite um valor válido!")

while True:
    try:
        fnumber = int(input("Insira o primeiro número da sua operação: "))
        break
    except ValueError:
        print("Digite um valor válido!")

while True:
    try:
        snumber = int(input("Agora, insira o segundo número da sua operação: "))
        break
    except ValueError:
        print("Digite um valor válido!")


if mathtype == 1:
    addcalc = fnumber + snumber
    print(addcalc)
    time.sleep(2)
elif mathtype == 2:
    subcalc = fnumber - snumber
    print(subcalc)
    time.sleep(2)
elif mathtype == 3:
    divcalc = fnumber/snumber
    print(divcalc)
    time.sleep(2)
elif mathtype == 4:
    multcalc = fnumber * snumber
    print(multcalc)
    time.sleep(2)
