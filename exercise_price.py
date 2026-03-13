def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    iva = precio_base * 0.21
    subtotal = precio_base + iva
    propina = subtotal * 0.10
    precio_final = subtotal + propina

    print(iva)
    print(subtotal)
    print(propina)
    print(precio_final)

#price()