# Problema Seleccinado:
# 4- Diseñe una solución que a partir de una lista de  calificaciones retorne una lista con su valor equivalente en letras
def ConvertirCalificacionALetras():
    Calificaciones = []
    CalificacionesLetra = []

    print("Cuanta Calificaciones va a Ingresar")
    Cantidad = int(input())

    for i in range(Cantidad):
        print(f"Ingrese la Calificacion # {i + 1}")
        ValorRecibido = int(input())
        Calificaciones.append(ValorRecibido)

        if (ValorRecibido >= 90): CalificacionesLetra.append("A")
        elif (ValorRecibido >= 80): CalificacionesLetra.append("B")
        elif (ValorRecibido >= 70): CalificacionesLetra.append("C")
        else: CalificacionesLetra.append("D")

    print(
        f"Calificaciones Ingresadas: {Calificaciones} y su equivalente en Letras: {CalificacionesLetra}"
    )


ConvertirCalificacionALetras()
