numero_con_cadena_mas_larga=0
largo_de_la_cadena=0

for i in range(1,1000000):
    numero=i
    contador=1
    while numero>1:
        contador+=1
        if numero%2==0:
            numero=numero//2
        else:
            numero=numero*3+1
    if contador>largo_de_la_cadena:
        largo_de_la_cadena=contador
        numero_con_cadena_mas_larga=i

print(f"El numero con la cadena mas alta es: {numero_con_cadena_mas_larga}")
print(f"La cadena tuvo: {largo_de_la_cadena} terminos")