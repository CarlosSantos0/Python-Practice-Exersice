# Problema Seleccionado:
# 2 - Diseñe una clase que represente una esfera y permita determinar el área de la superficie, el volumen y el diámetro a partir del radio.

class Esfera():

  def __init__(self, Radio):
    pi = 3.1415
    self.AreaSuperficie = round(4 * pi * (Radio**2), 2)
    self.Volumen = round(4/3 * (pi * (Radio**3)), 2)
    self.Diametro = 2 * Radio


print("Ingrese el Radio que tendra el Objeto Esfera")
esfera = Esfera(float(input()))
print(f"Area de la superficie: {esfera.AreaSuperficie}\n",
 f"Volumen: {esfera.Volumen}\n",
 f"Diametro: {esfera.Diametro}")