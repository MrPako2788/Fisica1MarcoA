import math

def vector_por_componentes():
    x = float(input("Ingrese la componente x: "))
    y = float(input("Ingrese la componente y: "))
    return x, y

def vector_por_magnitud_direccion():
    magnitud = float(input("Ingrese la magnitud del vector: "))
    angulo_grados = float(input("Ingrese la dirección del vector en grados (desde el eje x positivo): "))
    angulo_radianes = math.radians(angulo_grados)
    x = magnitud * math.cos(angulo_radianes)
    y = magnitud * math.sin(angulo_radianes)
    return x, y

def main():
    print("=== SUMA DE VECTORES ===")
    n = int(input("¿Cuántos vectores desea sumar?: "))

    suma_x = 0.0
    suma_y = 0.0

    for i in range(n):
        print(f"\nVector #{i+1}")
        metodo = input("¿Desea ingresar el vector por (1) componentes o (2) magnitud y dirección? (1/2): ").strip()

        if metodo == "1":
            x, y = vector_por_componentes()
        elif metodo == "2":
            x, y = vector_por_magnitud_direccion()
        else:
            print("Opción inválida. Intente de nuevo.")
            continue

        print(f"Vector #{i+1} en componentes: ({x:.2f}, {y:.2f})")

        suma_x += x
        suma_y += y

    print("\n=== RESULTADO FINAL ===")
    print(f"Vector resultante en componentes: ({suma_x:.2f}, {suma_y:.2f})")

if __name__ == "__main__":
    main()
