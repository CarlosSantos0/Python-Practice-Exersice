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




