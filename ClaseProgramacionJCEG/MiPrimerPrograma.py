numeros=[12, 5, 8, 21, 14]
pares=0
for num in numeros:
    if num%2==0:
        pares+=1

print(f"Total de numeros pares: {pares}")