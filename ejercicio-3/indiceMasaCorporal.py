def validarFloat(valor):
    try:
        x=float(valor)
        return True
    except:
        return False

def calcularIndiceDeMasaCorporal(p,a):
    return p/a**2


def main():
    while True:
        x=input("Ingrese su peso en Kg:")
        if validarFloat(x):
            p=float(x)
            break
        else:
            print("Ingrese un valor float")
    while True:
        x=input("Ingrese su peso en metros:")
        if validarFloat(x):
            a=float(x)
            break
        else:
            print("Ingrese un valor float")
    indice=calcularIndiceDeMasaCorporal(p,a)
    print("Tu índice de masa corporal es: " + str(round(indice,2)))

if __name__ == "__main__":
    main()
