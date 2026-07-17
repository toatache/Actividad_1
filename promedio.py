while True:
    num1 = float(input("Ingrese un primer número: "))
    num2 = float(input("Ahora un segundo: "))
    num3 = float(input("Y el tercero: "))
    if num1 > 0 or num2 > 0 or num3 > 0:
        prom = (num1 + num2 + num3) / 3
        print("El promedion es de: ", prom)
    else:
        print("NO ingrese valores negativos")
    print("Desea seguir calculando? ")
    res = input("s/otra tecla: ")
    if res == "s" or res == "S":
        print("Continuemos")
    else:
        break
print("ADIOS")