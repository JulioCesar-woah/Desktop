gastos = []

def agregar_gasto():
    descripcion = input("Descripción del gasto: ")
    
    try:
        monto = float(input("Monto ($): "))
        if monto <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return

    print("Categoría (1. Comida / 2. Transporte / 3. Ocio / 4. Otros)")
    try:
        op_cat = int(input("Elige una categoría: "))
        categorias_map = {1: "Comida", 2: "Transporte", 3: "Ocio", 4: "Otros"}
        if op_cat not in categorias_map:
            print("Error: Categoría no válida.")
            return
        categoria = categorias_map[op_cat]
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return

    nuevo_gasto = {
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria
    }
    gastos.append(nuevo_gasto)
    print("-> Gasto registrado con éxito.")


def mostrar_gastos():
    if not gastos:
        print("Aún no hay gastos registrados.")
        return

    print("\n--- TODOS LOS GASTOS ---")
    for i, g in enumerate(gastos, start=1):
        print(f"{i}. [{g['categoria']}] {g['descripcion']} - ${g['monto']:.2f}")


def filtrar_por_categoria():
    if not gastos:
        print("Aún no hay gastos registrados.")
        return

    print("\nCategorías: 1. Comida | 2. Transporte | 3. Ocio | 4. Otros")
    try:
        op_filtro = int(input("Elige una opción: "))
        categorias_map = {1: "Comida", 2: "Transporte", 3: "Ocio", 4: "Otros"}
        if op_filtro not in categorias_map:
            print("Error: Opción no válida.")
            return
        cat_buscada = categorias_map[op_filtro]
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return

    print(f"\n--- Gastos en {cat_buscada} ---")
    encontrados = False
    for i, g in enumerate(gastos, start=1):
        if g["categoria"] == cat_buscada:
            print(f"{i}. {g['descripcion']} - ${g['monto']:.2f}")
            encontrados = True

    if not encontrados:
        print("No hay gastos registrados en esta categoría.")


def calcular_resumen():
    if not gastos:
        print("Aún no hay gastos registrados.")
        return

    total_general = sum(g["monto"] for g in gastos)
    print("\n--- RESUMEN DE GASTOS ---")
    print(f"Total general: ${total_general:.2f}")

    for cat in ["Comida", "Transporte", "Ocio", "Otros"]:
        subtotal = sum(g["monto"] for g in gastos if g["categoria"] == cat)
        print(f"* {cat}: ${subtotal:.2f}")

while True:
    print("=== GESTOR DE GASTOS ===")
    print("\n1. Registrar gasto")
    print("2. Ver todos los gastos")
    print("3. Filtrar por categoría")
    print("4. Ver resumen total")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Ingresa un número entero válido.")
        continue

    if opcion == 1:
        agregar_gasto()
    elif opcion == 2:
        mostrar_gastos()
    elif opcion == 3:
        filtrar_por_categoria()
    elif opcion == 4:
        calcular_resumen()
    elif opcion == 5:
        print("ADIOS")
        break
    else:
        print("Opción no válida. Elige un número del 1 al 5.")