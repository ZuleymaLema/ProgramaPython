##Aplicacion del teorema de variacion de energia cinetica
print("Problema:")
print("Aplique el teorema sobre la variacion de la energia cinetica y \n calcule el trabajo realizado cuando en 8 seg un automovil de 120 kg varia \nsu velocidad de 20 m/seg a 30 m/seg")
vi = float(input("Ingrese la velocidad inicial"))
vf = float(input("Ingrese la velocidad final"))
m = float(input("Ingrese la masa"))

w = (1/2)*m*((vf**2)- (vi**2))
print("Respuesta:",w," julios")