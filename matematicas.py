"""Modulo de operaciones matematicas basicas y avanzadas."""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def potencia(base, exponente):
    return base ** exponente

def es_par(numero):
    return numero % 2 == 0
