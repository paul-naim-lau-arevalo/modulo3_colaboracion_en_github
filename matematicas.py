"""Modulo de operaciones matematicas basicas y avanzadas."""

def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser numeros")
    return a + b

def restar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser numeros")
    return a - b

def multiplicar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser numeros")
    return a * b

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser numeros")
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def potencia(base, exponente):
    if not isinstance(base, (int, float)) or not isinstance(exponente, (int, float)):
        raise ValueError("Los argumentos deben ser numeros")
    return base ** exponente

def es_par(numero):
    if not isinstance(numero, (int, float)):
        raise ValueError("El argumento debe ser un numero")
    return numero % 2 == 0
