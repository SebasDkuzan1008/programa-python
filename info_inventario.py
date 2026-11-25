INVENTARIO = [
    ["A001", "Tornillos", 50, 100],   # stock menor al mínimo
    ["A002", "Tuercas", 80, 80],      # stock igual al mínimo
    ["A003", "Arandelas", 200, 150],  # stock mayor al mínimo
    ["A004", "Clavos", 10, 60],       # stock menor al mínimo
    ["A005", "Martillos", 15, 10],    # stock mayor al mínimo
]
def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """Calcula la cantidad exacta a pedir de un artículo.

    Parámetros:
        stock_actual (int): unidades disponibles.
        stock_minimo (int): unidades mínimas requeridas.

    Retorna:
        int: stock_minimo - stock_actual si hay faltante; 0 en otro caso.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0
def mostrar_informe(inventario):
    """Recorre el inventario y muestra la cantidad a pedir de cada artículo."""
    print("===== INFORME DE REABASTECIMIENTO =====")
    for articulo in inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        cantidad = calcular_cantidad_pedir(stock_actual, stock_minimo)
        print(f"{nombre}: pedir {cantidad} unidades")
    print("===== FIN DEL INFORME =====")


mostrar_informe(INVENTARIO)