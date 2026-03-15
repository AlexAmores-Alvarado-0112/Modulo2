


print("\t\n Calculadora de salud\n")

Nombre = input("Ingresa tu nombre por favor: ")

print(f"\n Hola {Nombre} ingresa los datos a continucaion para calcular tus metricas\n")

imc = float(input("Ingresa tu Indice de Masa Corporal: "))

def tiene_sobrepeso():
    sobre_p = imc >= 25.0
    if sobre_p == True:
        print("\nTiene sobrepeso: ", sobre_p )
    else:
        print("\nTienes sobrepeso: ", sobre_p)
tiene_sobrepeso()

def tiene_bajo_peso():
    bajo_p = imc <= 18.4
    if bajo_p == True:
        print("\nSe encuentra bajo peso: ", bajo_p )
    else:
        print("\nSe encuentra bajo peso: ", bajo_p, "\n")
tiene_bajo_peso()

peso_kg = float(input("ingresa tu peso en KG: "))
altura_cm = float(input("\ningresa tu altura en CM: "))
edad = int(input("\ningresa tu edad: "))
es_hombre = int(input("\ningresa 1 se eres hombre o 0 si eres mujer: "))

def calcular_calorias_diarias():
    """Formula para hombre"""
    if es_hombre >= 1:
        calorias_hombre = (88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad))
        print("\nCantidad de calorias recomendadas para un hombre: ", calorias_hombre, "calorias")
    elif es_hombre <= 0:
        """Formula para mujeres"""
        calorias_mujer = (447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad))
        print("\nCantidad de calorias recomendadas para una mujer: ", calorias_mujer, "calorias")
calcular_calorias_diarias()

def calcular_agua_diaria():
    mililitros = peso_kg * 35
    litros_agua= mililitros / 1000
    print("\nSe deben de tomar: ", litros_agua, "litros de  agua aprox\n")
calcular_agua_diaria()

def calcular_ritmo_cardiaco_maximo():
    pulsaciones = 225 - edad 
    print("las pulsaciones son: ", pulsaciones, "ppm\n")
calcular_ritmo_cardiaco_maximo()
    