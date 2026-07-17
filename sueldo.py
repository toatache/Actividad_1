while True:
    sueldo = float(input("Ingrese su salario base: "))
    impuesto = float(input("Porcentaje de impuesto: "))
    deduccion = float(input("Y la cantida de deducciones: "))
    sueldo_f = sueldo - (sueldo * (impuesto / 100)) - deduccion
    print("Su sueldo final es de: ", sueldo_f)
    print("Desea seguir calculando? ")
    res = input("s/otra tecla: ")
    if res == "s" or res == "S":
        print("Continuemos")
    else:
        break
print("ADIOS")