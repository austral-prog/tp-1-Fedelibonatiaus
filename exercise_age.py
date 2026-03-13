
def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
    edad_anos = 25
    mes = 1 / 12
    dia = 1 / 365
    horas = dia / 24
    mins = horas / 60
    print(edad_anos // mes)
    print(edad_anos // dia)
    print(edad_anos // horas)
    print(edad_anos // mins)

#age()