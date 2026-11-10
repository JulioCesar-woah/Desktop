numero=600851475143
divisor=2
while divisor * divisor <= numero:
        if numero % divisor == 0:
            numero = numero // divisor
        else:
            divisor += 1
print(f"{numero}")