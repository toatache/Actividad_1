while True:
    peso = float(input("Ingrese se peso en Kg ej.(45.8): "))
    altura = float(input("Ingrese su altura en m ej.(1.67): "))
    imc = peso / (altura**2)
    print("Tu IMC(Indice de Masa Corporal) es de: ", imc)
    print("Desea seguir calculando? ")
    res = input("s/otra tecla: ")
    if res == "s" or res == "S":
        print("Continuemos")
    else:
        break
print("ADIOS")