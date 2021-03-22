# Problema #6 Selecionado: Hiatos y Diptongos
# Comprobar si una lista de palabras contiene Hiatos, Diptongos o AMBOS
# Si quiere ver mas detalle del problema seleccionado desplazece hacia abajo

Palabras = []
Contienen = []
VocalesFuertes = "a e o"
VocalesCerradas = "i u"

print("Cuantas Palabras va a Ingresar")
Cantidad = int(input())

for i in range(Cantidad):
    print(f"Ingrese la Palabra # {i + 1}")
    ValorRecibido = input().lower()
    Palabras.append(ValorRecibido)

    Examinar = list(Palabras[i])
    Hiato = 0
    Diptongo = 0

    for i in range(len(Examinar)):
        if (i < (len(Examinar) - 1)):
            if (Examinar[i] in VocalesFuertes):
                if (Examinar[i + 1] in VocalesFuertes):
                    Hiato += 1

                elif (Examinar[i + 1] in VocalesCerradas):
                    Diptongo += 1

            elif (Examinar[i] in VocalesCerradas):
                if (Examinar[i + 1] == Examinar[i]):
                    Hiato += 1

                elif (Examinar[i + 1] in VocalesCerradas
                      or Examinar[i + 1] in VocalesFuertes):
                    Diptongo += 1
                    
    if (Hiato > 0 and Diptongo > 0): Contienen.append("AMBOS")
    elif (Hiato > 0): Contienen.append("HIATO")
    elif (Diptongo > 0): Contienen.append("DIPTONGO")
    else: Contienen.append("NINGUNO")

print(Palabras,Contienen)

""""
Entrada:
 La primera línea contiene un número entero N (1 ≤ N ≤ 10).
 Cada una de las siguientes N líneas contiene una palabra, consistente en 1 a 20 letras del alfabeto inglés.
 Todas las letras son en mayúsculas.

Salida:
 Imprime N líneas. La i-ésima línea corresponde a la i-ésima palabra de entrada. La línea debe contener
 exactamente una de las siguientes respuestas:
 HIATO: si la palabra tiene uno o más hiatos (pero ningún diptongo)
 DIPTONGO: si la palabra tiene uno o más diptongos (pero ningún hiato)
 AMBOS: si la palabra tiene ambos efectos, hiato y diptongo
 NINGUNO: si la palabra no tiene ni hiato ni diptongo
"""
