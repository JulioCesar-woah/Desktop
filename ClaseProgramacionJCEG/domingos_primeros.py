dias_meses=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
domingos_primeros=0
dia_actual=0

for year in range (1900,2001):
    if (year%400==0) or (year%4==0 and year%100!=0):
        dias_meses[1]=29
    else:
        dias_meses[1]=28
    for meses in range (1,13):
            if year>=1901 and dia_actual==6:
                domingos_primeros+=1
            dia_actual=(dia_actual+dias_meses[meses-1])%7

print(f"La cantidad de domingos que cayeron en primero de mes 1901-2000 es: {domingos_primeros}")