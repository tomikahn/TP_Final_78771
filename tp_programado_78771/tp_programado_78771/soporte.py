import math, random

def generar_llegada():
    rnd = random.randint((30 - 10), (30 + 10))
    return rnd


def salonSiguiente():
    rnd = random.random()
    if rnd < 0.8:
        return "2"
    else:
        return "3"

def generar_permanencia(valor, reloj):
    #permanencia
    rnd = random.randint((valor-60), (valor+60))
    permanencia = rnd + reloj
    return permanencia