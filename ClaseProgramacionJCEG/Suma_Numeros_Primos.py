suma_primos=0

for numero in range(2, 2000001):
    primo=1
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i==0:
            primo=0
            break
            
    if primo==1:
        suma_primos+=numero

print(f"La suma de los numeros primos fue: {suma_primos}")