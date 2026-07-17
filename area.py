while True:
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ahora la altura: "))
    if base != 0 and altura != 0:
        area = base * altura
        print("El area es de: ", area)
    else:
        print("Ingreso un valor en cero")
    print("Desea seguir calculando? ")
    res = input("s/otra tecla: ")
    if res == "s" or res == "S":
        print("Continuemos")
    else:
        break
print("ADIOS")