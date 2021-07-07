import math, random

def generar_llegada_A(min, max):
        rnd = random.randint((min), (max))
        return rnd

def generar_llegada_B(min, max):
        rnd = random.randint((min), (max))
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
    return permanencia


def generar_permanenciasalon1(reloj, min, max):
    #permanencia
    rnd = random.randint(0, 60)
    rnd2 = min + rnd
    permanencia = rnd2 + reloj
    return permanencia