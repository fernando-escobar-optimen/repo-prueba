

def main():
    print("Introduce el tipo de operación que deseas realizar")
    print("1.- suma")
    print("2.- resta")
    print("3.- multiplicacion")
    print("4.- división")
    operacion = int(input("Número de la operación: "))
    match operacion:
        case 1:
            n1 = int(input("Primer número"))
            n2 = int(input("Segundo número"))
            resultado = n1 + n2
        case 2:
            n1 = int(input("Primer número"))
            n2 = int(input("Segundo número"))
            resultado = n1 - n2
        case 3:
            n1 = int(input("Primer número"))
            n2 = int(input("Segundo número"))
            resultado = n1 * n2
        case 4:
            n1 = int(input("Primer número"))
            n2 = int(input("Segundo número"))
            resultado = n1 / n2
        case _:
            resultado = "No se ha identificado correctamente la operación."
    print(resultado)

if __name__ == "__main__":
    main()