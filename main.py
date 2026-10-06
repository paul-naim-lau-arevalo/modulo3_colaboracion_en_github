"""
Punto de entrada principal del proyecto colaborativo.
Integra los tres modulos: matematicas, cuento y utilidades.
"""

import matematicas
import cuento
import utilidades

def menu():
    print("\n" + "=" * 45)
    utilidades.saludar("Grupo de Desarrollo")
    print("=" * 45)
    print("1. Operaciones Matematicas")
    print("2. Funciones de Utilidades (Promedio / Par)")
    print("3. Narrar Cuento")
    print("4. Salir")
    print("=" * 45)

def seccion_matematicas():
    print("\n-> Modulo: Matematicas <-")
    try:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        
        print(f"Suma: {matematicas.sumar(a, b)}")
        print(f"Resta: {matematicas.restar(a, b)}")
        print(f"Multiplicacion: {matematicas.multiplicar(a, b)}")
        print(f"Division: {matematicas.dividir(a, b)}")
        print(f"Potencia ({a}^{b}): {matematicas.potencia(a, b)}")
    except ValueError as e:
        print(f"Error: {e}")

def seccion_utilidades():
    print("\n-> Modulo: Utilidades <-")
    # Prueba de promedio
    entrada = input("Ingrese una lista de numeros separados por espacio (o Enter para lista vacia): ").strip()
    if entrada:
        numeros = [float(x) for x in entrada.split()]
    else:
        numeros = []
    
    print(f"Lista ingresada: {numeros}")
    print(f"Promedio calculado: {utilidades.promedio(numeros)}")
    
    # Prueba de paridad
    try:
        num = int(input("\nIngrese un numero entero para verificar si es par: "))
        if utilidades.es_par(num):
            print(f"El numero {num} es PAR.")
        else:
            print(f"El numero {num} es IMPAR.")
    except ValueError:
        print("Error: Debe ingresar un numero entero valido.")

def seccion_cuento():
    print("\n-> Modulo: Cuento <-")
    nombre = input("Nombre del explorador (presione Enter para usar 'Arturo'): ").strip()
    lugar = input("Lugar de la aventura (Enter para 'el bosque misterioso'): ").strip()
    objeto = input("Objeto magico (Enter para 'una llave dorada'): ").strip()
    
    # Asignar valores por defecto si el usuario los deja vacios
    p = nombre if nombre else "Arturo"
    l = lugar if lugar else "el bosque misterioso"
    o = objeto if objeto else "una llave dorada"
    
    print(cuento.narrar_cuento(personaje=p, lugar=l, objeto=o))
    print(cuento.mostrar_moraleja())

def main():
    while True:
        menu()
        opcion = input("Seleccione una opcion (1-4): ").strip()
        
        if opcion == "1":
            seccion_matematicas()
        elif opcion == "2":
            seccion_utilidades()
        elif opcion == "3":
            seccion_cuento()
        elif opcion == "4":
            print("\nFinalizando ejecucion. Proyecto colaborativo completado con exito!\n")
            break
        else:
            print("Opcion invalida. Por favor seleccione un numero entre 1 y 4.")

if __name__ == "__main__":
    main()
