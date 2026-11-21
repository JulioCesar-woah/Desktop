# HOLA MUNDO =D
ESTO ES UNA TAREA DE CALCULAR LOS DOMINGOS QUE CAYERON EL PRIMER DIA DEL 1901-2000

##
    from datetime import date

    total=sum(
        1
        for año in range (1901, 2001)
        for mes in range (1,13)
        if date(año, mes, 1).weekday()==6
    )
    print(total)